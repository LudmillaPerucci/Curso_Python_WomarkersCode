"""Faça um Programa que peça dois números,realize as principais operações soma,subtração,multiplicação,divisão"""

opcao = input("Escolha uma opção:\n"
    "1 - Soma\n"
    "2 - Subtração\n"
    "3 - Multiplicação\n"
    "4 - Divisão\n\n"
)

print("-------------------------------------------------------------------------------------------")

opcao_int = int(opcao)

num1 = input("Digite o primeiro número: ")
num2 = input("Digite o segundo número: ")

num1_int = int(num1)
num2_int = int(num2)


if opcao_int == 1:
    print(f"A soma de {num1_int} + {num2_int} = ",(num1_int + num2_int))
elif opcao_int ==2:
    print(f"A subtração de {num1_int} - {num2_int} = ",(num1_int - num2_int))
elif opcao_int ==3:
    print(f"A multiplicação de {num1_int} * {num2_int} = ",(num1_int * num2_int))
elif opcao_int == 4:
    if num1_int == 0 or num2_int == 0:
        print("Erro: Divisão por zero não é permitida.")
    elif num1_int > num2_int:
        print(f"A divisão de {num1_int} / {num2_int} = {num1_int / num2_int}")
    elif num2_int > num1_int:
        print(f"A divisão de {num2_int} / {num1_int} = {num2_int / num1_int:.1f}")
    else:
        print("Os números são iguais, a divisão é 1.")
else:
    print("Não foi possível realizar essa operação")
