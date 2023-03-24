##Escreva um programa que peça ao usuário para digitar uma lista de números e, 
##em seguida, imprima apenas os números que são menores do que 5.

lista = []
for i in range(5):
    lista.append(int(input("Insira um número: ")))

for i in lista:
    if i < 5:
        print(i)