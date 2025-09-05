# Desafio Cientista de Dados 2025 - Indicium

**Autor:** Matheus Augusto Fabri

Este é um repositório contendo a análise desenvolvida para o Desafio Cientista de Dados 2025 da Indicium. O desafio consiste em realizar uma análise exploratória de dados de uma tabela de filmes retirados do IMDB (Internet Movie Database) e criar um modelo de aprendizado de máquina para inferir a nota do IMDB (a nota média dada pelos usuários), dadas as informações do filme em questão. O conjunto de dados consiste em um arquivo `csv` contendo 999 filmes e 15 colunas com as seguintes informações:

- Series_Title – Nome do filme
- Released_Year - Ano de lançamento
- Certificate - Classificação etária
- Runtime – Tempo de duração
- Genre - Gênero
- IMDB_Rating - Nota do IMDB
- Overview - Overview do filme
- Meta_score - Média ponderada de todas as críticas 
- Director – Diretor
- Star1 - Ator/atriz #1
- Star2 - Ator/atriz #2
- Star3 - Ator/atriz #3
- Star4 - Ator/atriz #4
- No_of_Votes - Número de votos
- Gross - Faturamento

Os arquivos contidos neste repositório são:

- `LH_CD_MATHEUSAUGUSTOFABRI.ipynb`: Jupyter Notebook contendo o desenvolvimento do projeto.
- `functions.py`: Módulo com funções auxiliares que são utilizadas no Jupyter Notebook.
- `desafio_indicium_imdb.csv`: Arquivo com os dados fornecidos pela Indicium.
- `data_imdb_cleaned.csv`: Arquivo com os dados após data cleaning.
- `data_imdb_final.csv`: Arquivo com os dados usados para treinar os modelos.
- `final_model.pkl`: Modelo final salvo em `pkl`.

A versão do Python utilizada neste projeto foi 3.12.7. Já as versões das bibliotecas utilizadas são:

- `pandas`: 2.2.2
- `numpy`: 1.26.4
- `matplotlib`: 3.9.2
- `seaborn`: 0.13.2
- `sklearn`: 1.5.1
- `pickle`: 4.0
