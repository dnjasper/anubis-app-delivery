# Anubis Cloud Platform: Multi-Repo GitOps EKS Architecture

Enterprise-grade automated platform infrastructure leveraging Declarative Infrastructure as Code (IaC) and modern GitOps delivery paradigms for highly available container runtimes.

## 🏗️ Core Architectural Layout

*   **Infrastructure Repository (`anubis-infra-platform`):** Manages full-mesh raw VPC topologies, NAT gateway routing structures, private ECR storage registries, and AWS EKS compute node profiles utilizing Infrastructure as Code (Terraform).
*   **Application Delivery Repository (`anubis-app-delivery`):** Manages microservice deployments, network ingress controllers, Grafana tracking telemetry metrics configuration layers, and progressive environment overrides utilizing Kustomize and Flux CD.

## 🚀 Technical Capabilities Showcased

1.  **Declarative Multi-Layer Configuration:** Leverages Kustomize hierarchy (`base/` and `environments/dev/`) to achieve immutable, reproducible state tracking across distinct compute clusters.
2.  **Continuous Drift Correction & Pruning:** Embedded with a Flux CD file-watching automation engine to enforce automatic configuration drift resolution and garbage collection pruning upon target deletions.
3.  **Secure Least Privilege Provisioning:** Compute worker node instances utilize targeted AWS IAM managed roles (`AmazonEC2ContainerRegistryReadOnly`) to safely fetch software artifacts without public credential storage exposure.
4.  **Telemetry-Driven Operations:** Pre-configured with Grafana Prometheus time-series metric tracking widgets to stream container resource footprints and transaction layer traffic matrices.

## 🛠️ Verification Pass Handshake

Verify the internal cluster infrastructure health matrix metrics payload directly via local terminal tunnels:

```bash
# Verify active compute server nodes
kubectl get nodes

# Verify multi-replica pod states
kubectl get pods

# Establish local telemetry data proxy tunnel
kubectl port-forward deployment/anubis-api 8080:8080
```

