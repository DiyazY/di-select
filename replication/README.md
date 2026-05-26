# Di-Select — Replication Package

This directory reproduces the numerical results presented in Sections 6 and 7 of the manuscript
**"Di-Select: A Criteria-Driven Framework for Selecting Container Orchestration Distributions in Cloud and Edge Computing"**.

## Contents

| File | Description |
|---|---|
| `sensitivity.py` | Self-contained Python implementation of the Propositionally Adjusted Scoring Function. Reproduces every fit-score percentage in Section 6 and runs the lambda sensitivity sweep (Section 6.3). |
| `base_scores.csv` | Base scores `S_{i,j}` for the seven candidates referenced in the demonstration scenarios. The five Kubernetes distributions correspond to Table 6 of the manuscript; Nomad and Docker Swarm scores are drawn from the qualitative descriptions in the Section 6.2 scoring bullets and are flagged in the column header. |
| `propositions.csv` | The 15 propositions `P_1` to `P_15` as `(source, target, polarity)` triples, matching Table 4. |
| `scenario_weights.csv` | The weight vectors for Scenarios 1 and 2. |
| `expected_output.txt` | Verbatim output of `python3 sensitivity.py` for a given commit, so a reviewer can confirm an exact byte-level reproduction. |

## How to reproduce

```bash
python3 sensitivity.py > my_output.txt
diff expected_output.txt my_output.txt
```

The script depends only on `numpy`. No external data, network access, or
authenticated services are required.

## What the script demonstrates

1. **Worked-example verification.** The k8s / k3s Reliability adjustment in
   Table 3 of the manuscript is recomputed line-by-line (k8s net = -0.10,
   k3s net = +0.80, exact match).
2. **Net proposition effects.** Three opposing pairs of propositions
   (P2 / P3, P5 / P6, P7 / P9) cancel exactly at uniform lambda. The script
   prints the resulting net adjustment edges so a reviewer can see which
   propositions have non-zero effect at uniform lambda and which do not.
3. **Scenario reproduction.** Both demonstration scenarios from Section 6
   are computed from Table 6 inputs.
4. **Lambda sensitivity sweep.** The strength factor `lambda` is varied
   uniformly over the permissible range `[0, 1]` in steps of 0.1. The
   resulting fit-score percentages and rankings are reported per scenario.
   Top-1 ranking is stable across the full sweep in both scenarios.

## Grounded Theory coding artifacts

The Structured Literature Review and Grounded Theory coding artifacts
(extractions, open / axial / selective coding, propositions, trade-off
tables, scenario walkthrough) that produced the seven constructs and
fifteen propositions are in the parent directory of this repository
(`../extractions.md`, `../open-coding.md`, `../axial-coding.md`,
`../selective-coding.md`, `../first-order-propositions.md`,
`../trade-offs.md`, `../scenario.md`).

## Notes on score derivation

- Base scores for the five empirically benchmarked Kubernetes
  distributions (k8s, k3s, k0s, KubeEdge, OpenYurt) are anchored in the
  authors' prior publications cited in Section 6.1.
- Scores for the two non-benchmarked candidates (Nomad, Docker Swarm) are
  conservative qualitative readings of the published characteristics and
  are flagged with a dagger marker in Section 6.2 of the manuscript. They
  are included only to illustrate how qualitative literature evidence
  enters the same scoring pipeline; they are not claims of empirical fit.
  A reviewer who disagrees with a particular qualitative cell can edit
  `base_scores.csv` and rerun the script.

## Limitations of this replication package

This package replicates the **internal** consistency of the scoring
function and demonstrates **illustrative** ranking behaviour. It does not
constitute external validation. The framework's practical recommendation
accuracy on real-world deployment decisions remains an open question and
is the subject of the validation roadmap described in Section 7 of the
manuscript.
