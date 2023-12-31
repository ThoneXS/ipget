import socket

def analisar_portas(url, portas):
    for porta in portas:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(2)  
        
        try:
            resultado = sock.connect_ex((url, porta))
            
            if resultado == 0:
                print(f"A porta {porta} está aberta")
            else:
                print(f"A porta {porta} está fechada")
        except socket.error:
            print(f"Ocorreu um erro ao conectar à porta {porta}")
        
        sock.close()

# Exemplo de uso
url = input('Digite o nome do site:' )
portas = [80, 443, 8080]
analisar_portas(url, portas)

