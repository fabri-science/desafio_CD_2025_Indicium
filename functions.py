# funções usadas no desafio indicium 2025

import pandas as pd

def process_runtime(entry:str)->int:
    """
    Função que converte uma string do formato 'YYY min' em um inteiro YYY.
    """
    if pd.isna(entry):
        return entry
    else:
        return int(entry.split(' ')[0])

def gross_converter(entry:str)->int:
    """
    Função que converte o faturamento no formato YYY,YYY,YYY em int.
    """
    if pd.isna(entry):
        return entry
    else:
        return int(''.join(entry.split(',')))
    
def genre_preprocess(entry:str)->str:
    """
    Função que recebe uma str de gêneros e retorna somente o primeiro gênero.
    """
    if pd.isna(entry):
        return entry
    else:
        return entry.split(', ')[0]
    
def get_data(path:str='desafio_indicium_imdb.csv')->pd.DataFrame:
    """
    Função que recebe o path do dataset e retorna um DataFrame com as colunas processadas com process_runtime, gross_converter e genre_preprocess
    """
    # carregar dados:
    df = pd.read_csv(path, index_col=0, header=0)
    # processar Released_Year
    df['Released_Year'] = pd.to_numeric(df['Released_Year'], errors='coerce')
    # processar Runtime
    df['Runtime'] = df['Runtime'].apply(process_runtime)
    # processar Gross
    df['Gross'] = df['Gross'].apply(gross_converter)/1e6
    # processar Genre
    df['Genre'] = df['Genre'].apply(genre_preprocess)
    return df

def replace_metascore_nan(df:pd.DataFrame)->pd.DataFrame:
    """
    Função que recebe o dataset e retorna um DataFrame com os NaN de Meta_score substituidos com o Meta_score médio por gênero.
    """
    # recebe dataframe
    data = df.copy()
    # cria um dataframe com a nota média de cada gênero
    inft = data.groupby(by=['Genre'])['Meta_score'].mean()
    # substitui NaN de Meta_score com a nota média do gênero 
    for index in data.index:    
        if pd.isnull(data['Meta_score'][index]):
            data.loc[index ,'Meta_score'] = inft.loc[data['Genre'][index]]
    return data

def replace_gross_nan(df:pd.DataFrame)->pd.DataFrame:
    """
    Função que recebe o dataset e retorna um DataFrame com os NaN de Gross substituidos com o Gross médio por gênero e por ano.
    """
    # recebe dataframe
    data = df.copy()
    # cria um dataframe com a nota média de cada gênero
    inft = data.groupby(by=['Genre', 'Released_Year'])[['Gross']].mean()
    # substitui NaN de Gross com o faturamento médio por gênero por ano 
    for index in data.index:    
        if pd.isnull(data['Gross'][index]):
            data.loc[index ,'Gross'] = inft.loc[data['Genre'][index], data['Released_Year'][index]].values[0]
    return data

def bin_year(df:pd.DataFrame):
    """
    Função que recebe um DataFrame com Released_Year no mesmo range de data_imdb_cleaned.csv e retorna o DataFrame com
    a coluna Released_Year substituida pela variável categórica que representa as decadas
    """
    # criação dos bins e labels para categorizar as décadas de acordo com data_imdb_cleaned
    data_cut = pd.read_csv('data_imdb_cleaned.csv')['Released_Year']
    labels = [f'{x}s' for x in range(1920, 2010+1, 10)]
    _, bins_ = pd.cut(data_cut, bins=10, retbins=True, labels=labels)
    # substituição de Released_Year por Released_Decade
    df['Released_Decade'] = pd.cut(df['Released_Year'], bins=bins_, labels=labels)
    df = df.drop(columns=['Released_Year'])
    return df

def process_input_test(test_input:dict, type_cols:str):
    """
    Função que recebe um dict de input teste e o tipo de dados que consideraremos (type_cols) (completo=all ou somente numéricos=num)
    e retorna o DataFrame no mesmo formato de data_imdb_cleaned.csv com todas as colunas (type_cols=all) ou somente as variáveis
    numéricas (type_cols=num)
    """
    inputs = ['Certificate', 'Genre', 'Director', 'Released_Decade', 'Runtime', 'Meta_score', 'No_of_Votes', 'Gross']
    num_cols = ['Runtime', 'Meta_score', 'No_of_Votes', 'Gross']
    df = pd.DataFrame(test_input, index=[0])
    # processar Released_Year
    df['Released_Year'] = pd.to_numeric(df['Released_Year'], errors='coerce')
    # processar Runtime
    df['Runtime'] = df['Runtime'].apply(process_runtime)
    # processar Gross
    df['Gross'] = df['Gross'].apply(gross_converter)/1e6
    # processar Genre
    df['Genre'] = df['Genre'].apply(genre_preprocess)
    # bin ano
    df = bin_year(df)
    if type_cols == 'all':
        return df[inputs]
    elif type_cols == 'num':
        return df[num_cols]
    else:
        raise ValueError('Digite all ou num')
    