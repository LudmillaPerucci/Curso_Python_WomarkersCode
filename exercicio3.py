'''Faça um Programa que peça a quantidade de quilômetros,transforme em metros,centímetros e milímetros'''

km = input("Digite a quantidade de quilometros: ") 

km_conv_float = float(km)

print(f"A conversão de quilometro(s) para metro(s) é: {km_conv_float * 1000:,.2f}") 
print(f"A conversão de quilometro(s) para centimetro(s) é: {km_conv_float * 100000:,.2f}") 
print(f"A conversão de quilometro(s) para milimetro(s) é: { km_conv_float * 1000000:,.2f}") 