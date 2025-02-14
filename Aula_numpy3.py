import numpy as np 

# Matriz representando acidentes dos clientes nos últimos 3 anos
# Cada linha representa um cliente e cada coluna representa um ano
acidentes = np.array([[1, 3, 2],
                      [0, 1, 0],
                      [2, 1, 4],
                      [0, 0, 0],
                      [1, 1, 0]])

# 1. Identificar clientes com acidentes abaixo da média nos últimos 2 anos
# Calcula a média dos acidentes nos últimos 2 anos (colunas -2 e -1)
media_acidentes = np.mean(acidentes[:, -2:], axis=0)  

# Seleciona os clientes cuja média de acidentes é menor que a média geral
clientes_abaixo_media = np.where(np.mean(acidentes[:, -2:], axis=1) < np.mean(media_acidentes))[0]

print("\nClientes com acidentes abaixo da média nos últimos 2 anos (ganham desconto):")
print(clientes_abaixo_media)

# 2. Identificar clientes que tiveram pelo menos 2 anos sem cometer acidentes
# Conta quantos anos cada cliente teve 0 acidentes e seleciona aqueles com pelo menos 2 anos sem acidentes
clientes_sem_acidentes = np.where(np.sum(acidentes == 0, axis=1) >= 2)[0]

print("\nClientes que tiveram pelo menos 2 anos sem cometer acidentes:")
print(clientes_sem_acidentes)

# 3. Aplicar a função (3x + 2y + x*y) para dois arrays dados pela professora
x = np.array([1, 2, 3, 4, 5])  # Array com valores de x
y = np.array([5, 4, 3, 2, 1])  # Array com valores de y

# Aplica a fórmula matemática fornecida pela professora
resultado_funcao = 3*x + 2*y + x*y

print("\nResultado da função (3x + 2y + x*y) aplicada aos arrays:")
print(resultado_funcao)

# 4. Adicionar as notas dos trabalhos às notas das provas
notas_provas = np.array([[7, 8, 6],  # Notas dos alunos em 3 provas
                          [5, 9, 7],
                          [8, 6, 9]])

# Notas dos trabalhos que serão adicionadas a cada prova de cada estudante
notas_trabalho = np.array([1, 2, 1])  # Mesma nota para todas as linhas

# Soma as notas dos trabalhos às provas
notas_finais = notas_provas + notas_trabalho

print("\nNotas finais após adicionar a nota dos trabalhos:")
print(notas_finais)

# 5. Criando uma cartela de bingo e utilizando funções do NumPy
cartela_bingo = np.array([[16, 10,  3, 15],
                           [14, 23, 17, 27],
                           [ 6, 19,  3,  1],
                           [10,  4, 18, 19]])

# Ordena os valores dentro de cada linha da cartela
cartela_ordenada_linhas = np.sort(cartela_bingo)

# Ordena os valores dentro de cada coluna
cartela_ordenada_colunas = np.sort(cartela_bingo, axis=0)

# Seleciona a segunda coluna e transforma em um array 4x1
segunda_coluna = cartela_bingo[:, 1].reshape((4, 1))

# Transforma a cartela em um array unidimensional (1D)
cartela_flat = cartela_bingo.flatten()

print("\nCartela de bingo original:")
print(cartela_bingo)
print("\nCartela ordenada por linhas:")
print(cartela_ordenada_linhas)
print("\nCartela ordenada por colunas:")
print(cartela_ordenada_colunas)
print("\nSegunda coluna da cartela como um array 4x1:")
print(segunda_coluna)
print("\nCartela transformada em um array 1D:")
print(cartela_flat)

# 6. Gerando uma matriz aleatória com números inteiros entre 10 e 30
arr_aleatorio = np.random.randint(10, 31, size=(5, 3))

print("\nMatriz aleatória de números inteiros entre 10 e 30 (5x3):")
print(arr_aleatorio)
