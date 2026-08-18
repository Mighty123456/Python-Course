# Jenkins CI/CD Pipeline Assignment

**Repository**: https://github.com/Mighty123456/Python-Course  
**EC2 Instance**: Amazon Linux 2023 · `t2.micro` · Jenkins on port `8080`

> Every `git push` to the `main` branch automatically triggers Jenkins (via GitHub Webhook) to pull the latest code, run unit tests, and deploy both applications using **pm2**.

---

## 📁 Project Structure

```
Jenkins_CICD_Assignment_Final/
├── Jenkinsfile.backend        # Declarative Pipeline – Flask REST API
├── Jenkinsfile.frontend       # Declarative Pipeline – Express Frontend
├── ecosystem.config.js        # pm2 process manager configuration (both apps)
├── backend/
│   ├── app.py                 # Flask application (health + CORS)
│   ├── test_app.py            # Unit tests (unittest)
│   ├── Dockerfile             # (reference only – not used by Jenkins)
│   └── requirements.txt
├── frontend/
│   ├── server.js              # Express web app (calls Flask API)
│   ├── package.json           # npm scripts incl. test runner
│   ├── Dockerfile             # (reference only – not used by Jenkins)
│   └── views/index.ejs
├── screenshots/               # Jenkins pipeline + webhook proof screenshots
├── JENKINS_GUIDE.md           # Installation steps + troubleshooting log
└── README.md
```

---

## ⚙️ AWS EC2 Security Group – Inbound Rules

| Port | Protocol | Source    | Purpose                    |
|------|----------|-----------|----------------------------|
| 22   | TCP      | 0.0.0.0/0 | SSH Administration         |
| 8080 | TCP      | 0.0.0.0/0 | Jenkins Web UI             |
| 3000 | TCP      | 0.0.0.0/0 | Express Frontend           |
| 5000 | TCP      | 0.0.0.0/0 | Flask REST API             |

---

## 🔧 Jenkins Installation (Amazon Linux 2023)

```bash
# 1. Install Java 17 (required by Jenkins)
sudo dnf update -y
sudo dnf install java-17-amazon-corretto -y

# 2. Add Jenkins repo and import GPG key
sudo wget -O /etc/yum.repos.d/jenkins.repo \
    https://pkg.jenkins.io/redhat-stable/jenkins.repo
sudo rpm --import https://pkg.jenkins.io/redhat-stable/jenkins.io-2023.key

# 3. Install and start Jenkins
sudo dnf install jenkins -y
sudo systemctl enable --now jenkins

# 4. Print initial admin password
sudo cat /var/lib/jenkins/secrets/initialAdminPassword
```

---

## 📦 pm2 Installation & Setup on EC2

```bash
# Install Node.js 18 LTS (required for pm2 + Express frontend)
curl -fsSL https://rpm.nodesource.com/setup_18.x | sudo bash -
sudo dnf install nodejs -y

# Install pm2 globally
sudo npm install -g pm2

# Allow Jenkins user to run pm2 without sudo (add to sudoers)
echo "jenkins ALL=(ALL) NOPASSWD: /usr/bin/pm2" | sudo tee /etc/sudoers.d/jenkins-pm2

# Configure pm2 to auto-start on EC2 reboot
pm2 startup systemd -u jenkins --hp /var/lib/jenkins
# ⚠️ Run the exact command printed above as sudo

# Install pip / gunicorn for Flask
sudo dnf install python3-pip -y
pip3 install gunicorn
```

---

## 🔌 Required Jenkins Plugins

Install these via **Manage Jenkins → Plugins → Available**:

| Plugin | Purpose |
|--------|---------|
| **Pipeline** | Declarative pipeline support |
| **Git** | Checkout from GitHub |
| **GitHub** | Webhook trigger (`githubPush()`) |
| **GitHub Integration** | Push-event build trigger |
| **Blue Ocean** *(optional)* | Visual pipeline dashboard |

---

## 🔗 GitHub Webhook Configuration

1. Go to your GitHub repo → **Settings → Webhooks → Add webhook**
2. **Payload URL**: `http://<EC2-PUBLIC-IP>:8080/github-webhook/`
3. **Content type**: `application/json`
4. **Which events?**: ✅ *Just the push event*
5. Click **Add webhook** — GitHub will send a ping; verify the green ✅ tick under **Recent Deliveries**

In each Jenkins Pipeline job, check **"GitHub hook trigger for GITScm polling"** under **Build Triggers**.

---

## 🔄 Jenkins Pipeline Stages

Both `Jenkinsfile.backend` and `Jenkinsfile.frontend` execute these **5 automated stages**:

| Stage | Backend | Frontend |
|-------|---------|---------|
| **Checkout Code** | `git clone main` | `git clone main` |
| **Install Dependencies** | `python3 -m venv` + `pip install` + `gunicorn` | `npm install` |
| **Run Unit Tests** | `python -m unittest discover` | `npm test` |
| **Deploy with pm2** | `pm2 start gunicorn` (port 5000) | `pm2 start server.js` (port 3000) |
| **Verify Deployment** | `curl /api/health` | `curl /health` |

---

## 🚀 Manual pm2 Commands (using ecosystem.config.js)

```bash
# Start both apps
pm2 start ecosystem.config.js

# Check running processes
pm2 list

# View live logs
pm2 logs flask-backend
pm2 logs express-frontend

# Reload apps without downtime (after code change)
pm2 reload ecosystem.config.js

# Stop all apps
pm2 stop ecosystem.config.js

# Save process list (survives EC2 reboot)
pm2 save
```

---

## 🛠 Troubleshooting

| Problem | Solution |
|---------|----------|
| Jenkins can't run `pm2` | Add jenkins to sudoers: `echo "jenkins ALL=(ALL) NOPASSWD: /usr/bin/pm2" \| sudo tee /etc/sudoers.d/jenkins-pm2` |
| Webhook returns 403 | Install **GitHub** and **GitHub Integration** plugins; enable "GitHub hook trigger" in job config |
| Flask port 5000 already in use | `pm2 delete flask-backend` then re-run pipeline |
| `gunicorn: command not found` | Run `./venv/bin/pip install gunicorn` inside backend dir |
| `npm test` fails with no test script | Add `"test": "node --test"` to `package.json` scripts |
