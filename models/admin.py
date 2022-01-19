from pydantic import BaseModel, Field, EmailStr

class AdminModel(BaseModel):
    fullname: str = Field(...)
    email: EmailStr = Field(...)
    password: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "fullname": "juan de oliveira Nunes",
                "email": "juannunes@admin.com",
                "password": "suasenhavaiaqui"
            }
        }