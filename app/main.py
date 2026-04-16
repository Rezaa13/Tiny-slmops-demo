import time
import mlflow
from fastapi import FastAPI
from pydantic import BaseModel

from app.llm import summarize_text

mlflow.set_tracking_uri("http://127.0.0.1:5000")
mlflow.set_experiment("tiny-slmops-demo")

app = FastAPI(title="Tiny SLMOps Demo")

class SummarizeRequest(BaseModel):
    text: str
    model: str = "gemma3"
    prompt_version: str = "v1"

@app.get("/")
def root():
    return {"message": "Tiny SLMOps demo is running"}

@app.post("/summarize")
def summarize(req: SummarizeRequest):
    start = time.time()
    summary = summarize_text(req.text, req.model)
    latency = time.time() - start

    with mlflow.start_run():
        mlflow.log_param("model", req.model)
        mlflow.log_param("prompt_version", req.prompt_version)
        mlflow.log_param("input_chars", len(req.text))
        mlflow.log_metric("latency_seconds", latency)
        mlflow.log_metric("summary_chars", len(summary))

    return {
        "summary": summary,
        "latency_seconds": round(latency, 3)
    }