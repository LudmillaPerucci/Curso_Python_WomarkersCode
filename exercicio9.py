'''Faça um programa que utilize 4 variáveis como preferência no final print uma mensagem amigável utilizando as variáveis criadas. Exemplos de variáveis: nome, idade, lugar, profissão... Exemplo de retorno: Olá Maria, prazer te conhecer. Sou de São Paulo também e estou migrando de área. Lembrando que para o retorno vamos usar print com as variáveis criadas e este texto é somente um exemplo, utilizem a criatividade'''

nome = input("Informe o seu nome: ")
idade = input("Informe a sua idade: ")
cidade = input ("Em qual cidade você reside? ")
profissão = input( "Qual a sua profissão? ")

idade_int = int(idade)

print(f"Olá, me chamo {nome}, tenho {idade_int} anos e moro em {cidade}.\nTrabalho como {profissão} e estou empolgado(a) com as novas possibilidades que surgiram em minha jornada profissional!")