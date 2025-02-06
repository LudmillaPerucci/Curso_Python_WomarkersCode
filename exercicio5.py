
print("Bem vindo(a) ao programa que calcula o tempo de viagem\n")
print("-------------------------------------------------------")

avião = 600
carro = 100
onibus = 80

dist_percorrida = input("Digite a distancia percorrida: ")

dist_percorrida_float = float(dist_percorrida)

print(f"O tempo que o avião levaria para realizar a viagem é: {dist_percorrida_float /avião:.1f} horas\n")
print(f"O tempo que o carro levaria para realizar a viagem é: {dist_percorrida_float /carro:.1f} horas\n")
print(f"O tempo que o onibus levaria para realizar a viagem é: {dist_percorrida_float /onibus:.1f} horas\n")