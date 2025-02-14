# Instalação do NumPy

Para instalar o NumPy, execute o seguinte comando no terminal:

```sh
pip install numpy
```

# Importando o NumPy

Para utilizar o NumPy em um programa Python, importe-o da seguinte maneira:

```python
import numpy as np  # 'np' é um apelido para facilitar o uso do NumPy
```

# Criando Arrays no NumPy

## Criando um array com np.array()

```python
a = np.array([2, 4, 6, 8, 10])
```

Array bidimensional:

```python
b = np.array([
    [3,6,9,12,15],
    [1,3,4,5,6]
])
```

Array tridimensional:

```python
c = np.array([
    [0,9,8,7,6],
    [5,4,3,2,1],
    [10,11,12,13,15]
])
```

## Criando arrays preenchidos com zeros

```python
zero_array = np.zeros(shape=(5,3,6))
```

## Criando arrays preenchidos com uns

```python
um_array = np.ones((5,3))
```

## Criando arrays vazios (valores aleatórios da memória)

```python
vazio = np.empty(5)
```

## Criando arrays com np.arange()

```python
arr = np.arange(1, 11)
```

Definindo passo e intervalo:

```python
arr1 = np.arange(start=50, stop=200, step=20)
```

## Criando arrays espaçados linearmente com np.linspace()

```python
array_linear = np.linspace(0, 100, num=40, endpoint=False)  # endpoint=False exclui o valor final
```

# Descobrindo propriedades do array

```python
print(zero_array.shape)  # Dimensão do array (5,3,6)
print(zero_array.size)   # Quantidade total de elementos
print(zero_array.ndim)   # Número de dimensões do array
```

# Mudando a forma de um array

## np.reshape()

```python
arr = np.array([[2,4,2], [8,11,5]])
arr = arr.reshape(3,2)
print(arr)
```

## np.flatten() - Transformando um array multidimensional em unidimensional

```python
arr = np.array([[1, 2, 3], [4, 5, 6]])
flattened = arr.flatten()
print(flattened)
```

# Gerando valores aleatórios

## np.random.random() - Gerando números aleatórios entre 0 e 1

```python
random_array = np.random.random((3,3))
```

## np.random.randint() - Gerando números inteiros aleatórios dentro de um intervalo

```python
random_int_array = np.random.randint(0, 100, (3,3))
```

# Transformando dimensões de arrays

```python
a = np.array([1,2,3])
print(a.ndim)  # 1 dimensão

# Adicionando uma nova dimensão
horizontal = a[np.newaxis, :]  # Torna-se (1,3)
vertical = a[:, np.newaxis]    # Torna-se (3,1)
```

# Concatenando arrays

```python
a = np.array([1,2,3])
b = np.array([4,5,6])
c = np.concatenate((a, b))
d = np.concatenate((b, a))
```

# Filtrando elementos de um array

```python
e = np.array([
    [0,9,8,7,6],
    [5,4,3,2,14],
    [10,11,12,13,15]
])
maior_8 = e[e > 8]  # Filtra valores maiores que 8
```

# Operações matemáticas com arrays

```python
f = np.array([1,2,3])
print(f.sum())   # Soma total
print(f.max())   # Maior valor
print(f.min())   # Menor valor
print(f.mean())  # Média dos valores
```

Essa documentação possui os principais comandos do NumPy para manipulação de arrays. 
