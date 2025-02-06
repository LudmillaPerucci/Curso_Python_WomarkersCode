'''Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido'''

nota = float(input("Digite uma nota entre zero e dez: "))


while nota < 0 or nota > 10:
    print("O valor está inválido.")
    nota = float(input("Digite uma nota entre zero e dez: "))  # Atualiza a variável `nota`

print(f"Nota válida: {nota}")



