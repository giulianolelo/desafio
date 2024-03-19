import pandas as pd

# Declarações de variávei e parametros de funcionalidades do Chunk e Path
# Caminho escolhido pelo dev para identificar a origem do arquivo a ser utilizado pelo programa
caminho_arquivo  = './raw/vendas.csv' 

# Definição de números de linhas a serem lidas por bloco.
chunksize = 10000

# Criando DataFrame tendo como fonte de dados arquivo cvs
# Definindo chunk nesse Dataframe
df_vendas = pd.read_csv(caminho_arquivo, chunksize=chunksize)

lista_prod_vendido             = []
lista_prod_vendido_pais_regiao = []

for chucks in df_vendas:
    #print(chuck)
    lista_prod_vendido.append(chucks.groupby(['Country', 'Region'])['Total Revenue'].sum().astype(float))


# Após a coleta dos Chunk vamos iterar sobre a lista e criar uma lista com itens saneados e 
# criiar um DataFrame novo para agruparmos depois os multiplos DataFrame da Lista
for maior_venda in lista_prod_vendido:    
    for index, value in maior_venda.items():        
        Region, Country = index        
        lista_prod_vendido_pais_regiao.append((Region, Country, value))

# Criar o DataFrame com as dados saneados
df_prod_mais_vendido_pais_regiao = pd.DataFrame(lista_prod_vendido_pais_regiao, columns=['Country', 'Region', 'TotalRevenue'])

df_pmvpr_agg = df_prod_mais_vendido_pais_regiao.groupby(['Country', 'Region'])['TotalRevenue'].sum().astype(float)

print(df_pmvpr_agg)

#3. Determine qual pais e região teve o maior volume de vendas (em valor).