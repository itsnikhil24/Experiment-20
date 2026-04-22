# Experiment 20: Implement CI/CD Pipeline for Application Deployment

This project demonstrates:
- A simple Flask backend
- Docker image creation and container execution
- A GitHub Actions workflow that builds and verifies the Dockerized backend

## Folder Structure

```
experiment-20-ci-cd/
├── app.py
├── requirements.txt
├── Dockerfile
├── .dockerignore
└── .github/
    └── workflows/
        └── ci-cd.yml
```

## Local Setup

### 1) Clone or copy the project
Put all files in one folder.

### 2) Install dependencies locally
```bash
pip install -r requirements.txt
```

### 3) Run the Flask app locally
```bash
python app.py
```

Open:
- `http://127.0.0.1:5000/`
- `http://127.0.0.1:5000/health`

## Docker Commands

### Build Docker image
```bash
docker build -t flask-backend .
```

### Check images
```bash
docker images
```

### Run container
```bash
docker run -d -p 5005:5000 --name backend-container flask-backend
```

### Check running container
```bash
docker ps
```

### Stop container
```bash
docker stop backend-container
```

### Remove container
```bash
docker rm backend-container
```

## GitHub Actions Workflow

The workflow file is located at:
`.github/workflows/ci-cd.yml`

It automatically runs on:
- push to `main`
- pull request to `main`

Workflow steps:
1. Checkout code
2. Set up Python
3. Install dependencies
4. Import-check the Flask app
5. Build Docker image
6. Run Docker container
7. Verify `/health`
8. Stop container

## How to Submit the Experiment

1. Create a GitHub repository.
2. Push this code to the repository.
3. Make sure GitHub Actions runs successfully.
4. Take screenshots of:
   - `docker images`
   - `docker ps`
   - `docker run ...`
   - GitHub Actions workflow success page
5. Zip the whole project folder and upload it in the form.

## Sample Screenshot Commands

Use the following commands in terminal:

```bash
docker build -t flask-backend .
docker images
docker run -d -p 5005:5000 --name backend-container flask-backend
docker ps
docker stop backend-container
docker rm backend-container
```

## Notes

- This example uses Flask because your reference commands show `flask-backend`.
- If your Experiment-16 backend has different routes or files, replace `app.py` with your existing backend entry file and keep the same Docker and GitHub Actions setup.
