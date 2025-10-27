# 🧾 DevOps Tools Assignment-2  
**Automated Workflow using Git, Docker, Jenkins & Kubernetes**

---

## **1️⃣ Version Control and Branching (Git)**
```bash
git init
git add .
git commit -m "Initial commit"

git branch develop
git checkout develop
git checkout -b feature/login
# (make changes)
git add .
git commit -m "Added login feature"
git checkout develop
git merge feature/login
git checkout main
git merge develop

git remote add origin https://github.com/<username>/<repo-name>.git
git push -u origin main
git push origin develop
```
📸 *Screenshot: Git branching & commits*

---

## **2️⃣ Containerization (Docker)**
```bash
docker build -t ticket-booking-app:v1 .
docker images
docker run -d -p 3000:3000 ticket-booking-app:v1
docker ps
docker stop <container_id>
docker login
docker tag ticket-booking-app:v1 <dockerhub-username>/ticket-booking-app:v1
docker push <dockerhub-username>/ticket-booking-app:v1
```
📸 *Screenshot: Docker build & running container*

---

## **3️⃣ CI/CD Pipeline (Jenkins)**
```bash
# Install Jenkins & plugins (Git, Docker, Pipeline)
sudo systemctl start jenkins
sudo systemctl enable jenkins

# Access Jenkins at: http://localhost:8080
# Create new pipeline project

# Connect GitHub repo in Jenkins
# Add DockerHub credentials in Jenkins → Manage Credentials

# Build & deploy pipeline
```
📸 *Screenshot: Jenkins pipeline & success build*

---

## **4️⃣ Deployment & Orchestration (Kubernetes)**
```bash
kubectl version
kubectl get nodes

kubectl apply -f k8s-deployment.yaml
kubectl apply -f k8s-service.yaml
kubectl get pods
kubectl get svc

kubectl scale deployment ticket-booking-deployment --replicas=5
kubectl get pods
kubectl describe svc ticket-booking-service
```
📸 *Screenshot: Pods, Services & Scaling*

---

## **5️⃣ Final Steps**
```bash
git add .
git commit -m "Final project setup with CI/CD and Kubernetes"
git push origin main
```
📸 *Screenshot: GitHub repo with all files*

---

## 📂 Folder Structure
```
/screenshots
  ├── git.png
  ├── docker.png
  ├── jenkins.png
  ├── k8s.png
Dockerfile
Jenkinsfile
k8s-deployment.yaml
k8s-service.yaml
README.md
```
