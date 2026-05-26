#!/usr/bin/env python3
"""
Di-Select — Propositionally Adjusted Scoring Function
=====================================================

Reproduces the demonstration scenarios in Section 6 of the manuscript and
runs the lambda sensitivity sweep referenced in Section 6.3 and Section 7
(Validation roadmap).

Inputs are taken directly from the manuscript:
  - Base scores: Table 6 (Section 6.1, Score Derivation Methodology)
  - Propositions: Table 4 (Section 4, P1 to P15)
  - Scenario weights: Section 6.2 (Use Cases)

The script is self-contained (numpy only) so that a reviewer can re-run
every number in Section 6 without external state.

Usage:
    python3 sensitivity.py
"""

import numpy as np

# ── Dimensions ─────────────────────────────────────────────────────────────────
DIMS = ["Performance", "Security", "Reliability", "Maintainability",
        "Resource_Cost", "Connectivity", "Ecosystem"]
P, S, R, M, RC, C, E = range(7)

S_MAX   = 10.0
CLIP_LO = 1.0    # manuscript Sec. 5.1.3 specifies the 1--10 scale
CLIP_HI = 10.0

# ── Base scores (Table 6, Section 6.1) ────────────────────────────────────────
# Empirically benchmarked distributions are anchored in Yakubov & Hastbacka,
# ESOCC 2025 (Performance/Resource paper and Security/Resilience paper).
#
#          k8s  k3s  k0s  KubeEdge  OpenYurt
BASE_BENCH = np.array([
    [  9,   8,   8,   5,   6 ],   # Performance
    [  6,   1,   2,   6,   6 ],   # Security
    [  8,   8,   8,   7,   7 ],   # Reliability
    [  5,   9,   9,   3,   3 ],   # Maintainability
    [  4,   9,   8,   6,   5 ],   # Resource_Cost
    [  3,   5,   5,   9,   8 ],   # Connectivity
    [ 10,   8,   6,   6,   6 ],   # Ecosystem
], dtype=float)
CANDS_BENCH = ["k8s", "k3s", "k0s", "KubeEdge", "OpenYurt"]

# Qualitative literature estimates for non-benchmarked candidates.
# These are conservative readings of the published characteristics (HashiCorp
# Nomad documentation, Docker Swarm reference, CNCF landscape positioning).
# They are flagged with the dagger marker (†) in Table 6 of the manuscript.
NOMAD        = np.array([7, 5, 6, 8, 8, 4, 5], dtype=float)
DOCKER_SWARM = np.array([5, 4, 5, 8, 7, 3, 3], dtype=float)

IDX_BENCH = {name: i for i, name in enumerate(CANDS_BENCH)}

def select_cands(names, extras=None):
    """Stack base-score columns for the requested candidate list."""
    cols = []
    for name in names:
        if name in IDX_BENCH:
            cols.append(BASE_BENCH[:, IDX_BENCH[name]])
        elif extras and name in extras:
            cols.append(extras[name])
        else:
            raise KeyError(name)
    return np.column_stack(cols)

CANDS_S1   = ["k8s", "k3s", "KubeEdge", "OpenYurt", "Nomad†"]
SCORES_S1  = select_cands(CANDS_S1, extras={"Nomad†": NOMAD})

CANDS_S2   = ["k8s", "k3s", "KubeEdge", "Nomad†", "DockerSwarm†"]
SCORES_S2  = select_cands(CANDS_S2,
                          extras={"Nomad†": NOMAD, "DockerSwarm†": DOCKER_SWARM})

# ── Propositions P1–P15: (source_dim, target_dim, polarity) ───────────────────
# Polarity +1 = source increases target; -1 = source decreases target.
# (P2,P3), (P5,P6), and (P7,P9) are opposing pairs that cancel at uniform λ.
PROPOSITIONS = [
    (S,  RC, +1),  # P1:  Security        → Resource_Cost   ⬆
    (RC,  P, -1),  # P2:  Resource_Cost   → Performance     ⬇
    (RC,  P, +1),  # P3:  Resource_Cost   → Performance     ⬆  (cancels P2)
    (S,   R, -1),  # P4:  Security        → Reliability     ⬇
    (C,   R, +1),  # P5:  Connectivity    → Reliability     ⬆
    (C,   R, -1),  # P6:  Connectivity    → Reliability     ⬇  (cancels P5)
    (E,   M, +1),  # P7:  Ecosystem       → Maintainability ⬆
    (M,  RC, -1),  # P8:  Maintainability → Resource_Cost   ⬇
    (E,   M, -1),  # P9:  Ecosystem       → Maintainability ⬇  (cancels P7)
    (P,  RC, -1),  # P10: Performance     → Resource_Cost   ⬇
    (E,   S, +1),  # P11: Ecosystem       → Security        ⬆
    (S,   M, -1),  # P12: Security        → Maintainability ⬇
    (C,   P, -1),  # P13: Connectivity    → Performance     ⬇
    (RC,  S, -1),  # P14: Resource_Cost   → Security        ⬇
    (M,   R, +1),  # P15: Maintainability → Reliability     ⬆
]

# ── Core scoring functions ─────────────────────────────────────────────────────

def adjusted_scores(base, lam):
    """Return clipped adjusted score matrix S'_{i,j} for a given λ.

    base : (7, n_cands) float array
    lam  : scalar λ applied uniformly to all propositions
    """
    adj = base.copy()
    for src, tgt, pol in PROPOSITIONS:
        adj[tgt, :] += pol * lam * (base[src, :] / S_MAX)
    return np.clip(adj, CLIP_LO, CLIP_HI)

def fit_scores(adj, weights):
    """Compute F_j = Σ W_i · S'_{i,j} / (S_max · Σ W_i)."""
    w = np.array(weights, dtype=float)
    return (w[:, None] * adj).sum(axis=0) / (S_MAX * w.sum())

def rank_candidates(base, weights, candidates, lam):
    adj = adjusted_scores(base, lam)
    F   = fit_scores(adj, weights)
    order = np.argsort(-F)
    return [(candidates[i], float(F[i])) for i in order]


# ── Scenario weights (Section 6.2) ────────────────────────────────────────────
#              P,    S,    R,    M,    RC,   C,    E
W_S1     = [0.10, 0.20, 0.20, 0.10, 0.10, 0.25, 0.05]   # poor-connectivity startup
W_S2     = [0.25, 0.25, 0.15, 0.10, 0.05, 0.05, 0.15]   # enterprise cloud

LAMBDAS = np.round(np.arange(0.0, 1.05, 0.1), 2)


# ── Reporting helpers ─────────────────────────────────────────────────────────

def print_sweep(base, weights, candidates, label):
    print(f"\n{'='*78}")
    print(f"  {label}")
    print(f"{'='*78}")

    final_rank   = rank_candidates(base, weights, candidates, lam=1.0)
    sorted_cands = [r[0] for r in final_rank]

    col_w = 14
    print(f"\n  {'λ':>4}  " + "  ".join(f"{c:>{col_w}}" for c in sorted_cands))
    print("  " + "-" * (6 + (col_w + 2) * len(candidates)))

    prev = None
    for lam in LAMBDAS:
        results = rank_candidates(base, weights, candidates, lam)
        rank_names = [r[0] for r in results]
        fit_map = {n: f for n, f in results}
        row = f"  {lam:>4.1f}  " + "  ".join(
            f"{fit_map[c]*100:>{col_w-1}.1f}%" for c in sorted_cands
        )
        change = ""
        if prev is not None and rank_names != prev:
            change = f"  ← {' > '.join(rank_names[:3])}…"
        print(row + change)
        prev = rank_names

    zero = [r[0] for r in rank_candidates(base, weights, candidates, 0.0)]
    one  = [r[0] for r in rank_candidates(base, weights, candidates, 1.0)]
    print(f"\n  Ranking at λ=0.0: {' > '.join(zero)}")
    print(f"  Ranking at λ=1.0: {' > '.join(one)}")

    # Top-1 stability summary
    top1 = [rank_candidates(base, weights, candidates, l)[0][0] for l in LAMBDAS]
    if len(set(top1)) == 1:
        print(f"  Top-1 STABLE across all λ ∈ [0.0, 1.0]: {top1[0]}")
    else:
        flips = [(LAMBDAS[i], top1[i-1], top1[i])
                 for i in range(1, len(top1)) if top1[i] != top1[i-1]]
        for lam, before, after in flips:
            print(f"  Top-1 FLIP at λ={lam:.1f}: {before} → {after}")


def verify_worked_example():
    """Reproduce the worked example in Table 3 of the manuscript."""
    print("\n" + "="*78)
    print("  Verification: Worked Example (manuscript Table 3)")
    print("  Reliability adjustment for k8s and k3s at λ=1.0")
    print("  Expected: k8s net=−0.10, k3s net=+0.80")
    print("="*78)
    for name, seg, smaint, sconn in [("k8s", 6, 5, 3), ("k3s", 1, 9, 5)]:
        p4  = -1 * 1.0 * seg    / S_MAX
        p5  = +1 * 1.0 * sconn  / S_MAX
        p6  = -1 * 1.0 * sconn  / S_MAX
        p15 = +1 * 1.0 * smaint / S_MAX
        net = p4 + p5 + p6 + p15
        adj = 8 + net   # both candidates start from S_Rel = 8
        print(f"  {name}: P4={p4:+.2f}  P5={p5:+.2f}  P6={p6:+.2f}  "
              f"P15={p15:+.2f}  →  net={net:+.2f}  →  S'_Rel={adj:.2f}")


def summarise_active_props():
    """Show which (source→target) pairs survive the cancellation at uniform λ."""
    from collections import defaultdict
    net = defaultdict(int)
    for src, tgt, pol in PROPOSITIONS:
        net[(src, tgt)] += pol
    print("\n" + "="*78)
    print("  Net proposition effects at uniform λ")
    print("="*78)
    for (src, tgt), total_pol in sorted(net.items()):
        sname = DIMS[src]
        tname = DIMS[tgt]
        if total_pol == 0:
            print(f"  {sname:18s} → {tname:18s}  net = 0   (opposing pair cancels)")
        else:
            sign = "+" if total_pol > 0 else "−"
            print(f"  {sname:18s} → {tname:18s}  net = {sign}1  (active)")


# ── Main ───────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    verify_worked_example()
    summarise_active_props()

    print_sweep(
        SCORES_S1, W_S1, CANDS_S1,
        "Scenario 1 — poor-connectivity startup "
        "(Perf 10%, Sec 20%, Rel 20%, Maint 10%, RC 10%, Conn 25%, Eco 5%)",
    )

    print_sweep(
        SCORES_S2, W_S2, CANDS_S2,
        "Scenario 2 — enterprise cloud "
        "(Perf 25%, Sec 25%, Rel 15%, Maint 10%, RC 5%, Conn 5%, Eco 15%)",
    )

    print_sweep(
        BASE_BENCH, W_S1, CANDS_BENCH,
        "Reference: 5 benchmarked distributions under Scenario 1 weights",
    )
    print_sweep(
        BASE_BENCH, W_S2, CANDS_BENCH,
        "Reference: 5 benchmarked distributions under Scenario 2 weights",
    )
