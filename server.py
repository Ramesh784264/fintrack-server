from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="FinTrack API")

class User(BaseModel):
    name: str
    age: int
    email: str

@app.get("/")
def home():
    return {"message": "Welcome to FinTrack API"}

@app.get("/health")
def health():
    return {"status": "healthy"}

@app.post("/user")
def create_user(user: User): 
    user_data = user.model_dump()
    return {
        "message": "User created successfully",
        "user": user_data
    }