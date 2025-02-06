#Faça um Programa que peça dois números e imprima o maior deles

entrada_user = input("Digite o primeiro valor: ")
num1 = int(entrada_user)
entrada_user = input("Digite o segundo valor: ")
num2 = int(entrada_user)

if num1 > num2:
    print(f"O maior número é: {num1}")
elif num2 >num1:
    print(f"O maior número é: {num2}")
elif num1 == num2:
    print("Os valores são iguais")
else:
    print("O valor informado não é válido")
