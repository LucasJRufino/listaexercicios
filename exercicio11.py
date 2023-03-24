##Escreva um programa que peça ao usuário 
##para digitar uma lista de números e, em seguida, calcule e imprima a soma de todos os números ímpares na lista.

lista = []
impar = 0
for i in range(5):
    lista.append(int(input("Insira um número: ")))

for i in lista:
    if i % 2 != 0:
        impar += i

print(impar)