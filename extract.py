import requests
import zipfile
import io


# Como não é o objeto do desafio deixo aqui parte do processo de desenvolvimento para evoluções posterior

print("URL")
# URL de leitura do arquivo fonte
url = "https://quilted-neptune-7eb.notion.site/Teste-Engenheiro-de-Dados-73960f79a28b479d894d622a226ffa1a"
print("URL")

# Aqui baixando o arquivo utilizando a lib requests
# Caso não tenha a lib pode ser baixado através do 
# comando "pip install request"
response = requests.get(url)
print("response", response)


# Validando acesso a url
if response.status_code == 200:
    # Extração do arquivo    
    z = zipfile.ZipFile(io.BytesIO(response.content))
    z.extractall()
    print("Arquivo Baixado com sucesso")
else:
    print("Falha ao Baixar o arquivo. :.(")



