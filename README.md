# Book API

Desenvolvimento de uma API Mágica em Python + FastAPI + MongoDB + JWT que é capaz de criar livros com textos e imagens.

## Recursos Utilizados no Desenvolvimento da Aplicação:

- Python ~ 3.8.0;
- Pipenv ~ 11.9.0;
- FastAPI;
- MongoDB;
- PyJWT (Para criação do token);
- pymongo & motor; 
- bcrypt (Para encriptar a senha do user Admin)
- Docker & Docker Compose;
- Conceito Web & HTTP Protocol;
- Pydantic;
- uvicorn;
- boto3
- IDE: Visual Code;
- Insomnia (para testar as API's criadas);

## Features
- Python FastAPI backend.
- MongoDB database.
- Authentication (Extra)
- Upload Bucket S3

## Padrão das Rotas Criadas: 

Procurando seguir o padrão e design das API's, segue abaixo as URI's das rotas desenvolvidas:

 ROTA                      |     HTTP(Verbo)   |      Descrição        | 
-------------------------  | ----------------- | --------------------- | 
/admin/                  |       POST         | Cria um user ADMIN      |
/admin/login                  |       POST         |  Autenticação    |  
/book/                  |       GET         | Selecionar Todos      | 
/book/                  |       POST        | Criar                 | 
/book/{id}     |       GET         | Selecionar Por Magic_Id     | 
/livro/{id}     |       DELETE      | Excluir Por Magic_id        |


## Aplicação Em Produção:

bom...caso queira testar a aplicação sem instalar o ambiente basta acessar [AQUI]()

esse repositório está configurado para enviar automáticamente as modificações para o servidor.

## Executando a Aplicação:
Para que o projeto execute de maneira satisfatória, há a necessidade de instalar os programas abaixo:

1) Instalar: Python [AQUI](https://www.python.org/downloads/)
  - Video explicando como instalar Python [AQUI](https://www.youtube.com/watch?v=YdNiifNwt_M)

2) Instalar Docker [AQUI](https://docs.docker.com/engine/install/#server)

 - Documentação do docker explicando como instalar.

3) Instalar Docker Compose [AQUI](https://docs.docker.com/compose/install/)

 - Documentação de como installar Docker Compose.

4) Instalar Pipenv

    - Optei pelo pipenv por questão de costume e por ele  criar para nós um vitualev de forma mais dinâmica.
    - Para quem já trabalhou com javascript ele se assemelha ao npm

Deverá abrir o seu terminal e digitar o seguinte comando abaixo:

```
> pip install pipenv
```

3) Ativar seu Virtualenv

Deverá abrir o seu terminal e digitar o seguinte comando abaixo:

```
> pipenv shell
```

4) Instalar as dependências do projeto

Deverá abrir o seu terminal e digitar o seguinte comando abaixo:

```
> pipenv install
```

5) Alterar variaveis de ambiente

Você deverá rodar o seguinte comando para gerar o .env

```
> cp .env.example .env
```
Agora você deve alterar as variaveis de ambiente com as credenciais que foram fornecidas: 

```
MONGO_DETAILS=

AWS_ACCESS_KEY_ID=
AWS_SECRET_ACESS_KEY=
```


6) Bom, agora que tudo foi instalado vamos buildar e subir a nossa aplicação:

Deverá abrir o seu terminal e digitar o seguinte comando abaixo:
```
> docker-compose build 

> docker-composes up -d 
```

## Resultados dos Requests:
<br>

### Antes de executar os comandos você pode ver a documentação da API e pode até mesmo executar os metodos por lá:

<br>

### Documentação: http://localhost:8080/docs

![alt tag]()

<br>

## Administrador / Auth: 

### 1) Método: POST (Criar Novo User Admin: http://localhost:8080/admin/)

Insira um novo cadastro nos campos abaixo e clique no botão Execute.

![alt tag](https://i.imgur.com/0v6hqGw.png)

E vejam o resultado abaixo:

![alt tag](https://i.imgur.com/9Rl8VjQ.png)

### 2) Método: POST (Login/ Autenticação: http://localhost:8080/admin/login)

Esse metodo vai gerar um Token na sua response usando esse token você consegue utilizar as outras rotas de livro.

Insira aqui o username(email) e senha que foram cadastrados anteriormente

![alt tag](https://i.imgur.com/hVAWKBK.png)

E aqui está a resposta com o token 

![alt tag](https://i.imgur.com/R6nuHEe.png)

para se authenticar basta inserir o token aqui e clicar em authorize. 

![alt tag](https://i.imgur.com/VMfvQL2.png)

Porintinho agora já pode utilizar as proximas rotas :)
<br>

## Livros

<br>

### 1) Método: POST (Criar Novo: http://localhost:8080/book/)

Insira um novo cadastro nos campos abaixo e clique no botão Execute.

![alt tag](https://i.imgur.com/re2WVYk.png)

E vejam o resultado abaixo:

![alt tag]()


Arquivos upados no bucket s3, o mais interessante do bucket é o sistema de pastas que ele utiliza, cada livro nosso tem uma pasta com o id respectivo, alem disso coloquei na frente de seu arquivo o seu id. no metodo de exclusão apenas removemos a pasta:

![alt tag]()


### 2) Método: GET (Selecionar Todos: http://localhost:8080/book/)

E vejam a lista de todos os livros criados abaixo: 

![alt tag]()


### 3) Método: GET (By id) (Selecionar por código mágico: http://localhost:8080/book/{id})

Bom, agora vamos regastar um determinado livro através do id. E vejam o resultado abaixo:

![alt tag]()


### 5) Método: DELETE (Excluir Por id: http://localhost:8080/book/{id})

E enfim, o último método. Vamos excluir esse livro.... :( :( e Vejam o resultado abaixo:

![alt tag]()

O Livro foi devidademente excluído e ao listar via GET observem que o funcionário(a) não consta mais na lista:

![alt tag]()


