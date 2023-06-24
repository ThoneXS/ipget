import requests
from bs4 import BeautifulSoup

def analisar_diretorios(url):
    response = requests.get(url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        
        links = soup.find_all('a')
        
        for link in links:
            href = link.get('href')
             
            if href.endswith('/'):
                print(href)
    else:
        print('Falha ao acessar o site.')

# Exemplo de uso
url = input('Digite o nome do site:' )
analisar_diretorios(url)
