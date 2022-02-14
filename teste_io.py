import os
os.system("clear")

arquivo = open("contatos.csv", encoding = "latin_1")

print(type(arquivo))

print(type(arquivo.buffer))

conteudo = arquivo.buffer.read()

print(conteudo)

texto_em_bytes = bytes("Este é um texto em bytes", "latin_1")
print(texto_em_bytes)
print(type(texto_em_bytes))

arquivo.close()