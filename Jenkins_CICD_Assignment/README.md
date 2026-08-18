# Jenkins CI/CD Pipeline Deployment Documentation

This document describes the setup and automation of the CI/CD deployment pipelines for the Flask Backend and Express Frontend applications using Jenkins on AWS EC2.

---

## 📌 Architecture & Pipeline Overview

```
[ Developer Push ] ──> [ GitHub Repo ]
                              │ (Webhook Trigger)
                              ▼
                      [ Jenkins Server ]
                       ├── Pipeline 1: Flask Backend (Port 5000)
                       └── Pipeline 2: Express Frontend (Port 3000)
                              │
                              ▼
                      [ Live Application ]
```

---

## 🚀 Part 1: Single EC2 Deployment Setup

1. **EC2 Provisioning**: Ubuntu 24.04 EC2 Instance launched in AWS (`t3.micro`).
2. **Security Group Rules**:
   - Port 22 (SSH)
   - Port 8080 (Jenkins UI)
   - Port 3000 (Express Frontend)
   - Port 5000 (Flask Backend)
3. **Environment Setup**:
   ```bash
   sudo apt update -y
   sudo apt install -y python3 python3-pip python3-venv nodejs npm git openjdk-17-jdk
   sudo npm install -g pm2
   ```

---

## 🛠️ Part 2: Jenkins Installation & Pipeline Setup

### 1. Install Jenkins on EC2:
```bash
sudo wget -O /usr/share/keyrings/jenkins-keyring.asc https://pkg.jenkins.io/debian-stable/jenkins.io-2023.key
echo "deb [signed-by=/usr/share/keyrings/jenkins-keyring.asc] https://pkg.jenkins.io/debian-stable binary/" | sudo tee /etc/apt/sources.list.d/jenkins.list > /dev/null
sudo apt update -y
sudo apt install -y jenkins
sudo systemctl start jenkins
```

### 2. Jenkins Required Plugins:
- Git Plugin
- NodeJS Plugin
- Pipeline Plugin

### 3. Pipeline Configurations:
- **`Jenkinsfile.backend`**: Automates checkout, virtual environment setup, pip dependency installation, test execution, and application restart on Port `5000`.
- **`Jenkinsfile.frontend`**: Automates checkout, npm dependency installation, test execution, and PM2 process restart on Port `3000`.

### 4. GitHub Webhook Setup:
- Navigate to GitHub Repository $\rightarrow$ **Settings** $\rightarrow$ **Webhooks** $\rightarrow$ **Add webhook**.
- Payload URL: `http://<EC2-PUBLIC-IP>:8080/github-webhook/`
- Event: `Just the push event`.
