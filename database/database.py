import motor.motor_asyncio
from decouple import config
from aws.handler_s3 import delete_folder_s3

from .database_helper import livro_helper, admin_helper

MONGO_DETAILS = config('MONGO_DETAILS')

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)

database = client.livros

livros_collection = database.get_collection('livros_collection')
admin_collection = database.get_collection('admins')

#CRIA UM NOVO ADMIN PARA AUTH
async def add_admin(admin_data: dict) -> dict:
    admin = await admin_collection.insert_one(admin_data)
    new_admin = await admin_collection.find_one({"_id": admin.inserted_id})
    return admin_helper(new_admin)

#BUSCA TODOS OS LIVROS DA COLEÇÃO
async def buscar_livros():
    livros = []
    async for livro in livros_collection.find():
        livros.append(livro_helper(livro))
    return livros

#ADICIONA UM NOVO LIVRO
async def adicionar_livro(livro_data: dict) -> dict:
    livro = await livros_collection.insert_one(livro_data)
    novo_livro = await livros_collection.find_one({"_id": livro.inserted_id})
    return livro_helper(novo_livro)

#BUSCA LIVROS POR ID
async def buscar_livro_id(id: str) -> dict:
    livro = await livros_collection.find_one({"id": id})
    if livro:
        return livro_helper(livro)

#DELETA LIVRO POR ID
async def deletar_livro(id: str):
    livro = await livros_collection.find_one({"id": id})
    if livro:
        await livros_collection.delete_one({"id": id})
        delete_folder_s3(id)
        return True