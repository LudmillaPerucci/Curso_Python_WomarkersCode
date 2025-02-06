'''Desenvolva um programa que solicite ao usuário os comprimentos dos três lados de um triângulo e classifique-o como equilátero, isósceles ou escaleno.

Equilátero: todos os lados com o mesmo valor.
Isósceles: dois lados com o mesmo valor.
Escaleno: todos os lados com medidas distintas.'''

entrada_user = input("Informe o valor do primeiro lado do triangulo: \n")
lado1 = float(entrada_user)
entrada_user = input("Informe o valor do segundo lado do triangulo: \n")
lado2 = float(entrada_user)
entrada_user = input("Informe o valor do terceiro lado do triangulo: \n")
lado3 = float(entrada_user)

if lado1 == lado2 and lado2 == lado3:
    print('Esse triângulo é o Equilátero')
elif lado1 == lado2 and lado3 != lado1:
    print("Esse triângulo é o Isóceles")
elif lado1 != lado2 and lado1 != lado3 and lado2 != lado3:
    print("Esse triângulo é o Escaleno")
else:
    print("Os valores informados são inválidos")