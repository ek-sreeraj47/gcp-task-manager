# 📦 GCP Task Manager (Flask + PostgreSQL + Cloud Run)

This is a cloud-based task manager app built using **Python Flask** and **PostgreSQL**, deployed on **Google Cloud Platform (GCP)** using **Cloud Run**. This project helped me explore real-world DevOps practices like containerization, CI/CD automation, and managed cloud services.

---

## 🛠 Tech Stack Used

- **Backend**: Python Flask
- **Database**: PostgreSQL (Cloud SQL)
- **Cloud Platform**: Google Cloud Platform (GCP)
- **Containerization**: Docker
- **Deployment**: Cloud Run
- **CI/CD**: GitHub Actions + Cloud Build
- **Authentication**: IAM & Service Accounts
- **Monitoring**: Cloud Logging (basic)

---

## 🚀 Features

- Add and retrieve tasks using a REST API
- Persistent data storage with Cloud SQL
- Dockerized and container-ready
- Public deployment via Cloud Run
- Automated CI/CD using GitHub Actions and Cloud Build

---

## 📁 Project Structure

gcp-task-manager/
├── app.py # Flask application
├── requirements.txt # Python dependencies
├── Dockerfile # Container definition
├── .env # Local environment variables
└── .github/workflows/ # GitHub Actions CI/CD workflow


---

## ⚙️ Project Workflow

1. **Flask API**:
   - Simple app with a basic `/` route
   - Connects to a PostgreSQL database hosted on Cloud SQL

2. **Docker Containerization**:
   - The app is containerized using a minimal Dockerfile
   - Built and tested locally and in Cloud Build

3. **Cloud SQL (PostgreSQL)**:
   - Hosted in `us-central1` region
   - Used for storing task data securely

4. **Cloud Run Deployment**:
   - Cloud Run hosts the Docker image with autoscaling
   - Environment variables securely injected during deployment

5. **CI/CD Automation**:
   - GitHub Actions triggers Cloud Build on every push to `main`
   - The latest container is built and deployed automatically

---
 Key Learnings
Working with GCP services like Cloud Run and Cloud SQL

Dockerfile creation and container lifecycle

CI/CD setup using GitHub Actions and Cloud Build

IAM roles, service accounts, and permission handling

Managing environment variables securely in production
