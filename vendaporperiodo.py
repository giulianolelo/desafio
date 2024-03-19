import pandas as pd

# Declarações de variávei e parametros de funcionalidades do Chunk e Path
# Caminho escolhido pelo dev para identificar a origem do arquivo a ser utilizado pelo programa
caminho_arquivo  = './raw/vendas.csv' 

# Definição de números de linhas a serem lidas por bloco.
chunksize = 100

# Criando DataFrame tendo como fonte de dados arquivo cvs
# Definindo chunk nesse Dataframe
df_vendas = pd.read_csv(caminho_arquivo, chunksize=chunksize)

lista_prod_vendido       = []
lista_prod_vendido_canal = []


for chucks in df_vendas:
    #print(chuck)
    lista_prod_vendido.append(chucks.groupby(['Item Type','Ship Date'])['Total Revenue'].mean().astype(float))


# Após a coleta dos Chunk vamos iterar sobre a lista e criar uma lista com itens saneados e 
# criiar um DataFrame novo para agruparmos depois os multiplos DataFrame da Lista
for maior_venda in lista_prod_vendido:    
    for index, value in maior_venda.items():        
        item_type, sales_channel = index        
        lista_prod_vendido_canal.append((item_type, sales_channel, value))

# Criar o DataFrame com as dados saneados e limpos 
df_prod_mais_vendido_canal = pd.DataFrame(lista_prod_vendido_canal, columns=['ItemType','ShipDate', 'TotalRevenue'])
df_prod_mais_vendido_canal['ShipDate'] = pd.to_datetime(df_prod_mais_vendido_canal['ShipDate'])

df_pmvc_agg = df_prod_mais_vendido_canal.groupby(['ItemType', df_prod_mais_vendido_canal['ShipDate'].dt.to_period('M')])['TotalRevenue'].mean().astype(float)

print(df_pmvc_agg)
