import os
from contatos_utils import contatos_para_json, contatos_para_pickle, csv_para_contatos, json_para_contatos, pickle_para_contatos

os.system("clear")

def imprime(contatos, texto):
    print(texto)
    for contato in contatos:
        print(f"{contato.id} - {contato.nome} - {contato.email}")
    print()
    print()

try:
    contatos = csv_para_contatos("contatos.csv")
    imprime(contatos, "CSV para contatos")

    contatos_para_pickle(contatos, "contatos.pickle")
    pickle_contatos = pickle_para_contatos("contatos.pickle")
    imprime(pickle_contatos, "PICKLE para contatos")

    contatos_para_json(contatos, "contatos.json")
    json_contatos = json_para_contatos("contatos.json")
    imprime(json_contatos, "JSON para contatos")

except FileNotFoundError:
    print("Arquivo nao encontrado")
except PermissionError:
    print("Permissao negada")

