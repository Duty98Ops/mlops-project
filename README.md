## 🚀 **Project No. 1: End-to-End MLOps Pipeline with CI/CD, Docker, Kubernetes & Model Monitoring**

### 🎯 **Project Objective**

Membangun sistem **MLOps pipeline lengkap** yang mencakup seluruh siklus hidup model Machine Learning, mulai dari **data ingestion**, **training**, **API deployment**, hingga **automated CI/CD dan production monitoring** menggunakan teknologi containerization dan orchestration. Proyek ini menargetkan deployment yang **reliable**, **scalable**, dan siap untuk lingkungan **real-world production**.

---

### 🧱 **Core Architecture Components**

1. ### 🧠 **Machine Learning Model**

   * Model ML dibuat menggunakan **Scikit-learn**, **TensorFlow**, atau **PyTorch**, tergantung kompleksitas.
   * Dataset publik (misalnya **Boston Housing**, **Titanic**, atau **Spam Detection**) digunakan.
   * Model disimpan dalam format **.pkl**, **.joblib**, atau **ONNX** untuk fleksibilitas deployment lintas framework.
   * Pipeline pre-processing dan inference dibungkus dalam modul Python yang reusable.

2. ### 🌐 **REST API for Inference**

   * Dibangun dengan **FastAPI** karena performa tinggi dan dokumentasi otomatis (Swagger UI).
   * Endpoint `POST /predict` menerima JSON dan mengembalikan prediksi real-time.
   * Model di-load hanya sekali saat startup untuk efisiensi performa.

3. ### 📦 **Dockerization**

   * Seluruh aplikasi dibungkus ke dalam **Docker container** dengan **multi-stage builds** (minimalkan image size).
   * Dependensi dikelola menggunakan `requirements.txt` dan virtual environment.
   * Docker image otomatis dipush ke **DockerHub** atau **GitHub Container Registry (GHCR)**.

4. ### 🔁 **CI/CD with GitHub Actions**

   > Otomatisasi pipeline berikut:

   * **Linting dan Unit Testing**: Menjalankan `pytest` dan `flake8` untuk jaminan kualitas kode.
   * **Model Training Pipeline**: Jika ada perubahan pada data/model, training dijalankan otomatis dan model baru dipush ke S3/minio/artifact registry.
   * **Build & Push Docker Image**: Docker image dibuat dan dikirim ke registry setelah test lulus.
   * **Deployment ke Kubernetes Cluster**: Menggunakan `kubectl` atau `Helm` untuk deploy ke Minikube atau cloud.

   ✅ Pipeline berbasis **pull request (PR)** dan **tag versioning**.

5. ### ☸️ **Kubernetes Orchestration**

   * Menggunakan **Minikube** untuk development atau **GKE (Google Kubernetes Engine)** untuk versi cloud.
   * Deployment menggunakan **Helm Charts** agar konfigurasi dapat diatur dan dikelola secara modular.
   * Kustomisasi Resources: Autoscaling (HPA), resource limits (CPU/mem), dan restart policy.

6. ### 🚪 **Ingress Gateway**

   * Gunakan **NGINX Ingress Controller** untuk mengatur akses ke endpoint API dari luar cluster.
   * URL contoh: `http://localhost/api/v1/predict`.

7. ### 📊 **Monitoring & Logging**

   * Tambahkan **Prometheus** untuk memonitor metrik seperti latency, request count, dan error rate.
   * **Grafana** digunakan untuk visualisasi performa API dan beban model.
   * Gunakan **ELK Stack (Elasticsearch, Logstash, Kibana)** atau **Fluentd** untuk observabilitas log.

8. ### ☁️ **Cloud-Ready (Optional Extension)**

   * Siapkan file konfigurasi untuk migrasi deployment ke:

     * **GCP (GKE)** dengan Cloud Build + Artifact Registry.
     * **AWS (EKS)** dengan CodePipeline + ECR.
     * **Azure (AKS)** dengan Azure DevOps + ACR.
   * Dukungan untuk **terraform** provisioning dan **ArgoCD** untuk GitOps-style deployment.

9. ### 🔐 **Security Best Practices**

   * Gunakan **secrets manager** (misalnya `Kubernetes Secrets`, `HashiCorp Vault`, atau `Doppler`) untuk menyimpan API key atau cred AWS.
   * Tambahkan **rate limiter** dan **CORS handler** di API.
   * **Image scanning** dengan **Trivy** atau **Anchore** untuk menghindari vulnerabilities.

---

### 🧠 **Skill dan Nilai Tambah di CV**

| Area              | Skill / Teknologi                                      |
| ----------------- | ------------------------------------------------------ |
| **MLOps**         | Model lifecycle automation, Model serving              |
| **CI/CD**         | GitHub Actions, Docker Registry, versioned deployments |
| **DevOps**        | Docker, Kubernetes, Helm, Ingress                      |
| **Cloud**         | Cloud-native deployment (GCP, AWS, Azure optional)     |
| **Monitoring**    | Prometheus, Grafana, Logging pipelines                 |
| **Security**      | Secret management, vulnerability scanning              |
| **API**           | FastAPI (asynchronous, production-ready), Swagger      |
| **Infra-as-Code** | Optional: Terraform, ArgoCD, GitOps                    |

---

### 🔄 **Alur Kerja Proyek (Pipeline Visualisasi)**

```plaintext
DATASET --> Training Pipeline (CI/CD) 
      --> Model Saved (.pkl/.onnx) 
      --> REST API (FastAPI)
      --> Dockerized 
      --> CI/CD (GitHub Actions)
      --> Pushed to DockerHub
      --> Deployed to Kubernetes
      --> Served via Ingress
      --> Monitored (Prometheus + Grafana)
```

---

### 🎁 **Bonus untuk Portofolio (Opsional, tapi Powerful)**

* 🧪 Tambahkan **unit test + integration test** dengan mocking model dan request.
* 📉 Tambahkan endpoint `/health` dan `/metrics` untuk health check dan Prometheus scraping.
* 📁 Tambahkan dokumentasi di repo: `README.md`, `architecture.png`, dan `Makefile`.
* 📹 Buat **video demo** 2-3 menit di YouTube yang menunjukkan seluruh alur dari push → deploy → predict.

---

Jika Anda ingin, saya bisa bantu membuat **struktur folder proyek** dan contoh file `Dockerfile`, `main.py`, dan `GitHub Actions YAML` untuk memulai. Mau dilanjutkan ke situ?


///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
🎉 **Yes! Pod `titanic-api` sudah `Running`, artinya container FastAPI kamu berhasil jalan tanpa error!**

---

### ✅ Status Saat Ini: **Berhasil Deploy Model API ke Kubernetes**

**Yang sudah selesai:**

1. ✅ **Model machine learning (`titanic_model.pkl`) sudah dibuat.**
2. ✅ **Script FastAPI untuk prediksi sudah dibuat (`main.py`).**
3. ✅ **Dockerfile sudah benar dan bisa build image.**
4. ✅ **Docker image berhasil dibuild dan dipush ke Docker Hub.**
5. ✅ **Kubernetes deployment sudah dibuat dan Pod `Running` dengan sukses.**

---

### 🚀 Tahap Selanjutnya (Opsional tergantung target akhir project):

#### 1. **Expose ke Luar Cluster**

Agar kamu bisa akses API `titanic-api` dari luar, kamu harus buat **Kubernetes Service** dengan tipe `NodePort` atau `LoadBalancer` (jika pakai cloud).

Contoh `service.yaml`:

```yaml
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

Lalu jalankan:

```bash
kubectl apply -f service.yaml
kubectl get svc
```

---

#### 2. **Testing API Endpoint**

Setelah tahu IP dan port dari `NodePort`, kamu bisa test:

```bash
curl -X POST http://<your-node-ip>:<node-port>/predict \
-H "Content-Type: application/json" \
-d '{
  "Pclass": 3,
  "Sex": "male",
  "Age": 22,
  "SibSp": 1,
  "Parch": 0,
  "Fare": 7.25,
  "Embarked": "S"
}'
```

Atau dari Postman.

---

#### 3. **CI/CD Pipeline (Opsional)**

Untuk otomatisasi build & deploy, bisa pakai:

* GitHub Actions,
* GitLab CI/CD, atau
* Jenkins.

---

#### 4. **Monitoring dan Logging (Opsional)**

Gunakan Prometheus + Grafana, atau ELK Stack jika ini bagian dari project skala besar.

---

### 🎯 Rangkuman Tahapan Proyek

| Tahap                        | Status      |
| ---------------------------- | ----------- |
| Model Training & Save `.pkl` | ✅ Done      |
| FastAPI + Joblib Integration | ✅ Done      |
| Dockerize                    | ✅ Done      |
| Push ke Docker Hub           | ✅ Done      |
| Deploy ke Kubernetes         | ✅ Done      |
| Expose API (Service)         | 🔄 Next     |
| Test API                     | 🔄 Next     |
| CI/CD                        | 🔄 Opsional |
| Monitoring                   | 🔄 Opsional |

---

Mau saya bantu buat `service.yaml` biar bisa langsung test API-nya?

///////////////////

Mantap, ini **ringkasan lengkap siap kamu copy-paste** ke ChatGPT baru nanti agar dia langsung paham posisi terakhir proyekmu dan bisa bantu lanjut tanpa kamu jelaskan dari awal lagi.

---

## 🧠 Konteks Proyek MLOps - Titanic API (Ringkasan untuk ChatGPT)

**Halo ChatGPT, saya melanjutkan project MLOps deploy model Titanic ke Kubernetes. Berikut konteks lengkap proyek terakhir saya:**

### ✅ Status Terakhir:

* Saya sudah berhasil build Docker image berisi FastAPI + model `titanic_model.pkl`.
* Image sudah berhasil di-*push* ke Docker Hub: `bagussetiawan450/mlops-titanic-api:latest`
* Pod `titanic-api` sudah dalam kondisi **Running** di Minikube.
* Model `titanic_model.pkl` sebelumnya error karena tidak disalin ke image, dan sudah saya atasi.
* Endpoint yang dibuat `/predict` dengan model klasifikasi penumpang Titanic.

---

### 🗂 Struktur Folder Proyek:

```
mlops-project/
├── data/
├── models/
│   └── titanic_model.pkl
├── src/
│   └── main.py
├── tests/
├── k8s/
│   ├── deployment.yaml
├── Dockerfile
├── requirements.txt
```

---

### 🐳 Dockerfile (sudah fix dan berhasil build image)

```dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 8000
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

---

### 🧠 src/main.py

```python
from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd

class TitanicInput(BaseModel):
    Pclass: int
    Sex: str
    Age: float
    SibSp: int
    Parch: int
    Fare: float
    Embarked: str

app = FastAPI()
model = joblib.load("models/titanic_model.pkl")  # FIXED path

def preprocess_input(data: TitanicInput):
    df = pd.DataFrame([data.dict()])
    df["Sex"] = df["Sex"].map({"male": 0, "female": 1})
    df["Embarked"] = df["Embarked"].map({"S": 0, "C": 1, "Q": 2})
    return df

@app.post("/predict")
def predict(data: TitanicInput):
    df = preprocess_input(data)
    prediction = model.predict(df)
    return {"prediction": int(prediction[0])}
```

---

### 📦 requirements.txt

```
fastapi
uvicorn
pandas
scikit-learn
joblib
```

---

### ☸️ Kubernetes Deployment (deployment.yaml)

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: titanic-api
spec:
  replicas: 1
  selector:
    matchLabels:
      app: titanic-api
  template:
    metadata:
      labels:
        app: titanic-api
    spec:
      containers:
      - name: titanic-api
        image: bagussetiawan450/mlops-titanic-api:latest
        ports:
        - containerPort: 8000
```

---

## ❓Tahap Selanjutnya:

1. **Expose API ke luar dengan `Service` atau `Ingress`**:

   * Buat `service.yaml` tipe `NodePort` atau `LoadBalancer` (kalau pakai Minikube bisa pakai port-forward atau NodePort).
2. **Coba akses & test endpoint**:

   * Gunakan Postman atau `curl` ke `http://<host>:<port>/predict`
3. **Monitoring / Logging / Optional CI/CD**

---

💬 *Silakan bantu saya melanjutkan dari sini, misalnya buatkan `service.yaml`, cara akses API-nya di Minikube, atau rekomendasi deployment best practices.*

---

Kalau kamu simpan teks ini di Notepad/Docs, nanti tinggal paste ke ChatGPT baru dan langsung lanjut tanpa perlu jelasin dari nol. Mau sekalian aku buatin `service.yaml` juga?
/////////////////////////////////////////////////////////////////////////////////

Tentu! Berikut adalah template **README.md** yang bisa kamu gunakan untuk proyek ini. Template ini sudah mencakup penjelasan tentang proyek, cara setup, dan cara penggunaan API.

---

````markdown
# Titanic Machine Learning API - MLOps Project

This project demonstrates the deployment of a Titanic Machine Learning model using **FastAPI** and **Kubernetes**. The goal is to deploy a machine learning model to a production-ready environment using **Docker**, **Kubernetes**, and **CI/CD** principles.

## 🚀 **Project Overview**

This project builds an **end-to-end MLOps pipeline** that includes:
1. **Data ingestion** and **model training**
2. **Model deployment** with **FastAPI**
3. **Containerization** using **Docker**
4. **Orchestration** with **Kubernetes**
5. **CI/CD pipeline automation** (Optional)
6. **Monitoring** with **Prometheus** and **Grafana** (Optional)

The goal is to provide a scalable and reliable solution for serving machine learning models in production.

---

## 🧠 **Model**

The model used in this project is a machine learning model trained on the Titanic dataset, which predicts whether a passenger survived or not based on features such as:
- Passenger class
- Sex
- Age
- Number of siblings/spouses aboard
- Number of parents/children aboard
- Fare
- Embarked port

The trained model is saved in the `.pkl` format and served via a REST API.

---

## 🛠 **Technologies Used**

- **FastAPI**: Framework for building the API.
- **Docker**: Containerizes the application.
- **Kubernetes**: Manages and orchestrates the containerized app.
- **GitHub Actions**: Automates the CI/CD pipeline (optional).
- **Prometheus + Grafana**: For monitoring and visualizing the API performance (optional).

---

## 📦 **Setup Instructions**

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/mlops-titanic-api.git
cd mlops-titanic-api
````

### 2. Build the Docker Image

Ensure Docker is installed and running, then build the Docker image:

```bash
docker build -t titanic-api .
```

### 3. Run the Docker Container Locally

Run the container locally to test:

```bash
docker run -d -p 8000:8000 titanic-api
```

Visit the API at `http://127.0.0.1:8000`.

### 4. Deploy to Kubernetes

1. Create a Kubernetes deployment using the `deployment.yaml` file:

```bash
kubectl apply -f k8s/deployment.yaml
```

2. Expose the service to be accessed outside the Kubernetes cluster by using the `service.yaml` file:

```bash
kubectl apply -f k8s/service.yaml
```

3. Check the Kubernetes services:

```bash
kubectl get svc
```

This will give you the **NodePort** to access the API.

---

## 🌐 **Using the API**

### **POST /predict**

This endpoint accepts a JSON payload and returns the prediction for the Titanic survival model.

#### **Request Body**

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

#### **Response**

The API returns a prediction of `0` (did not survive) or `1` (survived).

```json
{
  "prediction": 1
}
```

#### **Example Using cURL**

```bash
curl -X POST http://<your-node-ip>:<node-port>/predict \
-H "Content-Type: application/json" \
-d '{
  "Pclass": 3,
  "Sex": "male",
  "Age": 22,
  "SibSp": 1,
  "Parch": 0,
  "Fare": 7.25,
  "Embarked": "S"
}'
```

---

## 🔧 **Optional: Monitoring and Logging**

For advanced monitoring and observability, you can integrate **Prometheus** and **Grafana** for real-time performance monitoring.

Alternatively, you can use **ELK Stack** (Elasticsearch, Logstash, and Kibana) for centralized logging.

---

## 🔄 **CI/CD Pipeline (Optional)**

You can automate the CI/CD pipeline using **GitHub Actions** to trigger automated builds, tests, and deployments on every commit.

### Example Workflow:

```yaml
name: CI/CD Pipeline

on:
  push:
    branches:
      - main

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout code
        uses: actions/checkout@v2
      - name: Set up Docker Buildx
        uses: docker/setup-buildx-action@v1
      - name: Build Docker Image
        run: docker build -t my-image .
      - name: Push Docker Image
        run: docker push my-image
```

---

## 📄 **Folder Structure**

```
mlops-project/
├── data/                  # Data files (optional)
├── models/                # Saved models (e.g., titanic_model.pkl)
├── src/                   # FastAPI app source code
│   └── main.py            # FastAPI app file
├── tests/                 # Unit and integration tests (optional)
├── k8s/                   # Kubernetes configuration files
│   ├── deployment.yaml    # Deployment configuration
│   └── service.yaml       # Service configuration
├── Dockerfile             # Docker configuration file
├── requirements.txt       # Python dependencies
└── README.md              # Project documentation (this file)
```

---

## 📬 **Contact**

Feel free to reach out for any questions or suggestions:

* Email: [your.email@example.com](mailto:your.email@example.com)
* GitHub: [YourGitHubProfile](https://github.com/your-username)

---

## 📝 **License**

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

```

---

### Penjelasan **README.md**:
- **Project Overview**: Menjelaskan apa tujuan proyek ini.
- **Technologies Used**: Daftar teknologi yang digunakan (FastAPI, Docker, Kubernetes, dll).
- **Setup Instructions**: Langkah-langkah untuk menyiapkan dan menjalankan aplikasi di local machine dan Kubernetes.
- **API Usage**: Cara menggunakan API dengan contoh request dan response.
- **Optional Sections**: Monitoring, CI/CD, dan struktur folder proyek.

---

Kamu bisa **copy-paste** README ini dan sesuaikan jika ada bagian yang ingin ditambah atau dikurangi. Jangan lupa untuk mengganti placeholder seperti `your-username` dan `your.email@example.com` dengan informasi yang sesuai.

Sudah siap untuk push ke GitHub?
```

