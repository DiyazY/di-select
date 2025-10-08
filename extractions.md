# Literature

Extraction criteria:

1. **Explicit mention of selection or evaluation factors for container orchestrators.**
2. **Empirical or analytical support for the factor’s relevance.**

## Extractions from documents

- Cast: 2024 Kubernetes Cost Benchmark Report. https://www.scribd.com/document/729316600/2024-Kubernetes-Cost-Benchmark-Report (2024)
  | Extracted Text | Criteria | Reference to Document |
  |---|---|---|
  | _"In clusters with 50 CPUs or more, only 13% of the CPUs that were provisioned were utilized, on average. Memory utilization was slightly higher at 20%, on average."_ | 1, 2 | Section: Key findings, Page 3 |
  | _"The trend appears unlikely to change in the near future given the widening gap between provisioned and requested CPUs between 2022 and 2023 (37% versus 43%)."_ | 1, 2 | Section: Key findings, Page 3 |
  | _"CPU utilization varies little between AWS and Azure; they both share nearly identical utilization rates of 11%. Cloud waste is lower on Google, at 17%."_ | 1, 2 | Section: Utilization by the cloud providers, Page 4 |
  | _"Overprovisioning – Clusters are provisioned with more capacity than they need. The more resources are overprovisioned and left idle in the background, the higher the cloud costs."_ | 1 | Section: The biggest drivers of overspending, Page 4 |
  | _"Unwarranted headroom in pod requests – CPU and memory requests are set higher than what Kubernetes applications actually require, leading to wasted capacity that companies pay for."_ | 1 | Section: The biggest drivers of overspending, Page 4 |
  | _"Low Spot instance usage – Many companies are reluctant to use Spot instances due to concerns over their perceived instability... there is no noticeable difference between Spot instance usage in 2022 and 2023."_ | 1, 2 | Section: The biggest drivers of overspending, Page 4 |
  | _"Provision the right type, size, and number of VMs through automation... choosing the right VMs for clusters is critical to avoid overspending on the cloud."_ | 1 | Section: How to cut cloud costs, Page 6 |
  | _"Below is an example of real-time CPU rightsizing. The requested CPU went from 0.3 CPU to 0.236, on average..." (includes detailed graph with P75, P50, P25, and max/min CPU usages)._ | 1, 2 | Section: Page 7 |
  | _"Kubernetes comes with three autoscaling mechanisms teams can use to increase resource utilization and reduce cloud waste."_ | 1 | Section: Page 8 |
  | _"Spot instances... the cost of an average CPU using on-demand is \$6.7 per hour, whereas the cost... using Spot instances is \$1.8 per hour."_ | 1, 2 | Section: Page 9 |
  | _"Branch... was able to fall back when Spot instances are reclaimed by automatically spinning up new equivalent compute instances... resulting in several millions of dollars per year in AWS Cloud compute cost savings."_ | 1, 2 | Section: Page 9 |

- Truyen, E., Van Landuyt, D., Preuveneers, D., Lagaisse, B., Joosen, W.: A comprehensive feature comparison study of open-source container orchestration frameworks. Applied sciences 9(5), 931 (2019)
  | Extracted Text | Criteria | Reference to Document |
  |---|---|---|
  | _“All container orchestration (CO) frameworks follow a declarative configuration management approach instead of an imperative configuration management approach.”_ | 1 | Section 4.1, Page 17 |
  | _“An important element of every CO framework is the scheduling algorithm used for computing on which node a container should be placed.”_ | 1 | Section 4.1, Page 18 |
  | _“All CO frameworks have a simple yet highly customizable scheduling algorithm.”_ | 1 | Section 4.1, Page 18 |
  | _“Kubernetes implements the highest number of common features, but also supports the highest number of unique features.”_ | 2 | Section 6, Page 36 |
  | _“Fifteen out of 27 sub-aspects can be considered mature and well-understood.”_ | 2 | Section 7, Page 42 |
  | _“Mesos offers support for both Docker volumes as well as CSI-based volumes.”_ | 1, 2 | Section 6, Page 39 |
  | _“Docker Swarm integrated mode offers support for all common features except authorization of CO agents on worker nodes.”_ | 1 | Section 6, Page 39 |
  | _“The sub-aspect ‘persistent volumes’ counts the most common features and the most common feature implementation strategies.”_ | 2 | Section 6, Page 35 |
  | _“The risk that a common feature will be deprecated by a CO framework without being replaced ... is less than 2%.”_ | 2 | Section 7, Page 45 |
  | _“Kubernetes is the most generic orchestration framework for 7 out of 27 sub-aspects.”_ | 2 | Section 10.1, Page 50 |
  | _“Significant differences in genericity with Docker EE and DC/OS have however not been found.”_ | 2 | Section 10.1, Page 50 |
  | _“CO frameworks offer various mechanisms to application managers for controlling scheduling decisions that influence the performance of the application.”_ | 1 | Section 4.6, Page 26 |
  | _“Mesos offers support for hard and soft limits for disk usage… Kubernetes offers support for setting a \<request, limit> pair for usage of a node’s local root partition…”_ | 1, 2 | Section 4.6, Page 26 |
  | _“All CO frameworks allow restricting the placement decision of the default scheduling algorithm by means of various user-specified constraints…”_ | 1 | Section 4.6, Page 27 |
  | _“Support for access to services from outside the cluster via the routing mesh…”_ | 1 | Section 4.3, Page 21 |
  | _“We recorded in total 626 feature additions ... only 9 ... comprised a feature update with deprecation or removal of the old implementation strategy of the feature.”_ | 2 | Section 7, Page 45 |

- Zhang, Y., Yu, H., Zhou, W., Man, M.: Application and research of iot architecture for end-net-cloud edge computing. Electronics (Basel) 12(1), 1(2023)
  | Extracted Text | Criteria | Reference to Document |
  |---|---|---|
  | _"Faster response times: When workloads are published at the edge... effectively reducing latency and increasing responsiveness..."_ | 1 | Section 2.3, Page 5 |
  | _"Edge computing enables data to be stored and processed at the edge... reducing the bandwidth consumption of the local network."_ | 1 | Section 2.3, Page 5 |
  | _"Data is generated, processed and stored on the edge device, avoiding the leakage of sensitive data... keeping the data local to the device maintains the integrity..."_ | 1 | Section 2.3, Page 6 |
  | _"EC-IoT reference architecture allows organizations to increase their computing power faster and at a lower cost..."_ | 1 | Section 2.4, Page 6 |
  | _"Different task offloading schemes significantly impact task completion latency and mobile device energy consumption."_ | 1, 2 | Section 3.1, Page 7 |
  | _"COME-UP... LSTM based user direction prediction... effectively reduces delays and energy consumption and improves resource efficiency."_ | 1, 2 | Section 3.1, Page 7 |
  | _"VM is migrated to the edge cloud data center where the user currently is... affect the VM migration policy."_ | 1 | Section 3.2, Page 7 |
  | _"Caching in the MEC increases network capacity by making content available locally, saving network bandwidth."_ | 1 | Section 3.3, Page 7 |
  | _"The system follows the design principle of maximized sharing... enable real-time processing of data and efficient utilization of heterogeneous and geo-distributed resources."_ | 2 | Section 4.2, Page 10 |
  | _"EC-IoT architecture has significant advantages in terms of service agility and bandwidth optimization, which help to improve the quality of service..."_ | 1, 2 | Section 5.1, Page 12 |
  | _"This strategy can effectively reduce the system delay of computing tasks."_ | 2 | Section 5.2, Page 14 |
  | _"Accessing smart device status and collected environmental data... help meet users’ needs for a more comfortable, safe and convenient home living experience."_ | 1 | Section 5.3, Page 15 |
  | _"Xia proposed an edge-based energy management framework... to schedule the operation time of each appliance for achieving minimum electricity cost."_ | 1, 2 | Section 5.3, Page 16 |

- Vaño, R., Lacalle, I., Sowiński, P., S-Julián, R., Palau, C.E.: Cloud-native workload orchestration at the edge: A deployment review and future directions. Sensors (Basel, Switzerland) 23(4), 2215 (2023)
  | Extracted Text | Criteria | Reference to Document |
  |---|---|---|
  | _"K3s’s minimum requirements are 256 MB of RAM for an agent node, and 512 MB for a server node with some workloads running in the agent node."_ | 1 | Section 6, Page 10 |
  | _"MicroK8s, which claims to have a minimal memory usage of around 540 MB, but its recommended memory allocation is 4 GB, which is considerably more than K3s."_ | 1, 2 | Section 6, Page 10 |
  | _"These two edge-focused distributions have been compared... giving as a result, a clear performance improvement against a classic distribution without showing significant performance differences between K3s and MicroK8s."_ | 2 | Section 6, Page 10 |
  | _"The KubeEdge architecture... translates into a low memory footprint of the EdgeCore installation... only around 70 MB."_ | 1, 2 | Section 6, Page 11 |
  | _"KubeEdge has successfully gone through a series of scalability tests... capable of orchestrating one million pods deployed across 100K edge nodes, accomplishing the K8s Service Level Indicators (SLI) and Service Level Objectives (SLO)."_ | 2 | Section 6, Page 12 |
  | _"KubeEdge’s EdgeMesh... allows for transparent communication in complex network environments and establishes high-reliability scenarios..."_ | 1 | Section 6, Page 12 |
  | _"crun achieved the goal in 1.69 s, while runC took 3.34 s."_ | 1, 2 | Section 5.1, Page 7 |
  | _"youki showed a better performance compared to runC, while crun remained as the fastest one."_ | 1, 2 | Section 5.1, Page 7 |
  | _"RunD has been able to start 200 lightweight VMs in a second and to successfully deploy 2500 of them in a machine with 384 GB of memory."_ | 2 | Section 7, Page 17 |
  | _"Wasm binaries’ tiny size, low memory footprint, great isolation, fast booting (up to 100 times faster than containers), and response times make Wasm perfect for running workloads in edge and IoT devices."_ | 1, 2 | Section 7, Page 18 |
  | _"the replacement of traditional container-based controllers with Wasm-based ones showed a reduced memory consumption of about 64%."_ | 2 | Section 7, Page 21 |

- Wang, Z., Goudarzi, M., Aryal, J., Buyya, R., Sarma, T.H., Kovvur, R.M.R.,Hernandez, S.M., Buyya, R.: Container orchestration in edge and fog computing environments for real-time iot applications. In: Computational Intelligence and Data Analytics. Lecture Notes on Data Engineering and Communications Technologies, vol. 142, pp. 1–21. Springer, Singapore (2022)
  | Extracted Text | Criteria | Reference to Document |
  |---|---|---|
  | "Firstly, orchestration techniques need to consider the heterogeneity of computing resources in different environments for complete adaptability." | 1 | Section 1, Page 5 |
  | "Edge/Fog devices are resource-limited, lightweight orchestration techniques should be deployed to free up the resources for the smooth execution of end-user applications." | 1 | Section 1, Page 5 |
  | "We choose K3s as the backbone for the hybrid computing environment because it only occupies less than half of the resources of Kubernetes..." | 1 | Section 3.1, Page 9 |
  | "The K3s server can be located at the Cloud or at the edge... as all components of FogBus2 run natively in Docker containers, we use Docker mode..." | 1 | Section 3.4, Page 10 |
  | "...the new system (i.e., O-FogBus2) enables resource limit control, health check, and self-healing from failure..." | 1 | Section 5, Page 18 |
  | "For all tested applications, the average response time is longer than the native FogBus2 framework by an average of 7%... this overhead is very lightweight and acceptable." | 2 | Section 4.1, Page 16 |
  | "The average response time is shorter by up to 29% when FogBus2 is running in the hybrid environment than when FogBus2 is running in the Cloud." | 2 | Section 4.2, Page 17 |
  | "Host Network Pattern... enables batch orchestration, health check, self-healing from failure, dynamic change, and resource utilization..." | 1 | Section 3.5, Page 14 |
  | "...placing the entire system in a hybrid computing environment can reasonably utilize the Cloud and Edge/Fog computing resources and improve system performance." | 2 | Section 4.2, Page 17 |

- Zhu, Y., Hu, Z., He, Z.: Edge intelligence service orchestration with process mining. Applied sciences 12(20), 10436 (2022)
  | Extracted Text | Criteria | Reference to Document |
  |---|---|---|
  | _"Service orchestration is based on business loads and node resources, and tasks are dispatched via MQTT topics."_ | 1 | Section 4, Page 11 |
  | _"Service orchestration achieves the best results. Only EIS results come in second place... non-orchestration warns that the result may deteriorate due to mismatches between nodes and tasks."_ | 1, 2 | Section 4, Page 11 |
  | _"This also basically shows that service delay can be significantly reduced by EIS and its service orchestration compared with centralized cloud computing."_ | 1, 2 | Section 4, Page 11 |
  | _"Performance is evaluated by the monitor of CPN Tools 4.0 in timed color set tokens."_ | 2 | Section 4, Page 10 |
  | _"Although the color set processing times significantly affect the efficiency of service orchestration, the color set resources per work node have little impact, because the conflict between nodes is not fully considered."_ | 2 | Section 4, Page 10 |
  | _"Kanban’s mode tuning can reasonably arrange service orchestration."_ | 1 | Section 4, Page 10 |
  | _"The strategy controller deployed on edge realizes the local nearby control to ensure the real-time performance of business scheduling."_ | 1 | Section 4, Page 9 |
  | _"Cloud-edge intelligent services support elastic capacity expansion to manage complex platform environments and resource expansion."_ | 1 | Section 4, Page 9 |
  | _"The system supports data security (SSL/TSL protocol communication), application security (container deployment) and platform security (based on RBAC, UAA, SSO, and JSON tokens)."_ | 1 | Section 4, Page 8 |
  | _"The edge interface provides customers with the development application of RESTful API, MQTT communication, and NodeRED data stream."_ | 1 | Section 4, Page 8 |
  | _"Simulation verification and its process instance is about to run on WISE-PaaS to evaluate the data stream engine performance and communication proxy QoS (quality of service)."_ | 1, 2 | Section 4, Page 10 |
  | _"The strategy focuses on high-level service requirements, and the specific intelligent algorithm realizes fine-grained control of edge computing nodes."_ | 1 | Section 4, Page 9 |

- EdgelessSystems: A comparison of Kubernetes engines: from basic functionality to security. https://www.edgeless.systems/resource-library/kubernetes-distributions-comparison/ (2024)
  | Extracted Text | Criteria | Reference to Document |
  |---|---|---|
  | _"GKE offers significantly more automation, including features like automatic node and control plane upgrades and GKE Autopilot, which manages worker nodes, enables cluster autoscaling, and configures sane networking and security defaults for the user."_ | 1 | Section 2, Page 1 |
  | _"Constellation... uses confidential computing and confidential VMs to create and run always-encrypted K8s clusters that are shielded from the cloud provider and potential attackers."_ | 1 | Section 2, Page 3 |
  | _"The RKE binary also builds in snapshot and restore functionality for disaster recovery."_ | 1 | Section 2, Page 4 |
  | _"With TKG, users can deploy 'management clusters'... Day-2 operations like control plane scaling and upgrades are also performed using the CLI."_ | 1 | Section 2, Page 4 |
  | _"Google Kubernetes Engine (GKE) offers confidential GKE nodes which provide encryption-in-use for Kubernetes worker nodes. This significantly reduces the attack surface..."_ | 1, 2 | Section 3, Page 6 |
  | _"By default, Constellation deploys Cilium with transparent encryption using WireGuard."_ | 1, 2 | Section 3, Page 7 |
  | _"Constellation offers a Rekor transparency log for its CLI and node images, and has adopted Level 3 of the Supply Chain Levels for Software Artifacts (SLSA) framework. Signatures and provenance information can be verified using slsa-verifier."_ | 1, 2 | Section 3, Page 7 |
  | _"OpenShift supports at-rest LUKS v2 encryption of persistent disks when using OpenShift Container Storage."_ | 1, 2 | Section 3, Page 8 |
  | _"OpenShift offers in-transit encryption when using the OVN-Kubernetes CNI. With IPSec enabled, all network traffic between nodes on the OVN-Kubernetes CNI cluster network travels through an encrypted tunnel."_ | 1, 2 | Section 3, Page 8 |
  | _"RKE1 supports multiple CNIs out of the box, like Canal, Flannel, Calico, and Weave. Depending on encryption support built-in to the CNI plugin, the user may be able to configure network encryption."_ | 1 | Section 3, Page 9 |
  | _"TKG allows users to build custom machine images, in which case the node image supply chain can be secured by the user."_ | 1 | Section 3, Page 9 |
  | _"Constellation does not rely on cloud-provider at-rest encryption and instead performs its own key management and at-rest encryption using a custom container storage interface… All cryptographic operations happen inside the trusted environment of the confidential Constellation node."_ | 1, 2 | Section 3, Page 7 |
  | _"Node images are managed and provided by AWS and provenance and transparency log information is not available to the user."_ | 1 | Section 3, Page 5 |
  | _"Azure Kubernetes Service (AKS) supports adding AMD SEV-SNP nodes as worker pools... provides encryption-in-use for Kubernetes worker nodes."_ | 1, 2 | Section 3, Page 6 |
  | _"Users can verify that AMD SEV is enabled for their confidential VMs and verify the confidential VM’s identity… With these features, users have access to launch attestation report events and integrity monitoring events."_ | 1, 2 | Section 3, Page 6 |
  | _"Constellation provides full cluster remote attestation."_ | 1, 2 | Section 3, Page 7 |

- Kjorveziroski, V., Filiposka, S.: Kubernetes distributions for the edge: serverless performance evaluation. The Journal of supercomputing 78(11), 13728–13755 (2022)
  | Extracted Text | Criteria | Reference to Document |
  |---|---|---|
  | _"One of the primary focuses is function instantiation speed as a prerequisite for efficient scale-to-zero behavior... this added complexity could also potentially affect the initial start up times of containers."_ | 1 | Section 2.1, Page 4 |
  | _"K3s has lower minimum hardware requirements... 512MB for master nodes and 256MB for worker nodes... compared to more than 2GB per node for a traditional deployment..."_ | 1, 2 | Section 3.3, Page 9 |
  | _"Kubespray... exhibits a 15% increase in the cold start delay compared to both K3s and MicroK8s."_ | 1, 2 | Section 4.1, Page 14 |
  | _"Kubespray lags in some of the more CPU intensive tests such as AES encryption/decryption and linear equation solving."_ | 1, 2 | Section 4.2, Page 17 |
  | _"Statistically significant results were obtained for 13 of the 14 functions \[in serial execution tests]... results between K3s and MicroK8s are much closer together compared to those of Kubespray."_ | 2 | Section 4.2, Page 17 |
  | _"Kubespray exhibits better performance than both K3s and MicroK8s in 6 of the 14 tests... such as model-training, pyaes, and sequential-disk-io."_ | 1, 2 | Section 4.3, Page 19 |
  | _"It is clearly visible that in all cases, OpenFaaS forks up to 4 different function processes in the same container."_ | 1, 2 | Section 4.3, Page 20 |
  | _"Under a consistent load... \[OpenFaaS native scaling] either scales to the maximum number of configured replicas or it does not scale at all."_ | 1 | Section 4.4.1, Page 21 |
  | _"MicroK8s exhibits lower response times \[than others] in varied workload HPA tests."_ | 1, 2 | Section 4.4.2, Page 22 |
  | _"Sequential read and write tests using the dd tool where a traditional Kubespray deployment shows 22% decrease in the number of total executions... and a 28% increase in the average response time."_ | 1, 2 | Section 5, Page 23–24 |
  | _"Kubespray... experienced higher average response times in both serial and parallel executions for matrix multiplication and linear equations solving."_ | 1, 2 | Section 5, Page 24 |

- Zhang, J., Jin, C., Huang, Y., Yi, L., Ding, Y., Guo, F.: Kole: breaking the scalability barrier for managing far edge nodes in cloud. In: Proceedings of the 13th Symposium on Cloud Computing, pp. 196–209. ACM, New York, NY, USA (2022)
  | Extracted Text | Criteria | Reference to Document |
  |---|---|---|
  | _"The apiserver can be stalled... the maximum in-flight requests that the apiserver can handle concurrently is by default configured to a few thousand... burst connection requests from numerous nodes can easily flood the apiserver..."_ | 1 | Section 1, Page 2 |
  | _"The etcd can be a bottleneck... loading millions of objects from an etcd can take dozens of minutes..."_ | 1, 2 | Section 1, Page 2 |
  | _"KOLE improves scalability by sacrificing the manageability of having individual objects... we snapshot the cloud state cache periodically..."_ | 1 | Section 3.2, Page 5 |
  | _"We have conducted experiments... distribute a workload specification to one million nodes in \~73 seconds, handle one million node registrations in five minutes, and rebuild the cloud state cache... in \~20 seconds..."_ | 2 | Section 3.2, Page 5 |
  | _"To evaluate the performance... distribute a workload specification... it takes ∼73 seconds to populate one workload specification to one million nodes..."_ | 2 | Section 5.3, Page 10 |
  | _"It takes ∼900 seconds to list one million node objects from the apiserver. Note that many Kubernetes controllers... need to list all nodes during the startup. The List API performance is a bottleneck..."_ | 1, 2 | Section 5.4, Page 11 |
  | _"The KOLE controller consumes ∼1.4 cores with one million nodes... the MQTT broker consumes ∼2 cores and 57.3GB memory..."_ | 2 | Section 5.2, Page 10 |
  | _"The installed node daemons consume less than 200MB memory constantly... the lite-kubelet... Containerd is used... Kubeproxy, network and storage plugins are not installed."_ | 1, 2 | Section 3.7, Page 8 |
  | _"Table 2: The overhead comparison for the node daemons... KOLE: lite-kubelet 80MB, containerd 80MB vs Kubernetes Kubelet 128MB, Kubeproxy 48MB, network plugin 48MB."_ | 1, 2 | Table 2, Page 12 |
  | _"KOLE controller publishes all n_App topics sequentially... The end-to-end performance might be improved by breaking the sequential PUBLISH API calls into batches..."_ | 1 | Section 5.3, Page 10 |
  | _"Using the gzip algorithm... reduced the number of snapshot CRs from 503 to 33 (93% reduction)... snapshot wall-clock time is ∼10 seconds..."_ | 2 | Section 5.4, Page 11 |
  | _"Figure 7 shows... ∼9.2 seconds to process one million heartbeats... the KOLE controller can mostly receive heartbeats... at the expected rate."_ | 2 | Section 5.1, Page 10 |
  | _"With one million nodes, the bulk registration takes ∼260 seconds which is about two minutes longer than that of the oracle case."_ | 2 | Section 5.5, Page 12 |

- Yang, T., Ning, J., Lan, D., Zhang, J., Yang, Y., Wang, X., Taherkordi, A.: Kubeedge wireless for integrated communication and computing services everywhere. IEEE wireless communications 29(2), 140–145 (2022)
  | Extracted Text | Criteria | Reference to Document |
  |---|---|---|
  | _"In edge computing, the ideal goal is that service is deployed and run at the edge, minimizing latency in service provisioning to users, especially for VR services and vehicle networking."_ | 1 | Section: The Edge-Mesh Architecture, Page 2 |
  | _"Service migration technology can be decomposed into a series of design steps such as service discovery, service resource allocation, service data migration, and service scheduling."_ | 1 | Section: The Edge-Mesh Architecture, Page 2 |
  | _"The recording topology is stored in a shared manner in corresponding containers, which means computing resource topology and communication topology are entirely isolated... Furthermore, the pluggable design also makes it easier to enter and leave."_ | 1 | Section: Edge Network Layer, Page 3 |
  | _"KubeEdge nodes can iterate over decisions quickly with fewer resources, which will significantly optimize service-migration decisions."_ | 1, 2 | Section: Edge Network Layer, Page 4 |
  | _"The dynamic node can also be seen as a mobile router participating in networking... Then, based on the edge mesh architecture, the ability of service migration and computing, communication, and caching resource allocation can be archived, greatly improving the efficiency of edge devices resource allocation."_ | 1, 2 | Section: Scenario of KEW, Page 4 |
  | _"Fast and flexible mesh technology is necessary... By the Edge-mesh architecture, a large computing block is broken down into small pieces, which will enable the service to respond more accurately and quickly."_ | 1, 2 | Section: Potential Research Issues, Page 5 |
  | _"In the Kube-mesh architecture, the networking strategy requires computing, communication, and caching (3C) resource work by machine learning algorithms."_ | 1 | Section: Potential Research Issues, Page 5 |
  | _"The edge-mesh framework also supports 3C resource allocation optimization by configuring the network environment according to the characteristics of AI services."_ | 1 | Section: Conclusions and Future Work, Page 5 |

- humanitec: Kubernetes Benchmarking Study 2022. https://humanitec.com/whitepapers/kubernetes-benchmarking-study-2022 (2022)
  | Extracted Text | Criteria | Reference to Document |
  |---|---|---|
  | _"Security is the first area that is often misunderstood when it comes to adopting K8s. \[...] Kubernetes is not secure per default."_ | 1 | Section: Technical challenges & best practices, Page 11 |
  | _"According to the 2021 State of Kubernetes Security Report by Redhat, 94% of respondents experienced at least one security incident in their Kubernetes environments in the last 12 months."_ | 2 | Section: Technical challenges & best practices, Page 11 |
  | _"For 70.67% of our respondents K8s security is a big topic. While 100% of top performers use a secrets management tool like Vault..."_ | 1, 2 | Section: Technical challenges & best practices, Page 11 |
  | _"Storing application configurations as code is a clear best practice and a determining factor in the success of your Kubernetes setup implementation."_ | 1 | Section: Application configuration management, Page 13 |
  | _"Close to 30% of low performing organizations apply changes manually, \[...] a higher percentage of top performers have a solution like Helm or Kustomize..."_ | 1, 2 | Section: Application configuration management, Page 13 |
  | _"Low performers fiddle with infrastructure on a case-by-case basis, \[...] top performers follow an IaC approach or build provisioning into their deployment pipeline."_ | 1, 2 | Section: Infrastructure provisioning, Page 15 |
  | _"Better documentation and visualization of your K8s setup not only means it’s easier and safer to expose more developers to it. You can also observe a much faster onboarding in high performing teams."_ | 1, 2 | Section: Onboarding time, Page 19 |
  | _"Developers can self-serve K8s namespaces for feature and preview environments in 73.4% of cases. That is true for only 33.3% of low performers."_ | 1, 2 | Section: Degree of developer self-service, Page 20 |
  | _"89.1% of the top performers are able to deploy to dev or staging on their own and on demand."_ | 1, 2 | Section: Degree of developer self-service, Page 21 |
  | _"Top performers document their Kubernetes setup overwhelmingly more accurately than low performers."_ | 1, 2 | Section: Documentation, Page 18 |
  | _"Only 22.4% of low performers have all services containerized, compared to 68.5% of top performers."_ | 1, 2 | Section: Implementation state of Kubernetes, Page 7 |

- Koziolek, H., Eskandani, N.: Lightweight kubernetes distributions: A performance comparison of microk8s, k3s, k0s, and microshift. In: ICPE 2023 - Proceedings of the 2023 ACM/SPEC International Conference on Performance Engineering, pp. 17–29. ACM, New York, NY, USA (2023)
  | Extracted Text | Criteria | Reference to Document |
  |---|---|---|
  | _"While k3s and k0s showed by a small amount the highest control plane throughput and MicroShift showed the highest data plane throughput, usability, security, and maintainability are additional factors that drive the decision..."_ | 1 | Abstract, Page 17 |
  | _"k0s showed the lowest resource utilization, while k3s and k0s achieved the highest control plane performance in terms of high throughput and low latency. MicroShift managed the high throughput in data plane stress scenario."_ | 1, 2 | Section 1, Page 17 |
  | _"Table 3 provides the GQM template framing our experiments... Metrics of main interest here are total CPU and memory utilization of respective nodes..."_ | 1 | Section 4, Page 20 |
  | _"CPU utilization (M1_1)... is on average between 12.49% (k0s) and 20.43% (k3s)... Memory utilization (M1_2) is almost constant during idling... Controller nodes naturally show a higher memory utilization (19–27%)..."_ | 1, 2 | Section 5.1, Page 22 |
  | _"M2_1: throughputs in pods/min of 115.18 (MicroK8s), 133.73 (k3s), 129.42 (k0s), 62.05 (MicroShift single node). M2_2: pod creation latencies in ms of 10.31 (MicroK8s), 9.01 (k3s), 9.34 (k0s), 18.12 (MicroShift single node)."_ | 1, 2 | Section 5.2, Page 25 |
  | _"MicroK8s shows the highest latencies with 'delete' operations going up to a maximum of 470 ms... k0s was significantly faster in deleting deployment compared to the other distributions."_ | 1, 2 | Section 5.2, Page 24 |
  | _"In data plane stress scenarios, the distributions could handle between 17172 (k0s), 10537 (k3s), 14819 (MicroK8s), and 18354 (MicroShift) operations per second... required latencies of 11.6 ms (k0s)... 10.9 ms (MicroShift)."_ | 1, 2 | Section 5.3, Page 25 |
  | _"MicroShift was the fastest distribution here, showing average latencies 15 percent shorter than MicroK8s and 38 percent shorter than k3s."_ | 2 | Section 5.3, Page 25 |
  | _"k3s has been consequently designed to reduce binary size (64.5 MB) and memory footprint targeting resource constrained edge clusters besides developer workstations."_ | 1 | Section 6.2, Page 26 |
  | _"k0s... was done with security in mind, allowing a 100% FIPS compliance if a proper toolchain is in place... can potentially be quickly fixed within k0s..."_ | 1 | Section 6.2, Page 27 |

- Kim, S.-H., Kim, T.: Local scheduling in kubeedge-based edge computing environment. Sensors (Basel, Switzerland) 23(3), 1522 (2023)
  | Extracted Text | Criteria | Reference to Document |
  |---|---|---|
  | _“We evaluated the performance of KubeEdge in terms of the number of pods of individual edge nodes, the pod distribution on edge nodes, and the delay between edge nodes...”_ | 1 | Section 5, Page 7 |
  | _“When the number of concurrent requests was increased to 16, the maximum throughput of one pod was 308 req/s, whereas four pods could handle 779 req/s user requests.”_ | 2 | Section 5.2, Page 8 |
  | _“The response time decreased from 113 ms for one pod to 42 ms for four pods when the number of concurrent requests was 16.”_ | 2 | Section 5.2, Page 8 |
  | _“We evaluated the effect of pod distribution on edge nodes as well as the delay between edge nodes...”_ | 1 | Section 5.3, Page 8 |
  | _“...the pod distributions 4-4-4, 8-3-1, and 10-1-1 show about 755 req/s, 1180 req/s, and 1682 req/s, respectively, for 16 concurrent requests.”_ | 2 | Section 5.3, Page 10 |
  | _“...the response time in the 4-4-4 pod distribution is approximately 10~14.5 ms for a 15 ms delay, and it increases to 15~20 ms for a 30 ms delay...”_ | 2 | Section 5.3, Page 10 |
  | _“We evaluated the effect of the load-balancing schemes by comparing the round-robin scheme in EdgeMesh and the proposed local scheduling scheme.”_ | 1 | Section 5.4, Page 10 |
  | _“In the local scheduling scheme, all the incoming traffic is processed at the edge nodes that receive the traffic...results in a low response time of approximately 8 ms regardless of the traffic pattern.”_ | 2 | Section 5.4, Page 11 |
  | _“...the 4:4:4, 8:3:1, and 10:1:1 traffic distributions achieve throughputs of approximately 1493, 1646, and 1644 req/s, respectively.”_ | 2 | Section 5.4, Page 11 |
  | _“...load-balancing traffic to remote edge nodes degrades the performance of the KubeEdge cluster in an edge computing environment.”_ | 1 | Section 4.2, Page 6 |
  | _“...the proposed scheme reduces the latency by preventing traffic forwarding between edge nodes in an edge computing environment and improves the throughput of the overall system...”_ | 2 | Section 4.2, Page 6 |

- Phuc, L.H., Kundroo, M., Park, D.-H., Kim, S., Kim, T.: Node-based horizontal pod autoscaler in kubeedge-based edge computing infrastructure. IEEE access 10, 1–1 (2022)
  | Extracted Text | Criteria | Reference to Document |
  |---|---|---|
  | _"Load balancing is an important aspect to be considered for providing seamless services in any computing environment."_ | 1 | Section III.A, Page 3 |
  | _"Forwarding requests to nodes without knowing the status of their resources can result in non-optimal results... resulting in degraded overall performance."_ | 1, 2 | Section III.A, Page 4 |
  | _"KE lacks dynamic scaling of the number of pods, which limits its ability to handle incoming requests effectively."_ | 1 | Section V.C, Page 8 |
  | _"NHPA exhibits a steady increment in response time from 2.6 ms to 4.9 ms... allocating a sufficient number of pods... for 1, 3, 5, and 9 concurrent requests respectively."_ | 2 | Section V.C, Page 8 |
  | _"NHPA improves throughput by allocating pod resources proportionally to the network traffic volume that accesses each node."_ | 1, 2 | Section V.C, Page 8 |
  | _"NHPA dynamically allocates the number of pods to 5-5-5, 8-4-4, and 9-2-2 to accommodate each traffic pattern..."_ | 1, 2 | Section V.B, Page 7 |
  | _"NHPA achieves approximately 219%, 81%, and 18% higher throughput than KE (1-1-1), KE (3-3-3), and KE (6-6-6), respectively..."_ | 2 | Section V.D, Page 9 |
  | _"KE lacks an HPA functionality, edge nodes cannot allocate more resources dynamically to handle heavy traffic demands."_ | 1 | Section II, Page 2 |
  | _"The throughput and response time of NHPA were reduced by a factor of 3 and 25, respectively."_ | 2 | Conclusion, Page 9 |
  | _"Each node in the NHPA adjusts the number of pods dynamically and independently, according to the traffic load from the other edge nodes."_ | 1, 2 | Section V.D, Page 8 |
  | _"Table 1 shows that the number of pods in KE remains constant regardless of traffic types, whereas NHPA adjusts them to adapt to the traffic distribution."_ | 1, 2 | Section V.B, Page 7 |
  | _"NHPA independently adjusts the number of pods on nodes to maximize the application performance regarding response time and throughput in a KE-based edge computing environment."_ | 1 | Section IV.B, Page 6 |

- Čilić, I., Krivić, P., Podnar Žarko, I., Kušek, M.: Performance evaluation of container orchestration tools in edge computing environments. Sensors (Basel, Switzerland) 23(8), 4008 (2023)
  | Extracted Text | Criteria | Reference to Document |
  |---|---|---|
  | _"Custom scheduling policies and ease of configuration across different networks are the focus of our examination of the existing tools..."_ | 1 | Section 3, Page 3 |
  | _"Most of the works implementing scheduling use latency as the main scheduling parameter."_ | 1, 2 | Section 2, Page 8 |
  | _"The overhead of running the Kubernetes worker node on a Raspberry Pi is approximately the same as running a K3s or KubeEdge worker node..."_ | 2 | Section 4.2.1, Page 16 |
  | _"Kubernetes, K3s, and KubeEdge show \~50 MB memory footprint... ioFog shows \~240 MB, indicating its unsuitability for constrained devices."_ | 1, 2 | Section 4.2.1, Page 16 |
  | _"K3s uses a tunnel proxy... to enable communication towards nodes in private networks..."_ | 1 | Section 3.1.2, Page 10 |
  | _"The main feature that enabled the inclusion of edge nodes to the remote cloud using the KubeEdge platform is the bi-directional WebSocket..."_ | 1 | Section 3.1.3, Page 11 |
  | _"Kubernetes shows the best performance, with a startup time of approximately 1.8 s."_ | 1, 2 | Section 4.2.2, Page 17 |
  | _"ioFog is by far the worst performer... startup time of 34.5 s and migration time of 23.2 s, due to long request processing time at the controller."_ | 1, 2 | Section 4.2.2, Page 17 |
  | _"KubeEdge introduces CloudCore and EdgeCore... affects performance."_ | 1, 2 | Section 4.2.2, Page 17 |
  | _"Using SQLite instead of the default etcd affects the footprint of the controller, but not the worker node."_ | 1, 2 | Section 4.3, Page 18 |
  | _"None of the selected tools offer a solution to monitor and schedule services based on client QoS parameters."_ | 1 | Section 4, Page 14 |
  | _"Kubernetes does offer customization of its scheduling logic... but cannot specify custom variable QoS parameters or perform re-scheduling."_ | 1 | Section 3.2, Page 13 |

- Fogli, M., Kudla, T., Musters, B., Pingen, G., Broek, C., Bastiaansen, H., Suri, N., Webb, S.: Performance evaluation of kubernetes distributions (k8s, k3s, kubeedge) in an adaptive and federated cloud infrastructure for disadvantaged tactical networks. In: 2021 International Conference on Military Communication and Information Systems (ICMCIS), pp. 1–7. IEEE, ??? (2021)
  | Extracted Text | Criteria | Reference to Document |
  |---|---|---|
  | _"cluster initialization time increases when either the network quality degrades ... or the cluster gets bigger ... however, the decline in performance is the smallest for all KubeEdge experiments."_ | 1, 2 | Section V.A, Page 5 |
  | _"KubeEdge manages to succeed in more experiment setups ... due to its enhanced cloud/edge communication architecture and the underlying QUIC protocol ... instead of TCP..."_ | 1, 2 | Section V.A, Page 5 |
  | _"KubeEdge’s communication is not impacted as much ... traffic is 4.4× larger for K8s, 6× for K3s, and only 2.3× for KubeEdge."_ | 1, 2 | Section V.B, Page 5 |
  | _"With TCP + TLS, it becomes an overhead to establish / re-establish connections frequently due to intermittent networks. In such scenarios, QUIC ... can help reduce this overhead."_ | 1, 2 | Section V.B, Page 5 |
  | _"KubeEdge never exceeds more than 74kBit/s ... whereas K8s uses up to 102kBit/s and K3s up to 309kBit/s for the same task."_ | 1, 2 | Section V.C, Page 6 |
  | _"In the worst network scenario K8s would consume up to 38%, K3s up to 52.9% and KubeEdge only 22.1% of the available bandwidth."_ | 1, 2 | Section V.C, Page 6 |
  | _"As the cluster size grew to twelve nodes, experiments involving K8s and K3s failed, whereas those using KubeEdge succeeded."_ | 1, 2 | Section V.D, Page 6 |
  | _"Under the worst network scenario, K8s, K3s and KubeEdge failed consistently ... Kubernetes cannot be deployed on TNs affected by such disadvantaged conditions."_ | 1, 2 | Section V.D, Page 6 |
  | _"the average bandwidth consumption ... can help with planning current and future mission networks."_ | 1 | Section VI, Page 7 |
  | _"several small clusters are preferable to a single large one."_ | 1 | Section VI, Page 7 |

- Zhang, J.: Research on optimization strategy of container orchestration technology for cloud computing environment. Applied mathematics and nonlinear sciences 9(1) (2024)
  | Extracted Text | Criteria | Reference to Document |
  |---|---|---|
  | _"The orchestration strategy usually needs to consider three aspects: ... does not consider the time dimension."_ | 1 | Section 2.3, Page 6 |
  | _"The PBFDR policy is compared with the Spread orchestration policy and Binpack orchestration policy ... comparing the average resource utilization of the three policies."_ | 2 | Section 4.1.2, Page 10 |
  | _"The utilization of CPU, memory, network bandwidth, and disk IO by the PBFDR policy is 53.14%, 63.85%, 59.83 %, and 68.76%, respectively."_ | 2 | Section 4.1.2, Page 10 |
  | _"The utilization of each resource of the PBFDR strategy is 59.04%, 58.04%, 66.78%, and 51.03%, respectively, which is a more reasonable and balanced allocation of resources compared with the other strategies."_ | 1, 2 | Section 4.1.2, Page 11 |
  | _"Rancher and Docker Swarm use the default orchestration policy ... using resource utilization and load balancing as performance indicators to measure performance."_ | 1 | Section 4.2.1, Page 12 |
  | _"KLLPL’s load balancing is at 13% for different deployment sizes and 13% for different deployment sizes. According to different deployment sizes, KLLPL has an average load balancing degree of 13.7%..."_ | 2 | Section 4.2.2, Page 13 |
  | _"The resource utilization equilibrium point of KLLPL is around 23%, while the resource utilization of Rancher and Docker Swarm will be unbalanced as the deployment scale increases..."_ | 1, 2 | Section 4.2.2, Page 12 |
  | _"Container orchestration strategies achieve memory utilization above 60%." (Figure 4 and surrounding text)_ | 2 | Section 4.1.2, Page 10 |
  | _"In this paper, different container orchestration technology optimization strategies are compared and analyzed from four aspects: CPU, memory, network bandwidth, and disc IO utilization..."_ | 1 | Section 5, Page 13 |
  | _"This paper suggests an optimization strategy ... PBFDR strategy that utilizes CPU, memory, network bandwidth, and disk IO in a more reasonable and balanced manner..."_ | 1 | Abstract, Page 1 |

- Bahy, M.B., Dwi Riyanto, N.R., Fawwaz Nuruddin Siswantoro, M.Z., Santoso, B.J.: Resource utilization comparison of kubeedge, k3s, and nomad for edge computing. In: 2023 10th International Conference on Electrical Engineering, Computer Science and Informatics (EECSI), pp. 321–327. IEEE, ??? (2023)
  | Extracted Text | Criteria | Reference to Document |
  |---|---|---|
  | _“One of the critical factors in choosing an edge computing platform is resource utilization, as it directly impacts the performance, scalability, and security of the platform.”_ | 1 | Introduction, Page 1 |
  | _“Nomad is the orchestrator that gets the lowest average CPU usage and is the most efficient among other orchestrators on the ARM node.”_ | 1, 2 | Section V.A, Page 4 |
  | _“Nomad also has the lowest CPU usage, namely 1.21% \[on master node]... on an x86 node... Nomad Orchestrator still had the lowest average CPU usage.”_ | 1, 2 | Section V.A, Page 4–5 |
  | _“Nomad becomes the container which more efficient in memory consumption than others in ARM worker node... master node... and on the x86 worker node.”_ | 1, 2 | Section V.B, Page 5–6 |
  | _“Nomad demonstrates a superior level of memory efficiency compared to the others on fresh install state.”_ | 1, 2 | Section V.B, Page 5 |
  | _“K3s continues to have the lowest average storage usage, totalling 2371 MB \[ARM node]... K3s remains the most storage-efficient on the x86 node, utilizing only 2620 MB...”_ | 1, 2 | Section V.C, Page 6–7 |
  | _“K3s shows an impressive level of efficiency in terms of storage resource utilization, as evidenced by its average usage in the deployment state.”_ | 1, 2 | Section V.C, Page 7 |
  | _“The scenario testing is to evaluate the resource utilization of each orchestrator, such as K3s, Nomad, and KubeEdge. The test scenarios include measuring CPU usage, memory usage, and storage usage.”_ | 1 | Conclusion, Page 7 |
