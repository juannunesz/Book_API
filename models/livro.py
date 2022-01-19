from typing import List

from pydantic import BaseModel, Field

class Texto(BaseModel):
    conteudo: str = Field(...)

class Ilustracao(BaseModel):
    url_img: str

class LivroModel(BaseModel):
    titulo: str = Field(...)
    autor: str = Field(...)
    professor: str = Field(...)
    texto: List[Texto]
    ilustracao: List[Ilustracao]

    class Config:
        schema_extra = {
            "example": {
                "titulo": "O Guia do Mochileiro Das Galáxias",
                "autor": "Douglas Adams",
                "professor": "Thomas Tidholm",
                "texto": [
                    {
                        "conteudo": "conteudo"
                    }
                ],
                "ilustracao": [
                    {
                        "url_img": "imagem"
                    }
                ]
            }
        }

def ResponseModel(data, message):
    return {
        "data": data,
        "code": 200,
        "message": message,
    }

def ErrorResponseModel(error, code, message):
    return {
        "error": error,
        "code": code,
        "message": message
    }
