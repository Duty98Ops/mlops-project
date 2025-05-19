# 🚀 End-to-End MLOps Pipeline: Titanic ML API with CI/CD, Docker, Kubernetes & Monitoring

> **Production-ready machine learning API** using Docker, Kubernetes, GitHub Actions, and FastAPI.

---

## 🎯 Project Objective

Membangun sistem **end-to-end MLOps pipeline** yang mencakup:

* Data ingestion dan model training
* API deployment untuk inference
* CI/CD automation untuk training dan deploy
* Containerization dengan Docker
* Orkestrasi dengan Kubernetes (Minikube/GKE)
* Monitoring dan logging (Prometheus, Grafana, ELK Stack)

---

## 🧠 Machine Learning Model

* Model klasifikasi penumpang Titanic (survive atau tidak).
* Fitur: `Pclass`, `Sex`, `Age`, `SibSp`, `Parch`, `Fare`, `Embarked`.
* Dibuat dengan `scikit-learn` dan disimpan sebagai `titanic_model.pkl`.

---

## 🌐 FastAPI: REST API for Model Inference

* Endpoint `POST /predict` menerima data JSON.
* Response: hasil prediksi (`0` = tidak selamat, `1` = selamat).
* Dokumentasi otomatis via **Swagger UI**.

---

## 📦 Dockerized Deployment

* Aplikasi dibungkus dalam Docker image menggunakan `python:3.9-slim`.
* Multi-stage build untuk image yang ringan.
* Image di-push ke Docker Hub:
  `bagussetiawan450/mlops-titanic-api:latest`

### 🔧 Docker Commands

```bash
docker build -t titanic-api .
docker run -d -p 8000:8000 titanic-api
```

---

## ☸️ Kubernetes Orchestration

* Deployment menggunakan file `deployment.yaml`.
* Dapat dijalankan di **Minikube** (dev) atau **GKE** (cloud).

### ✅ Deployment Command

```bash
kubectl apply -f k8s/deployment.yaml
```

---

## 🔌 Expose API with Kubernetes Service

Gunakan `NodePort` untuk mengakses API dari luar cluster:

```yaml
# k8s/service.yaml
apiVersion: v1
kind: Service
metadata:
  name: titanic-api-service
spec:
  selector:
    app: titanic-api
  ports:
    - protocol: TCP
      port: 80
      targetPort: 8000
  type: NodePort
```

### Apply & Get Service Info

```bash
kubectl apply -f k8s/service.yaml
kubectl get svc
```

---

## 🔍 API Usage

### ✅ Endpoint

`POST /predict`

### 🧾 Example Request

```json
{
  "Pclass": 3,
  "Sex": "male",
  "Age": 22,
  "SibSp": 1,
  "Parch": 0,
  "Fare": 7.25,
  "Embarked": "S"
}
```

### 🔁 Response

```json
{
  "prediction": 1
}
```

### 🧪 Test via Curl

```bash
curl -X POST http://<node-ip>:<port>/predict \
-H "Content-Type: application/json" \
-d '{"Pclass":3,"Sex":"male","Age":22,"SibSp":1,"Parch":0,"Fare":7.25,"Embarked":"S"}'
```

---

## 🔄 CI/CD Pipeline with GitHub Actions *(Optional but Recommended)*

### 🔁 Features:

* Auto run tests and lint (`pytest`, `flake8`)
* Auto build & push Docker image
* Auto deploy to Kubernetes using `kubectl` or Helm

### 🚧 Sample Workflow (`.github/workflows/main.yml`)

```yaml
name: CI/CD Pipeline

on:
  push:
    branches:
      - main

jobs:
  build-and-deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Build Docker Image
        run: docker build -t bagussetiawan450/mlops-titanic-api:latest .
      - name: Push to Docker Hub
        run: docker push bagussetiawan450/mlops-titanic-api:latest
```

---

## 📊 Monitoring (Optional)

* **Prometheus**: Collect metrics like request count, latency, error rate.
* **Grafana**: Visualize performance.
* **ELK Stack** (Elasticsearch + Kibana): Log observability.

---

## 🔐 Security Best Practices

* API keys disimpan menggunakan `Kubernetes Secrets` atau `Vault`.
* Tambahkan CORS dan rate-limiting di FastAPI.
* Docker image discan dengan **Trivy** untuk cek kerentanan.

---

## 📁 Project Structure

```
mlops-project/
├── data/                  # Dataset (optional)
├── models/                # Model (.pkl)
│   └── titanic_model.pkl
├── src/
│   └── main.py            # FastAPI App
├── tests/                 # (Optional) Unit & Integration Tests
├── k8s/                   # K8s Configs
│   ├── deployment.yaml
│   └── service.yaml
├── Dockerfile
├── requirements.txt
└── README.md
```

## 🧭 Project Pipeline Flow

```plaintext
Dataset → Model Training (.pkl)
       → FastAPI REST API
       → Dockerized Image
       → Pushed to DockerHub
       → Kubernetes Deployment
       → Exposed via NodePort/Ingress
       → Monitoring & Logging
```


