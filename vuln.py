import requests

def analisar_vulnerabilidades(url):
    dir_listing_url = url + '/directory_that_does_not_exist/'
    response = requests.get(dir_listing_url)
    
    if response.status_code == 200:
        print("O site permite listagem de diretórios.")
    else:
        print("O site não permite listagem de diretórios.")
    
    response = requests.head(url)
    sensitive_headers = ['Authorization', 'Set-Cookie', 'X-Frame-Options']
    
    for header in sensitive_headers:
        if header in response.headers:
            print(f"O header {header} está exposto no site.")
    
 
    sqli_payload = "' OR '1'='1"
    sqli_url = url + "/search?query=" + sqli_payload
    response = requests.get(sqli_url)
    
    if "error" in response.text:
        print("O site está vulnerável a ataques de injeção de SQL.")
    else:
        print("O site não está vulnerável a ataques de injeção de SQL.")

# Exemplo de uso
url = input('Digite o nome do site:' )
analisar_vulnerabilidades(url)
