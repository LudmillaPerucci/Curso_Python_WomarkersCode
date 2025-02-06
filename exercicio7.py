'''Faça um programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
Calcule e mostre o total do seu salário no referido mês.'''

valor_hora = input("Informe o valor que você ganha por hora: ")
horas_trabalhadas = input(" Informe quantas horas você trabalha no mês: ")

valor_hora_float = float(valor_hora)
horas_trabalhadas_float = float(horas_trabalhadas)

print(f"O seu salário é: {valor_hora_float * horas_trabalhadas_float:.2f}")
