arquivo1 = open("contatos-escrita.csv", encoding = "latin_1", mode = "w")
arquivo2 = open("contatos-escrita.csv", encoding = "latin_1", mode = "w")

contato_carol = "11,Carol,carol@carol.com.br\n"
contato_andreza = "12,Andreza,andreza@andreza.com.br\n"

arquivo1.write(contato_carol)
arquivo2.write(contato_andreza)

arquivo1.close()
arquivo2.close()