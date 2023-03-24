##Escreva um programa que peça ao usuário para digitar uma lista de nomes e, 
##em seguida, crie uma nova lista que contenha apenas os nomes que contêm a letra "e".

lista = []
for i in range(5):
    lista.append(input("Insira uma palavra: "))

for i in lista:
    if 'e' in i.lower():
        print(i)