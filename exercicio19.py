'''Faça um programa que lê três números inteiros e os mostra em ordem crescente.'''

entrada_user = input("Digite o primeiro valor: ")
valor1 = int(entrada_user)
entrada_user = input("Digite o segundo valor: ")
valor2 = int(entrada_user)
entrada_user = input("Digite o terceiro valor: ")
valor3 = int(entrada_user)

valores = sorted([valor1,valor2,valor3])

print(f"Os valores em ordem crescente são: {valores}")