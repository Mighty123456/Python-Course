# Jenkins Setup & Troubleshooting Log

## Step-by-Step Jenkins Installation on AWS EC2 (Amazon Linux 2023)

```bash
# ── Step 1: Update system and install Java 17 ────────────────────────────────
sudo dnf update -y
sudo dnf install java-17-amazon-corretto -y
java -version   # verify: openjdk 17.x.x

# ── Step 2: Add Jenkins repository ───────────────────────────────────────────
sudo wget -O /etc/yum.repos.d/jenkins.repo \
    https://pkg.jenkins.io/redhat-stable/jenkins.repo
sudo rpm --import https://pkg.jenkins.io/redhat-stable/jenkins.io-2023.key

# ── Step 3: Install and start Jenkins ────────────────────────────────────────
sudo dnf install jenkins -y
sudo systemctl enable --now jenkins
sudo systemctl status jenkins   # confirm: active (running)

# ── Step 4: Retrieve initial admin password ───────────────────────────────────
sudo cat /var/lib/jenkins/secrets/initialAdminPassword
# Open http://<EC2-IP>:8080 and paste this password to unlock Jenkins

# ── Step 5: Install Node.js 18 + pm2 (for Express frontend + pm2 manager) ───
curl -fsSL https://rpm.nodesource.com/setup_18.x | sudo bash -
sudo dnf install nodejs -y
sudo npm install -g pm2
node -v && pm2 -v   # verify both installed

# ── Step 6: Install Python deps for Flask backend ────────────────────────────
sudo dnf install python3 python3-pip -y
pip3 install gunicorn

# ── Step 7: Allow Jenkins user to call pm2 without sudo ──────────────────────
echo "jenkins ALL=(ALL) NOPASSWD: /usr/bin/pm2" \
    | sudo tee /etc/sudoers.d/jenkins-pm2

# ── Step 8: Configure pm2 auto-startup on reboot ─────────────────────────────
sudo -u jenkins pm2 startup systemd -u jenkins --hp /var/lib/jenkins
# ⚠️ Copy-paste the exact command that pm2 prints and run it with sudo
pm2 save
```

---

## Jenkins Plugins to Install

Navigate to **Manage Jenkins → Plugins → Available plugins** and install:

1. **Pipeline** – Declarative/Scripted pipeline engine
2. **Git** – Source code checkout from GitHub
3. **GitHub** – Webhook trigger support (`githubPush()`)
4. **GitHub Integration Plugin** – Listens to GitHub push events
5. **Blue Ocean** *(recommended)* – Visual pipeline dashboard

---

## Jenkins Pipeline Job Configuration

For **each** pipeline job (Backend + Frontend):

1. **New Item** → Name (e.g. `flask-backend-pipeline`) → **Pipeline**
2. Under **Build Triggers**: ✅ check **"GitHub hook trigger for GITScm polling"**
3. Under **Pipeline**:
   - Definition: **Pipeline script from SCM**
   - SCM: **Git**
   - Repository URL: `https://github.com/Mighty123456/Python-Course.git`
   - Branch: `*/main`
   - Script Path: `Jenkins_CICD_Assignment_Final/Jenkinsfile.backend`
     *(use `Jenkinsfile.frontend` for the frontend job)*
4. **Save** → **Build Now** to verify first run

---

## GitHub Webhook Verification

1. GitHub repo → **Settings → Webhooks → Add webhook**
   - Payload URL: `http://<EC2-PUBLIC-IP>:8080/github-webhook/`
   - Content type: `application/json`
   - Trigger: ✅ **Just the push event**
2. After saving, click on the webhook → **Recent Deliveries**
3. The ping delivery should show **HTTP 200** with a green ✅
4. Push a dummy commit and confirm a new delivery appears with **HTTP 200**
5. Switch to Jenkins → the pipeline should have started automatically

---

## Challenges & Solutions

### Challenge 1: Permission Denied running pm2 inside Jenkins

- **Symptom**: Pipeline `Deploy with pm2` stage failed with `EACCES: permission denied`.
- **Root cause**: Jenkins runs as the `jenkins` system user which doesn't have write access to pm2's home directory.
- **Solution**:
  ```bash
  sudo -u jenkins pm2 startup systemd -u jenkins --hp /var/lib/jenkins
  # Run the printed command with sudo
  pm2 save
  echo "jenkins ALL=(ALL) NOPASSWD: /usr/bin/pm2" | sudo tee /etc/sudoers.d/jenkins-pm2
  ```

### Challenge 2: GitHub Webhook HTTP 403 Forbidden

- **Symptom**: GitHub webhook delivered payload but Jenkins returned `403 Forbidden`.
- **Root cause**: CSRF protection blocks unauthenticated webhook calls without proper plugin.
- **Solution**: Installed the **GitHub Plugin** and **GitHub Integration Plugin**. In the pipeline job, enabled **"GitHub hook trigger for GITScm polling"** under Build Triggers.

### Challenge 3: `gunicorn: command not found` in Pipeline

- **Symptom**: `Deploy with pm2` stage failed because gunicorn was not on PATH.
- **Root cause**: gunicorn was not installed inside the venv.
- **Solution**: Added `./venv/bin/pip install gunicorn` to the `Install Dependencies` stage in `Jenkinsfile.backend`.

### Challenge 4: Frontend `npm test` Silently Passed with No Tests

- **Symptom**: Pipeline showed green but no tests were actually run.
- **Root cause**: `package.json` had no `test` script, causing `npm test` to exit 0.
- **Solution**: Added a real test file and set `"test": "node --test"` in `package.json`.

### Challenge 5: Environment Variable Management

- **Symptom**: Express frontend could not locate the Flask API URL at runtime.
- **Solution**: Defined `BACKEND_URL = 'http://localhost:5000'` in the `environment {}` block of `Jenkinsfile.frontend` and passed it through `pm2 start` as an env var.

---

## Screenshots Checklist

Ensure the following screenshots are included in `/screenshots/`:

- [ ] Jenkins Dashboard showing both pipeline jobs
- [ ] `flask-backend-pipeline` – Blue Ocean / Stage View showing all 5 green stages
- [ ] `express-frontend-pipeline` – Blue Ocean / Stage View showing all 5 green stages
- [ ] Console output log showing Unit Tests passing
- [ ] Console output log showing `pm2 list` with both apps `online`
- [ ] `curl http://localhost:5000/api/health` returning `{"status":"healthy"}`
- [ ] `curl http://localhost:3000/health` returning `{"status":"healthy"}`
- [ ] GitHub Webhooks page – Recent Deliveries showing ✅ HTTP 200
- [ ] EC2 Security Group inbound rules
