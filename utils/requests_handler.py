from fastapi import HTTPException
from gen_id import id_generator
from aws.handler_s3 import upload_bucket_s3


def request_helper(titulo, autor, professor,textos, ilustracoes):
    livro = {
        "id": id_generator(),
        "titulo": titulo,
        "autor": autor,
        "professor": professor,
        "texto": [],
        "ilustracoes": []
    }

    text_handler(textos, livro)

    ilustracao_handler(ilustracoes, livro)

    return livro

def ilustracao_handler(ilustracoes, livro):
    valida_numero_itens(ilustracoes)
    pg_ilustracao = 6
    for ilustracao in ilustracoes:
        valida_upload(ilustracao.filename)

        url = upload_bucket_s3(ilustracao, livro['id'])

        pg_ilustracao += 1
        livro['ilustracoes'].append({"pagina": pg_ilustracao, "conteudo": url})

def text_handler(textos, livro):
    pg_text = 0
    for texto in textos:
        n_texto = texto.split(',')
        valida_numero_itens(n_texto)
        for tx in n_texto:
            pg_text += 1
            livro['texto'].append( {"pagina": pg_text, "conteudo": tx})

def valida_numero_itens(itens):
    if len(itens) > 6:
            raise HTTPException(status_code=404, detail="Porfavor insira somente 6 itens no campo Ilustacao / Textos")

def valida_upload(filename): 
    res = filename.lower().endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif'))
    if res != True: 
        raise HTTPException(status_code=404, detail="Porfavor insira somente arquivos de imagem")
