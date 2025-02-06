'''Implemente um programa que classifique um aluno com base em sua pontuação em um exame. O programa deverá solicitar uma nota de 0 a 10. Se a pontuação for maior ou igual a 7, o aluno é aprovado; caso contrário, é reprovado.'''

entrada_user = input("Digite a sua nota: ")

nota = float(entrada_user)

if nota >= 7:
    print(f"Você foi aprovado com a nota {nota:.1f}")
else: 
    print(f"Você foi reprovado")