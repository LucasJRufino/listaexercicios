##Escreva um programa que peça ao usuário 
##para digitar uma lista de números e, em seguida, encontre e imprima o segundo número mais alto na lista.

lista = []
novalista = []


for i in range(5):
    lista.append(int(input("Insira um número: ")))

novalista = lista
novalista.remove(max(lista))

print(max(novalista))