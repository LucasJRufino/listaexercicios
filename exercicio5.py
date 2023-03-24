##Escreva um programa que peça ao usuário para digitar uma lista de números e, em seguida, imprima a lista ordenada em ordem crescente.

lista = []
for i in range(5):
    lista.append(int(input("Insira um número: ")))

print(sorted(lista))