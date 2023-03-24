##Escreva um programa que peça ao usuário para digitar uma lista de números e, em seguida, 
##crie uma nova lista que contenha apenas os números que aparecem mais de uma vez na lista original.

lista = []
novalista = []

for i in range(5):
    numero = (int(input("Insira um número: ")))
    if numero in lista:
        novalista.append(numero)

    lista.append(numero)

print(novalista)

