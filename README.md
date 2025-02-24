# Cloud-Native Monitoring Application Deployment

## Overview
This project demonstrates the end-to-end deployment of a cloud-native monitoring application on AWS EKS. It showcases expertise in Kubernetes, Docker, AWS IAM, ECR, and troubleshooting real-world deployment challenges. The application monitors system resources using Python and Flask, providing a visual representation of CPU and memory usage.

---

## Tech Stack
- **Cloud Provider**: AWS (IAM, EKS, ECR)
- **Containerization**: Docker
- **Orchestration**: Kubernetes (kubectl, manifests)
- **Backend**: Python, Flask
- **Monitoring**: `psutil` (CPU & memory usage)
- **Automation**: AWS CLI, Boto3

---

## Key Features
✅ **Cloud-Native Deployment**: Fully deployed on AWS EKS using Kubernetes manifests.  
✅ **Secure IAM Configuration**: Least-privilege AWS IAM setup for secure access.  
✅ **Dockerized Application**: Efficient containerization and registry management with AWS ECR.  
✅ **Optimized Node Group**: Cost-effective Kubernetes cluster provisioning.  
✅ **CI/CD Ready**: Potential integration with GitHub Actions for automated deployments.  
✅ **Troubleshooting & Debugging**: Hands-on experience in diagnosing and resolving Kubernetes issues.  

---

## Deployment Steps

### 1️⃣ AWS IAM Configuration
1. **Created an IAM User**: Configured necessary permissions for AWS services.
2. **Configured IAM Locally**:
   ```sh
   aws configure
   ```
3. **Verified IAM Setup**:
   ```sh
   aws iam list-users
   ```

### 2️⃣ Environment Setup
1. **Installed Kubernetes CLI**:
   ```sh
   sudo apt install -y kubectl
   ```
2. **Developed Python Monitoring App**:
   - Uses `psutil` to track CPU & memory.
   - Serves metrics using Flask (`render_template` for `index.html`).

### 3️⃣ Dockerizing the Application
1. **Created Dockerfile** (with dependency management and exposed port 5000).
2. **Built and Ran Docker Container**:
   ```sh
   docker build -t monitoring-app .
   docker run -p 5000:5000 monitoring-app
   ```
3. **Resolved Docker Issues**:
   - Fixed incorrect port binding warnings.

### 4️⃣ AWS ECR Setup
1. **Created an ECR Repository Using Boto3**:
   ```python
   import boto3
   client = boto3.client('ecr')
   response = client.create_repository(repositoryName='monitoring-app')
   print(response)
   ```
2. **Pushed Docker Image to ECR**:
   ```sh
   aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin <aws-account-id>.dkr.ecr.us-east-1.amazonaws.com
   docker tag monitoring-app:latest <aws-account-id>.dkr.ecr.us-east-1.amazonaws.com/monitoring-app:latest
   docker push <aws-account-id>.dkr.ecr.us-east-1.amazonaws.com/monitoring-app:latest
   ```

### 5️⃣ Kubernetes Deployment on AWS EKS
1. **Created an EKS Cluster**:
   ```sh
   eksctl create cluster --name cloud-native-cluster --region us-east-1
   ```
2. **Configured Node Group (Optimized Cost by Using `t2.micro`)**
3. **Deployed Kubernetes Manifest Files**:
   ```sh
   kubectl apply -f deployment.yaml
   ```
4. **Exposed the Application**:
   ```sh
   kubectl expose deployment monitoring-app --type=LoadBalancer --port=80 --target-port=5000
   ```
5. **Updated Kubernetes Cluster Config**:
   ```sh
   aws eks update-kubeconfig --name cloud-native-cluster
   ```

### 6️⃣ Troubleshooting & Debugging
1. **Checked Service Status**:
   ```sh
   kubectl get svc
   ```
2. **Debugged Failures Using `kubectl describe`**:
   ```sh
   kubectl describe pod <pod-name>
   ```
3. **Forwarded Service for External Access**:
   ```sh
   kubectl port-forward svc/monitoring-app 8080:5000
   ```

---

## Outcome
🚀 Successfully deployed a cloud-native monitoring application on AWS Kubernetes, accessible via port forwarding.  
📌 Demonstrated proficiency in DevOps tools, cloud deployment, container orchestration, and troubleshooting real-world infrastructure issues.  
🛠️ Open for improvements—potential to integrate CI/CD pipelines for automated deployment!

---


## Author
**Mirang Bhandari**  
[LinkedIn](https://www.linkedin.com/in/mirangbhandari) • [GitHub](https://github.com/mirangbhandari)
