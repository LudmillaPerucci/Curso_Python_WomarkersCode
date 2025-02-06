'''Peça ao usuário para informar o ano de nascimento.Em seguida,calcule e imprima a idade atual.'''

ano_atual = 2025

idade = input("Digite o ano do seu nascimento: ")
idade_int = int(idade)

print(f"Sua idade é: {ano_atual - idade_int}")