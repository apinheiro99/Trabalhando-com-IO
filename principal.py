import os
os.system("clear")

arquivo_contatos = open("contatos.csv", encoding = "latin_1")

conteudo = arquivo_contatos.readlines()

print(conteudo)
print()

for linha in conteudo:
    print(linha, end = "")