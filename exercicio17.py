'''Criar um programa em Python que solicite três números ao usuário, utilize estruturas condicionais para determinar o maior entre eles e apresente o resultado'''

entrada_user = input("Entre com o primeiro valor: ")
valor1 = float(entrada_user)
entrada_user = input("Entre com o segundo valor: ")
valor2 = float(entrada_user)
entrada_user = input("Entre com o terceiro valor: ")
valor3 = float(entrada_user)

maior_valor = max(valor1,valor2,valor3)

print(f"O maior valor é: {maior_valor}")