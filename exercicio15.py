##Escreva um programa que peça ao usuário para digitar uma lista de números e, em seguida,
##remova todos os números duplicados da lista e imprima a nova lista.

lista = []
novalista = []

for i in range(5):
    lista.append(int(input("Insira um número: ")))

for i in lista:
    if i not in novalista:
        novalista.append(i)
    
print(novalista)