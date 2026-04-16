import json
from pathlib import Path
import requests
import mlflow

mlflow.set_tracking_uri("http://127.0.0.1:5000")
mlflow.set_experiment("tiny-slmops-demo-eval")

samples = json.loads(Path("data/eval_samples.json").read_text(encoding="utf-8"))

passed = 0

with mlflow.start_run():
    for i, sample in enumerate(samples):
        response = requests.post(
            "http://127.0.0.1:8000/summarize",
            json={"text": sample["text"], "model": "gemma3", "prompt_version": "v1"},
            timeout=120
        )
        response.raise_for_status()
        summary = response.json()["summary"]

        ok = len(summary) > 20
        passed += int(ok)

        mlflow.log_metric(f"sample_{i}_pass", int(ok))
        mlflow.log_metric(f"sample_{i}_summary_chars", len(summary))

    mlflow.log_metric("pass_rate", passed / len(samples))

print("Evaluation done.")