import os
os.system("clear")

arquivo_contatos = open ("contatos-escrita.csv", encoding = "latin_1", mode = "a")

contato = "11,carol,carol@carol.com.br\n"

arquivo_contatos.write(contato)