import xmlrpc.client

conexao = xmlrpc.client.ServerProxy('http://localhost:8000')# String para conexao ao servidor


numero = int(input("Insira um número inteiro: ")) # Pede ao utilizador quer insiria um número inteiro


print(" \n A tabauda do "+str(numero)+ " é : \n")# Informa ao Utilizador que a seguir irá aparecer a tabuada

print(conexao.tb(numero))  # Retoma a tabuada do numero pedido pelo cliente

