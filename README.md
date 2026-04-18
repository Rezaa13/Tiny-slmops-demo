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


**   Screenshots: 

1. 
<img width="1920" height="2128" alt="1" src="https://github.com/user-attachments/assets/e04d0ecb-4472-48d9-a6dd-ede8025ba823" />

2. 
<img width="1920" height="3162" alt="2" src="https://github.com/user-attachments/assets/c933b545-572f-4403-9feb-4691ef16eb22" />

3. 
<img width="1920" height="912" alt="3" src="https://github.com/user-attachments/assets/77389fb2-da5c-4635-96f5-f26964e40f0f" />
