##Escreva um programa que peça ao usuário
##para digitar uma lista de palavras e, em seguida, imprima apenas as palavras que começam com a letra "a".

lista = []
for i in range(5):
    lista.append(input("Insira uma palavra: "))

for i in lista:
    if i.lower().startswith('a'):
        print(i, " ")