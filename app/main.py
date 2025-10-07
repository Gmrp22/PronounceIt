import os
from dotenv import load_dotenv
from fastapi import FastAPI, UploadFile, Form
from fastapi.responses import JSONResponse
from vosk import Model, KaldiRecognizer
import wave
import json

# Cargar variables de entorno
load_dotenv()
MODEL_PATH = os.environ.get("MODEL_PATH", "/app/models")

# Inicializar modelo
if not os.path.exists(MODEL_PATH):
    raise FileNotFoundError(f"Model not found in {MODEL_PATH}")
model = Model(MODEL_PATH)

app = FastAPI(title="Vosk Inference API")

@app.get("/test-model")
def test_model():
    recognizer = KaldiRecognizer(model, 16000)
    # Simula datos vacíos
    data = b"\0" * 4000
    recognizer.AcceptWaveform(data)
    result = recognizer.FinalResult()
    return {"resultado": result}