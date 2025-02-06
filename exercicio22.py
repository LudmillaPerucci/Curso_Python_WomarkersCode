'''Faça um Programa que peça as quatro notas de 5 alunos, calcule e armazene numa lista a média de cada aluno, imprima o número de alunos com média maior ou igual a 7.0.'''

lstMedia=[]

for Aluno in range(0,5):
    print(f"Digite a nota do aluno {Aluno+1}")
    notasAlunos=0.0
    for notas in range(0,4):
        notasAlunos += float(input(f"Digite a nota  {notas+1}: "))
    lstMedia.append(notasAlunos/4)

# for valores in lstMedia:
#     if valores >=7:
#         quantidade++;


print(sum(x >= 7 for x in lstMedia))