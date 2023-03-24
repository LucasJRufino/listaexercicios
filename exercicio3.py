##Escreva um programa que peça ao usuário
##para digitar uma lista de números e, em seguida, encontre o número máximo e o número mínimo da lista.

lista = []
for i in range(5):
    lista.append(int(input("Insira um número: ")))

print(max(lista))
print(min(lista))