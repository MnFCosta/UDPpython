import socket
import struct

# criando um socket UDP (Familia de endereços 'AF_INET' indica endereço IPV4
#  e 'SOCK_DGRAM' indica que o socket irá usar protocolo UDP)
socket_udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# configurando a porta (localhost) e o endereço IP do servidor (5000)
endereco = ('localhost', 5000)
socket_udp.bind(endereco)

print(f"Servidor rodando no endereço {endereco}: Esperando por dados do cliente.....")
#while loop que irá processar os dados recebidos do cliente
while True:
    # recebendo dados do cliente com um buffer máximo de 1024 bytes
    dados_recebidos, endereco_cliente = socket_udp.recvfrom(1024)
    print(f"Dados recebidos do cliente no endereço {endereco_cliente}, iniciando processamento...")
    # processando os dados recebidos
    dados_processados = dados_recebidos[::-1].decode('utf-8') # inverte a string
    
    # enviando a resposta de volta para o cliente
    data = struct.pack('!50s', dados_processados.encode('utf-8'))
    socket_udp.sendto(data, endereco_cliente)
