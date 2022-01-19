from fastapi import APIRouter, File, UploadFile, Form
from fastapi.encoders import jsonable_encoder
from utils.requests_handler import request_helper
from typing import Text, List
from database.database import *
from models.livro import *

router = APIRouter()


@router.post("/", response_description="Livro adicionado")
async def add_livro(titulo:str = Form(...), autor: str = Form(...), professor: str = Form(...),textos: List[Text] = Form(...) ,ilustracoes: List[UploadFile] = File(...)):
    livro = request_helper(titulo,autor, professor, textos, ilustracoes)
    livro_encod = jsonable_encoder(livro)
    novo_livro = await adicionar_livro(livro_encod)
    return ResponseModel(novo_livro, "Livro Adicionado com sucesso!")


@router.get("/", response_description="Livros retornados")
async def get_livros():
    livros = await buscar_livros()
    return ResponseModel(livros, "Livros retornados com sucesso!") \
        if len(livros) > 0 \
        else ResponseModel(
        livros, "Lista de livros está vazia")


@router.get("/{id}", response_description="Retorno dos dados")
async def get_livro_data(id):
    livro = await buscar_livro_id(id)
    return ResponseModel(livro, "Dados do livro retornou com sucesso!") \
        if livro \
        else ErrorResponseModel("Ocorreu um erro.", 404, "Livro não existe.")


@router.delete("/{id}", response_description="Livro Deletado")
async def delete_livro_data(id: str):
    livro_deletado = await deletar_livro(id)
    return ResponseModel("Livro com id: {} removido".format(id), "Livro Deletado com sucesso") \
        if livro_deletado \
        else ErrorResponseModel("Ocorreu um erro", 404, "Livro com id {0} não existe".format(id))
