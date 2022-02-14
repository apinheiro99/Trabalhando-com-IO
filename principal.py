import os
os.system("clear")

try:
    arquivo_contatos = open("nao-existe.csv", encoding = "latin_1")
    for linha in arquivo_contatos:
        print(linha,end = "")
except FileNotFoundError:
    print("Arquivo nao encontrado")
finally:
    arquivo_contatos.close()