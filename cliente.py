import socket
import struct

# criando um socket UDP (Familia de endereços 'AF_INET' indica endereço IPV4
#  e 'SOCK_DGRAM' indica que o socket irá usar protocolo UDP)
socket_udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# configurando a porta que os dados serão enviados
endereco = ('localhost', 5000)

#configurando a porta e IP do cliente
endereco_cliente = ('localhost', 7000)
socket_udp.bind(endereco_cliente)

# enviando dados para o servidor utilizando a biblioteca "struct"
# a struct empacota a string enviada (dado que desejamos processar no servidor) em um objeto de 50 bytes
#para que ela possa ser enviada para o servidor
input = input("Digite alguma coisa: ")
dado = struct.pack('!50s', input.encode('utf-8'))
socket_udp.sendto(dado, endereco)

# recebendo a resposta do servidor utilizando o método recvfrom do socket
dados_recebidos, endereço_servidor = socket_udp.recvfrom(1024)

# processando a resposta do servidor utilizando o decode para 
# decodificar uma sequencia de bytes recebidas pelo servidor em
# uma string legível
resposta = dados_recebidos.decode('utf-8')

print('Resultado do processamento: ', resposta)

# fechando o socket
socket_udp.close()