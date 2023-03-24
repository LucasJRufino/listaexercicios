##Escreva um programa que peça ao usuário 
##para digitar uma lista de nomes e, em seguida, imprima o nome mais longo e o nome mais curto da lista.

lista = []
for i in range(5):
    lista.append(input("Insira um número: "))

print(max(lista))
print(min(lista))