import requests
from bs4 import BeautifulSoup

def analisar_diretorios(url):
    # Faz a requisição GET para a URL fornecida
    response = requests.get(url)
    
    # Verifica se a requisição foi bem-sucedida (código 200)
    if response.status_code == 200:
        # Cria o objeto BeautifulSoup com o conteúdo HTML retornado
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Encontra todos os links no conteúdo HTML
        links = soup.find_all('a')
        
        # Itera sobre os links encontrados
        for link in links:
            # Obtém o valor do atributo 'href' de cada link
            href = link.get('href')
            
            # Verifica se o link é um diretório (termina com '/')
            if href.endswith('/'):
                # Imprime o diretório encontrado
                print(href)
    else:
        # Imprime uma mensagem de erro caso a requisição falhe
        print('Falha ao acessar o site.')

# Exemplo de uso
url = 'https://www.pt.org.br'
analisar_diretorios(url)
