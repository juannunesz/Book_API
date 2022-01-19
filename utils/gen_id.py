import string
import random

# Gera um codigo mágico de 6 caracteres maiusculos
def id_generator():
    return ''.join(random.choices(string.ascii_uppercase, k=6))