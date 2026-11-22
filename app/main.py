from fastapi import FastAPI
import socket

app = FastAPI()

@app.get("/health")
def health_check():
    return{
        "status" : "ok",
        "host" : socket.gethostname()
    }

@app.get("/predict")
def predict(text: str = "hello"):
    return{
        "input" : text,
        "prediction" : f"AI_processed_{text.upper()}"
    }