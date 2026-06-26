from fastapi import FastAPI
from pydantic import BaseModel, EmailStr, field_validator, Field

app = FastAPI(title="FastAPI")

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
def create_user(name, age, email): 
    # user_data = user.model_dump()
    return {
        "message": "User created successfully",
        "user":{
            "name": name,
            "age": age,
            "email": email
            }
    }
    
class UserRegister(BaseModel):
    name: str 
    email: EmailStr 
    password: str 
    mobile: str 
    
    model_config = {
        "json_schema_extra": {
            "example": {
                "name": "Ramesh",
                "email": "ramesh@gmail.com",
                "password": "Password123",
                "mobile": "9876543210"
            }
        }
    }

    @field_validator("name")
    @classmethod
    def validate_name(cls, value):
        if len(value) < 3:
           raise ValueError("Name must be at least 3 characters long")
        if not value[0].isalpha():
           raise ValueError("Name must start with a letter")
        return value

    @field_validator("password")
    @classmethod
    def validate_password(cls, value):
        if len(value) < 8 or len(value) > 16:
           raise ValueError("Password must be between 8 and 16 characters")
        return value
    @field_validator("mobile")
    @classmethod
    def validate_mobile(cls, value):
        if not value.isdigit():
           raise ValueError("Mobile number must be numeric")
        if len(value) != 10:
           raise ValueError("Mobile number must be 10 digits")
        if value[0] not in "6789":
            raise ValueError("Mobile number must start with 6, 7, 8, or 9")
        return value
    
@app.post("/register")
def register(user: UserRegister):
    return{
        "message":"User registered successfully",
        "user":user.model_dump(exclude={"password"})
    }          