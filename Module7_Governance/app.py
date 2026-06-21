from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="AI Governance Layer - Module 7")

class InputText(BaseModel):
    text: str

def safety_check(text: str):
    blocked_words = ["hate", "violence", "abuse"]
    for word in blocked_words:
        if word in text.lower():
            return False
    return True

@app.post("/predict")
def predict(data: InputText):
    if not safety_check(data.text):
        return {
            "status": "blocked",
            "message": "Input violates safety policy"
        }

    # Dummy sentiment output (replace with ONNX model later if needed)
    return {
        "status": "ok",
        "input": data.text,
        "prediction": "positive"
    }