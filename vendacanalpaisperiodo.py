import pandas as pd
from memory_profiler import profile

# Declarações de variávei e parametros de funcionalidades do Chunk e Path
# Caminho escolhido pelo dev para identificar a origem do arquivo a ser utilizado pelo programa
caminho_arquivo  = './raw/vendas.csv'

# Definição de números de linhas a serem lidas por bloco.
chunksize = 1000 # Registros

# Váriaveis de parametros utilizadas nas chamadas das agregações
coluna_chave01 = None
coluna_chave02 = None
coluna_valor   = None
operacao       = None 


# Criando DataFrame tendo como fonte de dados arquivo cvs
# Definindo chunk nesse Dataframe
df_vendas = pd.read_csv(caminho_arquivo, chunksize=chunksize)

# Lista para armazenar os resultados
lista_prod_vendido = []


# Função para tratar as agregações
@profile
def calcular_agregacoes_vendas(df_chunk, coluna_chave01, coluna_chave02, coluna_valor, operacao):
    if operacao == 'mean': # PAra média dos valores
        return df_chunk.groupby([coluna_chave01, coluna_chave02])[coluna_valor].mean().astype(float)
    elif operacao == 'sum': # Para soimar/agregar
        return df_chunk.groupby([coluna_chave01, coluna_chave02])[coluna_valor].sum().astype(float)    
    else:
        raise ValueError("Operação não suportada. Escolha entre 'mean' ou 'sum'.")
    
# Função para diminuir código repetido para as agregações criadas nesse desenvolvimento
# e para os próximos.
@profile
def chunk_loop(coluna_chave01, coluna_chave02, coluna_valor, operacao):
# Iterar sobre os chunks
    for chunk in pd.read_csv(caminho_arquivo , chunksize=chunksize):
        agregacao_vendas = calcular_agregacoes_vendas(chunk, coluna_chave01, coluna_chave02, coluna_valor, operacao)
        lista_prod_vendido.append(agregacao_vendas)
        del chunk

    return pd.concat(lista_prod_vendido)


# Controle das chamadas das agregações utilizando Chunk
def main():  
    parameter = 0 
    for i in range(0,1,1): 
        if parameter == 0:
            # Colunas que você deseja selecionar
            coluna_chave01 = 'Item Type'
            coluna_chave02 = 'Ship Date'
            coluna_valor   = 'Total Revenue'

            # Operação desejada (mean, sum)
            operacao = 'mean'

            resultado_final = chunk_loop(coluna_chave01 ,coluna_chave02 ,coluna_valor ,operacao)
                        
            print(resultado_final)
            parameter += 1

        elif parameter == 1:
            # Colunas que você deseja selecionar         
            coluna_chave01 = 'Country'
            coluna_chave02 = 'Region'
            coluna_valor   = 'Total Revenue'

            # Operação desejada (mean, sum)
            operacao = 'sum'

            resultado_final = chunk_loop(coluna_chave01 ,coluna_chave02 ,coluna_valor ,operacao)
            
            print(resultado_final)
         
            parameter += 1
        elif parameter == 2:
            # Colunas que você deseja selecionar         
            coluna_chave01 = 'Item Type'
            coluna_chave02 = 'Sales Channel'
            coluna_valor   = 'Units Sold'

            # Operação desejada (mean, sum)
            operacao = 'sum'

            resultado_final = chunk_loop(coluna_chave01 ,coluna_chave02 ,coluna_valor ,operacao)
            
            print(resultado_final)
            print("Acabou")
            parameter += 1

# Execução do programa
if __name__ == "__main__":
    main()