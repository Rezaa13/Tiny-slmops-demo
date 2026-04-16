# Tiny SLMOps Demo

A small local AI-native system that summarizes text using a local model.

## Stack
- FastAPI
- Ollama
- MLflow
- DVC

## What it shows
- Local small-model inference
- Data versioning with DVC
- Experiment tracking with MLflow
- API-based AI service with FastAPI

## How to run

1. Install Python dependencies:
   pip install -r requirements.txt

2. Start Ollama:
   ollama run gemma3

3. Start MLflow:
   mlflow server --host 127.0.0.1 --port 5000

4. Start the API:
   uvicorn app.main:app --reload

5. Open:
   http://127.0.0.1:8000/docs
