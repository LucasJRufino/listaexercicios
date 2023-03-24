##Escreva um programa que peça ao usuário para digitar uma lista de números e,
##em seguida, crie uma nova lista que contenha apenas os números que são divisíveis por 3.

lista = []
novalista = []
for i in range(5):
    lista.append(int(input("Insira um número: ")))

for i in lista:
    if i % 3 == 0:
        novalista.append(i)

print(novalista)