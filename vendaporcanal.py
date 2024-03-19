import pandas as pd
from memory_profiler import profile

# Declarações de variávei e parametros de funcionalidades do Chunk e Path
# Caminho escolhido pelo dev para identificar a origem do arquivo a ser utilizado pelo programa
caminho_arquivo  = './raw/vendas.csv' 

# Definição de números de linhas a serem lidas por bloco.
chunksize = 10000

# Criando DataFrame tendo como fonte de dados arquivo cvs
# Definindo chunk nesse Dataframe
df_vendas = pd.read_csv(caminho_arquivo, chunksize=chunksize)

lista_prod_vendido       = []
lista_prod_vendido_canal = []

@profile
def item_canal_vendas():
    for chucks in df_vendas:
        #print(chuck)
        lista_prod_vendido.append(chucks.groupby(['Item Type','Sales Channel'])['Units Sold'].sum().astype(float))


    # Após a coleta dos Chunk vamos iterar sobre a lista e criar uma lista com itens saneados e 
    # criiar um DataFrame novo para agruparmos depois os multiplos DataFrame da Lista
    for maior_venda in lista_prod_vendido:    
        for index, value in maior_venda.items():        
            item_type, sales_channel = index        
            lista_prod_vendido_canal.append((item_type, sales_channel, value))

    # Criar o DataFrame com as dados saneados
    df_prod_mais_vendido_canal = pd.DataFrame(lista_prod_vendido_canal, columns=['ItemType', 'SalesChannel', 'UnitsSold'])


    return df_prod_mais_vendido_canal.groupby(['ItemType', 'SalesChannel'])['UnitsSold'].sum().astype(float)

df_pmvc_agg = item_canal_vendas()
print(df_pmvc_agg)

#2. Identifique o produto mais vendido em termos de quantidade e canal.