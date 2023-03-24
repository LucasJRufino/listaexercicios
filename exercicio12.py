##Escreva um programa que peça ao usuário para digitar uma lista de nomes e, em seguida, 
##verifique se um determinado nome está na lista. Se estiver, 
##imprima "O nome está na lista"; caso contrário, imprima "O nome não está na lista".

lista = []

for i in range(5):
    lista.append(input("Insira um nome: "))

if input("Qual nome deseja conferir? ") in lista:
    print("Nome presente na lista")
else:
    print("Nome não está na lista")
