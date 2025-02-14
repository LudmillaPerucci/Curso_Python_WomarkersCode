import numpy as np  # Importa a biblioteca NumPy para trabalhar com arrays e cálculos numéricos

# Criando um array NumPy a partir de uma lista
l = [1, 2, 3, 4]
arr1 = np.array(l)
print("Array criado a partir de uma lista:")
print(arr1)

# Criando um array 2x2 preenchido com zeros
arr1 = np.zeros((2, 2))
print("\nArray 2x2 preenchido com zeros:")
print(arr1)

# Criando um array 10x5 preenchido com zeros
# O primeiro número representa a quantidade de linhas e o segundo representa as colunas
arr1 = np.zeros((10, 5))
print("\nArray 10x5 preenchido com zeros:")
print(arr1)

# Criando um array com valores de 1 a 10 (intervalo fechado à esquerda)
arr1 = np.arange(1, 11)
print("\nArray com valores de 1 a 10:")
print(arr1)

# Verificando o tipo da variável 'arr1'
tipo_arr1 = type(arr1)
print("\nTipo da variável 'arr1':")
print(tipo_arr1)

# Criando um array 4x3 com valores aleatórios entre 0 e 1
# np.random.random((linhas, colunas)) gera números decimais aleatórios entre 0 e 1
arr2 = np.random.random((4, 3))
print("\nArray 4x3 com valores aleatórios entre 0 e 1:")
print(arr2)

# Criando um array 5x3 com valores inteiros aleatórios entre 10 e 30
# np.random.randint(inicio, fim, size=(linhas, colunas)) gera números inteiros aleatórios entre 'inicio' e 'fim-1'
arr2 = np.random.randint(10, 31, size=(5, 3))
print("\nArray 5x3 com valores inteiros aleatórios entre 10 e 30:")
print(arr2)
