'''O programa deve calcular e apresentar a quantidade de números pares e ímpares inseridos. O processo de leitura deve ser encerrado quando o usuário informar o valor zero. Certifique-se de incluir validações para garantir que apenas números positivos sejam considerados na contagem e cálculos.'''

pares = 0
impares = 0

while True:
    valor = int(input("Insira um número positivo (0 para sair): "))

    if valor == 0:
        break
    if valor < 0:
        print("Apenas números positivos são permitidos.")
        continue

    if valor % 2 == 0:
        pares += 1
    else:
        impares += 1

print(f"Pares: {pares}, Ímpares: {impares}")
