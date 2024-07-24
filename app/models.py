from pydantic import BaseModel


class LoginSchema(BaseModel):
    email: str
    password: str

    class Config:
        schema_extra = {
            "example": {
                "email": "test@mail.com",
                "password": "Test123"
            }
        }
