import numpy as np  # Importa a biblioteca NumPy para manipulação de arrays

# Criando um array unidimensional com números inteiros
arr = np.array([2, 4, 6, 7, 8])

# Acessando o segundo elemento do array (índice 1)
print("Segundo elemento do array:", arr[1])  # Saída: 4

# Criando uma matriz 4x4 representando uma cartela de bingo
cartela_bingo = np.array([[16, 10,  3, 15],
                          [14, 23, 17, 27],
                          [ 6, 19,  3,  1],
                          [10,  4, 18, 19]])

print("\nCartela de Bingo:")
print(cartela_bingo)

# Transformando a matriz em um array unidimensional usando flatten()
cartela_flat = cartela_bingo.flatten()
print("\nCartela de Bingo transformada em array unidimensional (flatten):")
print(cartela_flat)

# Selecionando toda a segunda coluna da matriz e a transformando em uma matriz coluna (4x1)
segunda_coluna = cartela_bingo[:, 1].reshape((4, 1))
print("\nSegunda coluna da cartela de bingo, convertida em matriz coluna (4x1):")
print(segunda_coluna)

# Acessando a primeira linha da matriz
primeira_linha = cartela_bingo[0]
print("\nPrimeira linha da cartela de bingo:")
print(primeira_linha)

# Ordenando os elementos da matriz ao longo das linhas (ordem crescente para cada linha)
cartela_ordenada_linhas = np.sort(cartela_bingo)
print("\nCartela de Bingo ordenada por linha:")
print(cartela_ordenada_linhas)

# Ordenando os elementos da matriz ao longo das colunas (ordem crescente para cada coluna)
cartela_ordenada_colunas = np.sort(cartela_bingo, axis=0)
print("\nCartela de Bingo ordenada por coluna:")
print(cartela_ordenada_colunas)

# Criando uma matriz representando diferentes espécies e seus atributos
especies = np.array([[747,  89,  33,   5],
                     [623, 123,  32,  13],
                     [501,  22,  49,   2],
                     [116, 101,  42,  10],
                     [297,  56,  69,  22],
                     [613,  64,  27,   7],
                     [295,  84,  29,  14],
                     [692, 105,  72,  16],
                     [229, 103,  35,   5],
                     [374, 124,  70,   1]])

print("\nMatriz de espécies e atributos:")
print(especies)

# Transformando a matriz de espécies em um array unidimensional usando flatten()
especies_flat = especies.flatten()
print("\nMatriz de espécies transformada em array unidimensional (flatten):")
print(especies_flat)

# Criando um array unidimensional
arr1 = np.array([1, 2, 3, 4, 5])

# Criando uma máscara booleana para identificar elementos divisíveis por 3
mask = arr1 % 3 == 0
print("\nMáscara booleana (True para elementos divisíveis por 3):")
print(mask)

# Criando uma matriz onde cada linha contém um ID de pessoa e sua idade
pessoas_id_idade = np.array([[1, 22],  # Pessoa com ID 1 tem 22 anos
                              [2, 21],  # Pessoa com ID 2 tem 21 anos
                              [3, 27],  # Pessoa com ID 3 tem 27 anos
                              [4, 26]]) # Pessoa com ID 4 tem 26 anos

print("\nMatriz com ID de pessoas e suas idades:")
print(pessoas_id_idade)

# Transformando a matriz de ID e idades em um array unidimensional usando flatten()
pessoas_flat = pessoas_id_idade.flatten()
print("\nMatriz de ID e idades transformada em array unidimensional (flatten):")
print(pessoas_flat)
