import os
os.system("clear")

arquivo_contatos = open("nao-existe.csv", encoding = "latin_1")

for linha in arquivo_contatos:
    print(linha,end = "")

arquivo_contatos.close()