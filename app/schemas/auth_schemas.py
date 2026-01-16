from pydantic import BaseModel, EmailStr, Field

class RegisterRequest(BaseModel):
    username: str
    email: EmailStr
    password: str

class LoginRequest(BaseModel):
    username: str
    password: str

class RegisterResponse(BaseModel):
    message: str = Field(default="User registered successfully")

class TokenResponse(BaseModel):
    access_token: str
    token_type: str = Field(default="bearer")
