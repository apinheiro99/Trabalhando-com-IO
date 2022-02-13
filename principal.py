import os
os.system("clear")

arquivo_contatos = open("contatos.csv", encoding = "latin_1")

print(arquivo_contatos.readline(),end = "")
print(arquivo_contatos.readline(),end = "")
print(arquivo_contatos.readline(),end = "")