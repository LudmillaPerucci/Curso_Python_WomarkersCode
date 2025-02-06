'''Solicite ao usuário o peso em kg e a altura em metros.
Calcule e imprima o Índice de Massa Corporal (IMC) usando a fórmula:
IMC = peso / (altura x altura).'''

print("Bem vindo(a) a calculadora de IMC")
print("-------------------------------------")


peso = input("Informe o seu peso: ")
altura = input("Informe a sua altura respeitando as casas decimais: ")

peso_float = float(peso)
altura_float = float(altura)

print(f"O seu IMC é: {peso_float / (altura_float * altura_float):.2f}")