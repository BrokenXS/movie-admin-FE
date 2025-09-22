# Movie Admin Backend Deployment (Kubernetes)

This project provides a FastAPI backend, PostgreSQL database, and pgAdmin UI, all deployable on Kubernetes (kind).

## Prerequisites
- Docker
- kind (Kubernetes in Docker)
- kubectl

## Setup Steps

### 1. Build and Push Backend Image
Build your backend Docker image and push it to a registry accessible by your cluster (e.g., Docker Hub).

```
docker build -t <your-dockerhub-username>/movie-admin-be:latest .
docker push <your-dockerhub-username>/movie-admin-be:latest
```

Update `k8s/k8s-backend.yaml` to use your image name.

### 2. Create kind Cluster
```
kind create cluster --name movie-admin
```

### 3. Deploy Database and pgAdmin
```
kubectl apply -f k8s/k8s-postgres-pgadmin.yaml
```

### 4. Deploy Backend
```
kubectl apply -f k8s/k8s-backend.yaml
```

### 5. Access Services
- **pgAdmin:** http://localhost:30500 (login: admin@admin.com / admin123)
- **Backend API:** http://localhost:30080

### 6. Connect Backend to Database
The backend connects to PostgreSQL using the internal service name:
```
DATABASE_URL=postgresql://admin:admin123@postgres:5432/movies_db
```

## Useful Commands
- List pods:
  ```kubectl get pods -n movie-admin```
- List services:
  ```kubectl get services -n movie-admin```
- View logs:
  ```kubectl logs <pod-name> -n movie-admin```

## Notes
- Persistent data is stored in a PVC (`postgres-pvc`).
- Resource requests/limits are set for production safety.
- Update image names and environment variables as needed for your setup.

---
For more details, see the manifests in the `k8s/` folder.
