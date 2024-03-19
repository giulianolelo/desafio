import pandas as pd
from memory_profiler import profile

# Declarações de variávei e parametros de funcionalidades do Chunk e Path
# Caminho escolhido pelo dev para identificar a origem do arquivo a ser utilizado pelo programa
caminho_arquivo  = './raw/vendas.csv' 

# Definição de números de linhas a serem lidas por bloco.
chunksize = 10000

# Criando DataFrame tendo como fonte de dados arquivo cvs
# Definindo chunk nesse Dataframe
df_vendas = pd.read_csv(caminho_arquivo)

lista_prod_vendido       = []
lista_prod_vendido_canal = []
@profile
def item_canal_vendas():
    
    return df_vendas.groupby(['Item Type','Sales Channel'])['Units Sold'].sum().astype(float)

df_resultado = item_canal_vendas()
print(df_resultado)

#2. Identifique o produto mais vendido em termos de quantidade e canal.