
import numpy as np


#Criar um array com 4 linhas e 3 colunas com valores aleatórios

array1 = np.random.rand(4, 3)
print(array1)
print("-----------------------------------------------------\n")

#2. Criar um array com valores inteiros, 3 linhas e 5 colunas

array2 = np.random.randint(1, 31, size = (3, 5))  
print(array2)
print("-----------------------------------------------------\n")

#3. Criar um array 5x10 inicializado com zeros

array3 = np.zeros((10,5))
print(array3)
print("-----------------------------------------------------\n")

#4. Criar um array de 0 a 90, pulando de 4 em 4

array4 = np.arange(0,91,4)
print(array4)
print("-----------------------------------------------------\n")

#5. Reduzir um array (5,7) para apenas uma dimensão

array5 = np.random.randint(1,31, (5,7))
array5_flatten = array5.flatten()
print(array5_flatten)
print("-----------------------------------------------------\n")

#6. Criar um array para cartelas de bingo (10 cartelas, 12 números cada, valores entre 1 e 30)

cartelas = np.random.randint(1, 31, (10, 4, 3))  # 10 cartelas de 4x3 que totaliza 12 números
print(cartelas)
print("-----------------------------------------------------\n")

#7. Fazer o reshape das cartelas para 5 cartelas de 4x6

cartelas_reshape = cartelas.reshape(5, 4, 6)
print(cartelas_reshape)
print("-----------------------------------------------------\n")

#Manipulando Arrays

#1. Trabalhando com o array de espécies

especies = np.array([
    [747,  89, 33,  5],     # ID da espécie, quantidade de representantes, profundidade, tamanho médio
    [623, 123, 32, 13],
    [501,  22, 49,  2],
    [116, 101, 42, 10],
    [297,  56, 69, 22],
    [613,  64, 27,  7],
    [295,  84, 29, 14],
    [692, 105, 72, 16],
    [229, 103, 35,  5],
    [374, 124, 70,  1]
],dtype=object)

#Criar array com a quantidade de espécies encontradas

qtd_especies = especies[:, 1]  # Segunda coluna
print(qtd_especies)
print("-----------------------------------------------------\n")

# Selecionar as 3 primeiras quantidades

print(qtd_especies[:3])
print("-----------------------------------------------------\n")

# Selecionar as 5 ultimas quantidades

print(qtd_especies[-5:])
print("-----------------------------------------------------\n")

# Criar array apenas com os tamanhos e ordenar

tamanhos = np.sort(especies[:, 3])
print(tamanhos)
print("-----------------------------------------------------\n")

# Array da maior espécie encontrada (tamanho = 22)

maior_especie = especies[especies[:, 3] == 22]
print(maior_especie)
print("-----------------------------------------------------\n")

# Filtrar espécie com ID 297

especie_297 = especies[especies[:, 0] == 297]
print(especie_297)
print("-----------------------------------------------------\n")

# Filtrar linha da espécie com 105 representantes

especie_105 = especies[np.where(especies[:, 1] == 105)]
print(especie_105)
print("-----------------------------------------------------\n")

# Substituir profundidades maiores que 60 por "Profundo"
profundidade = especies[:, 2]
indice_profundo = profundidade.astype(int) > 60  # Garantindo que a comparação seja com números inteiros
especies[indice_profundo, 2] = "Profundo"
print("Array atualizado com profundidade 'Profundo':")
print(especies)
print("-----------------------------------------------------\n")

# Adicionar duas novas espécies
novas_especies = np.array([
    [204, 10, 40, 12],
    [392, 11, 81, 11]
])
especies = np.vstack((especies, novas_especies))
print(especies)
print("-----------------------------------------------------\n")

# Adicionar nova coluna indicando se a espécie enxerga
coluna_visao = np.array([0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0])  # Incluí os novos elementos
especies = np.column_stack((especies, coluna_visao))
print(especies)
print("-----------------------------------------------------\n")

acidentes = np.array([
    [1, 3, 2],
    [0, 1, 0],
    [2, 1, 4],
    [0, 0, 0],
    [1, 1, 0]
])

# Identificar clientes abaixo da média de acidentes nos últimos 2 anos
media_acidentes = np.mean(acidentes[:, -2:], axis=1)
clientes_desconto = np.where(media_acidentes < np.mean(media_acidentes))
print(clientes_desconto)
print("-----------------------------------------------------\n")

# Identificar cliente com pelo menos 2 anos sem acidentes
clientes_sem_acidente = np.where(np.sum(acidentes == 0, axis=1) >= 2)
print(clientes_sem_acidente)
print("-----------------------------------------------------\n")

# Aplicar a função (3x + 2y + x*y)
x = np.array([1, 2, 3])
y = np.array([4, 5, 6])

resultado = 3*x + 2*y + x*y
print(resultado)
print("-----------------------------------------------------\n")

# Adicionar valores [1, 2, 1] para cada prova
notas = np.random.randint(0, 10, (5, 3))  # Exemplo de notas de 5 alunos e 3 provas
notas += np.array([1, 2, 1])
print(notas)
print("-----------------------------------------------------\n")


a57 = np.random.random((5,7))
print(a57)
a57_flatten = a57.flatten()
print("-----------------------------------------------------\n")
print(a57_flatten)
print("-----------------------------------------------------\n")

bingo = np.random.randint(1,31, size=(10,4,3))
print(bingo)
print("-----------------------------------------------------\n")


bingo_resh = bingo.reshape((5,4,6))
print(bingo_resh)
print("-----------------------------------------------------\n")