def livro_helper(livro) -> dict:
    textos = []
    for itens in livro['texto']:
        textos.append(itens)

    ilustracoes = []
    for itens in livro['ilustracoes']:
        ilustracoes.append(itens)

    return {
        "id": livro['id'],
        "titulo": livro['titulo'],
        "autor": livro['autor'],
        "professor": livro['professor'],
        "texto": textos,
        "ilustracao": ilustracoes,
    }


def admin_helper(admin) -> dict:
    return {
        "id": str(admin['_id']),
        "fullname": admin['fullname'],
        "email": admin['email'],
    }
