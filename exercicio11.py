'''Faça um programa que pergunte em que turno você estuda. Peça para digitar M - matutino ou V - vespertino ou N - noturno. Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.'''

print("Em qual turno você estuda?\n [M] - Matutino\n [V] - Vespertino\n [N] - Noturno\n")
turno = input()

if turno == 'M':
    print("Bom dia!")
elif turno == 'V':
    print("Boa tarde!")
elif turno == 'N':
    print("Boa noite!")
else:
    print("O valor informado está incorreto")