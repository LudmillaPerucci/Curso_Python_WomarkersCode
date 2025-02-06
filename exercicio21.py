'''Utilizando listas, faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
"Telefonou para a vítima?"
"Esteve no local do crime?"
"Mora perto da vítima?"
"Devia para a vítima?"
"Já trabalhou com a vítima?"'''

print("Responda as perguntas: \n [1] - Telefonou para a vítima?\n [2] - Esteve no local do crime?\n [3] - Mora perto da vítima?\n [4] - Devia para a vítima?\n [5] - Já trabalhou com a vítima?")

opcoes = []


opcoes.append(input("Digite a resposta da 1ª pergunta: "))
opcoes.append(input("Digite a resposta da 2ª pergunta: "))
opcoes.append(input("Digite a resposta da 3ª pergunta: "))
opcoes.append(input("Digite a resposta da 4ª pergunta: "))
opcoes.append(input("Digite a resposta da 5ª pergunta: "))

contagem = opcoes.count("sim") 

if contagem == 2:
    print("Suspeita")
elif contagem == 3 or contagem == 4:
    print("Cúmplice")
elif contagem == 5:
    print("Assassino")
else:
    print("Inocente")

