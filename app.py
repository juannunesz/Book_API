from fastapi import FastAPI, Depends

from auth.jwt_bearer import JWTBearer
from routes.livro import router as LivroRouter
from routes.admin import router as AdminRouter

description = """
Esta API é responsavel por criar livros contendo  Titulo, Autor, Professor, Textos e Imagens

## Recursos
* **Administrador / Auth**: Responsável por criar um user e posteriormente criar um token de autenticação para o uso da API.
* **Livros**: Responsável por conter informações de leitura, modificação e remoção de livros, 


### Administrador / Auth
com essse recurso é possivel?

* Criar um admin user;
* Fazer login e Pegar o Token JWT para autenticação de rotas;

### Livros
com essse recurso é possivel?

* Listar todos os Livros Criados;
* Listar informações detalhadas de um Livro por seu ID;
* Criar um livro enviando Textos e imagens;
* Apagar um Livro por seu ID.

"""

app = FastAPI(
    title='Books API',
    description=description,
    version='0.1.0',
    contact={
        "name": "Juan",
        "email": "juannunesdev@gmail.com"
    }
)

token_listener = JWTBearer()

@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Aplication is running..."}


app.include_router(AdminRouter, tags=["Admin / Auth"], prefix="/admin")
app.include_router(LivroRouter, tags=["Books"], prefix="/book", dependencies=[Depends(token_listener)])
