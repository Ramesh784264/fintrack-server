from fastapi import FastAPI

app = FastAPI(title="FinTrack API")

@app.get("/")
def home():
    return {"message": "Welcome to FinTrack API"}

@app.get("/health")
def health():
    return {"status": "healthy"}