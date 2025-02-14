def calcular_media(valores):
    if not valores:  
        return 0  

    soma = sum(valores)  
    tamanho = len(valores)  
    return soma / tamanho  


continuar = True
valores = []

while continuar:
    valor = input('Digite um número para entrar na sua média ou "ok" para calcular o valor: ')
    
    if valor.lower() == 'ok':
        continuar = False
    else:
        try:
            valores.append(float(valor))  
        except ValueError:
            print("Por favor, digite um número válido.")

media = calcular_media(valores)
print(f'A média calculada para os valores {valores} foi de {media:.2f}')
