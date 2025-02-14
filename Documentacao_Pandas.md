# Documentação Completa de Comandos do Pandas

## Instalação do Pandas
Para instalar o Pandas, execute o seguinte comando:
```bash
pip install pandas
```

## Importação do Pandas
Para importar o Pandas, utilize:
```python
import pandas as pd
```

## Leitura de Arquivos
### CSV
```python
df_csv = pd.read_csv('arquivo.csv')
```

### Excel
```python
df_excel = pd.read_excel('planilha.xlsx', sheet_name='nome_da_planilha')
```

### JSON
```python
df_json = pd.read_json('arquivo.json')
```

### Parquet
```python
df_parquet = pd.read_parquet('arquivo.parquet')
```

## Análise de Dados
### Visualização Inicial
- `df.head(n)`: Mostra as primeiras `n` linhas do DataFrame. Se `n` não for especificado, exibe as 5 primeiras linhas.
```python
df.head(10)
```

- `df.tail(n)`: Mostra as últimas `n` linhas do DataFrame.
```python
df.tail(10)
```

- `df.info()`: Exibe informações sobre as colunas, tipos de dados e valores nulos.
```python
df.info()
```

- `df.shape`: Retorna uma tupla com a quantidade de linhas e colunas.
```python
linhas, colunas = df.shape
```

- `df.describe()`: Retorna estatísticas descritivas das colunas numéricas.
```python
df.describe()
```

## Atributos do DataFrame
- `df.values`: Retorna os dados como um array NumPy.
```python
dados = df.values
```

- `df.columns`: Retorna os nomes das colunas.
```python
colunas = df.columns
```

- `df.index`: Retorna os índices das linhas.
```python
indices = df.index
```

## Manipulação de Dados
### Renomear Colunas
```python
df.rename(columns={'Coluna_Antiga': 'Coluna_Nova'}, inplace=True)
```

### Adicionar Coluna
```python
df['Nova_Coluna'] = valor
```

### Remover Coluna
```python
df = df.drop(columns=['Coluna1', 'Coluna2'])
```

### Remover Linhas
```python
df = df.drop(index=[0, 1, 2])
```

### Preenchimento de Valores Nulos
```python
df.fillna(valor, inplace=True)
```

### Remoção de Valores Nulos
```python
df.dropna(inplace=True)
```

### Substituir Valores
```python
df.replace({'valor_antigo': 'valor_novo'}, inplace=True)
```

## Ordenação de Dados
- `df.sort_values(by='coluna')`: Ordena os dados pelo valor da coluna especificada.
```python
df_ordenado = df.sort_values(by='Altura (cm)')
```

- `df.sort_values(by='coluna', ascending=False)`: Ordena os dados em ordem decrescente.
```python
df_ordenado_desc = df.sort_values(by='Altura (cm)', ascending=False)
```

## Filtros e Subconjuntos
### Filtragem com `isin()`
Filtra o DataFrame para incluir apenas valores contidos em uma lista.
```python
df_filtrado = df[df['Coluna'].isin(['Valor1', 'Valor2'])]
```

### Subconjunto de Linhas
Filtra dados com base em condições.
```python
df_filtrado = df[df['Idade'] > 30]
```

### Subconjunto com Base em Texto
Filtra dados que contêm determinada string.
```python
df_filtrado = df[df['Nome'].str.contains('João')]
```

### Subconjunto com Base em Múltiplas Condições
```python
df_filtrado = df[(df['Idade'] > 30) & (df['Salario'] > 5000)]
```

## Agrupamento de Dados
### Agrupar por uma Coluna
```python
df_grouped = df.groupby('Categoria').mean()
```

### Contagem de Valores por Grupo
```python
df_grouped = df.groupby('Categoria').size()
```

## Estatísticas Básicas
### Média, Mediana e Moda
```python
media = df['Coluna'].mean()
mediana = df['Coluna'].median()
moda = df['Coluna'].mode()
```

### Mínimo e Máximo
```python
minimo = df['Coluna'].min()
maximo = df['Coluna'].max()
```

### Desvio Padrão e Variância
```python
desvio_padrao = df['Coluna'].std()
variancia = df['Coluna'].var()
```

