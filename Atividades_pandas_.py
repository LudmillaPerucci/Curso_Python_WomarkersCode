# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np

# Carregar o dataset
df = pd.read_csv('saude_do_sono_estilo_vida.csv')
print(df.head(10))

# 1. Renomear colunas
df.rename(columns={
    'ID': 'Identificador',
    'Pressão sanguíneaaaa': 'Pressão Sanguínea',
    'Ocupação': 'Profissão',
    'Categoria BMI': 'Categoria IMC'
}, inplace=True)
print(df.head())

# 2. Média, mediana e moda de horas de sono por profissão
media_horas = df.groupby('Profissão')['Duração do sono'].mean()
mediana_horas = df.groupby('Profissão')['Duração do sono'].median()
moda = df.groupby('Profissão')['Duração do sono'].apply(lambda x: x.mode()[0] if not x.mode().empty else np.nan)
print(media_horas, mediana_horas, moda)

# 3. Porcentagem de engenheiros de software obesos
engenheiros_software = df[df['Profissão'] == 'Engenheiro de Software']
porcentagem_obesos = (len(engenheiros_software[engenheiros_software['Categoria IMC'] == 'Obesidade']) / len(engenheiros_software)) * 100
print(f"{porcentagem_obesos:.2f}% dos engenheiros de software são obesos.")

# 4. Advogados ou representantes de vendas dormem menos?
profissoes_df = df[df['Profissão'].isin(['Advogado(a)', 'Representante de Vendas'])]
media_profissoes = profissoes_df.groupby('Profissão')['Duração do sono'].mean()
resultado = "Advogado(a) dorme menos." if media_profissoes['Advogado(a)'] < media_profissoes['Representante de Vendas'] else "Representante de Vendas dorme menos."
print(resultado)

# 5. Quem dorme menos: enfermeiros ou médicos?
profissoes_df = df[df['Profissão'].isin(['Enfermeiro(a)', 'Médico(a)'])]
media_profissoes = profissoes_df.groupby('Profissão')['Duração do sono'].mean()
resultado = "Enfermeiro(a) dorme menos." if media_profissoes['Enfermeiro(a)'] < media_profissoes['Médico(a)'] else "Médico(a) dorme menos."
print(resultado)

# 6. Criar subconjunto de colunas
subconjunto = df[['Identificador', 'Gênero', 'Idade', 'Pressão Sanguínea', 'Frequência cardíaca']]
print(subconjunto.head())

# 7. Profissão menos frequente
profissao_menos_frequente = df['Profissão'].value_counts().idxmin()
print(f"A profissão menos frequente é: {profissao_menos_frequente}")

# 8. Quem tem maior pressão sanguínea média, homens ou mulheres?
agrupar = df.groupby('Gênero')['Pressão Sanguínea'].mean()
resultado = "Mulher tem maior pressão." if agrupar['Mulher'] > agrupar['Homem'] else "Homem tem maior pressão."
print(resultado)

# 9. É predominante dormir 8 horas por dia?
moda_sono = df['Duração do sono'].mode()[0]
print("Sim, é predominante." if moda_sono >= 8 else "Não, não é predominante.")

# 10. Pessoas com frequência cardíaca acima de 70 dão mais passos?
maiorFrequencia = df[df['Frequência cardíaca'] > 70]
menorFrequencia = df[df['Frequência cardíaca'] <= 70]
passosMaiorFreq = maiorFrequencia['Passos diários'].mean()
passosMenorFreq = menorFrequencia['Passos diários'].mean()
resultado = "acima de" if passosMaiorFreq > passosMenorFreq else "igual ou abaixo"
print(f"Pessoas com Frequência Cardíaca {resultado} 70 bpm dão mais passos.")
