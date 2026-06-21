from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Sentiment API Running"}

@app.post("/predict")
def predict(text: str):
    return {
        "text": text,
        "sentiment": "positive"
    }