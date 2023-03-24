##Escreva um programa que peça ao usuário para digitar uma lista de palavras e,
##em seguida, crie uma nova lista que contenha apenas as palavras que têm um número ímpar de letras.

lista = []
novalista = []
for i in range(5):
    lista.append(input("Insira uma palavra: "))

for i in lista:
    if len(i) % 2 != 0:
        novalista.append(i)

print(novalista)