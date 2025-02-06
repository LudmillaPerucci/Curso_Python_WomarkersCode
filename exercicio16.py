'''Desenvolver um programa que solicite a idade do usuário e identifique se ele é uma criança, um adolescente, adulto ou idoso'''

entrada_user = input("Informe a sua idade: ")

idade_user = int(entrada_user)

if idade_user >= 0 and idade_user <=12:
    print("Você é uma criança")
elif idade_user >= 13 and idade_user <=17:
    print("Você é um adolescente")
elif idade_user >= 18 and idade_user <=59:
    print("Você é um adulto")
elif idade_user >= 60:
    print("Você é um idoso")
else:
    print("Valor inválido, tente novamente")
