import os
os.system("clear")

try:
    with open("contatos.csv", encoding = "latin_1") as arquivo_contatos:
        for linha in arquivo_contatos:
            print(linha,end = "")
except FileNotFoundError:
    print("Arquivo nao encontrado")
except PermissionError:
    print("Permissao negada")