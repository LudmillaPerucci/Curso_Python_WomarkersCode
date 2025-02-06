'''Receba do usuário a quantidade de litros de combustível consumidos e a distância percorrida.
Calcule e imprima o consumo médio em km/l.'''

dist_percorrida = input ("Informe quantos quilomentros foram percorridos: ")
consumo_total = input("Informe o consumo do combustível: ")

dist_percorrida_float = float (dist_percorrida)
consumo_total_float = float(consumo_total)

print(f"O consumo médio por litro é: {dist_percorrida_float / consumo_total_float:.1f} Km/l")

