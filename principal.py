import os
from contatos_utils import csv_para_contatos

os.system("clear")

try:
    contatos = csv_para_contatos("contatos.csv")

    for contato in contatos:
        print(f"{contato.id} - {contato.nome} - {contato.email}")
except FileNotFoundError:
    print("Arquivo nao encontrado")
except PermissionError:
    print("Permissao negada")