##Escreva um programa que peça ao usuário para digitar uma lista de números e,
##em seguida, crie uma nova lista que contenha apenas os números que são divisíveis por um número fornecido pelo usuário.

lista = []
novalista = []
for i in range(5):
    lista.append(int(input("Insira um número: ")))

numero = int(input("Insira o número: "))

for i in lista:
    if i % numero == 0:
        novalista.append(i)

print(novalista)
