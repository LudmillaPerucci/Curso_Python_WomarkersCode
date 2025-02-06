'''Escreva um programa que calcule o salário líquido. Lembrando de declarar o salário bruto e o percentual de desconto do Imposto de Renda.
Renda até R$ 1.903,98: isento de imposto de renda;
Renda entre R$ 1.903,99 e R$ 2.826,65: alíquota de 7,5%;
Renda entre R$ 2.826,66 e R$ 3.751,05: alíquota de 15%;
Renda entre R$ 3.751,06 e R$ 4.664,68: alíquota de 22,5%;
Renda acima de R$ 4.664,68: alíquota máxima de 27,5%.'''

entrada_user = input("Informe o seu salário: ")
salario_user = float(entrada_user)

if salario_user <= 1903.98:
    print("Você está isento do imposto de renda")
elif salario_user >=1903.99 and salario_user <=2826.65:
    salario_atual = salario_user - (salario_user *0.075)
    print(f"Salario ajustado com a aliquota de 7,5 %: {salario_atual:.2f}")
elif salario_user >=2826.66 and salario_user <=3751.05:
    salario_atual = salario_user - (salario_user *0.15)
    print(f"Salario ajustado com a aliquota de 15%: {salario_atual:.2f}")
elif salario_user >=3751.06 and salario_user <=4664.68:
    salario_atual = salario_user - (salario_user *0.225)
    print(f"Salario ajustado com a aliquota de 22,5%: {salario_atual:.2}")
elif salario_user > 4664.68:
    salario_atual = salario_user - (salario_user *0.275)
    print(f"Salario ajustado com a aliquota de 27,5%: {salario_atual:.2f}")
else:
    print("Valor incorreto, tente novamente")
