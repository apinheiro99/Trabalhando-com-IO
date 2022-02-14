import os
from contatos_utils import contatos_para_json, contatos_para_pickle, csv_para_contatos, pickle_para_contatos

os.system("clear")

def imprime(contatos):
    for contato in contatos:
        print(f"{contato.id} - {contato.nome} - {contato.email}")
    print()
    print()

try:
    contatos = csv_para_contatos("contatos.csv")
    imprime(contatos)

    contatos_para_pickle(contatos, "contatos.pickle")

    pickle_contatos = pickle_para_contatos("contatos.pickle")
    imprime(pickle_contatos)

    contatos_para_json(contatos, "contatos.json")

except FileNotFoundError:
    print("Arquivo nao encontrado")
except PermissionError:
    print("Permissao negada")

