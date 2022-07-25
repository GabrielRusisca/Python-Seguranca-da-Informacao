# Se conecta com o server do código clienteServer
import socket


s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0) # socket.socket(socket.AF_INET "IPV4", socket.SOCK_DGRAM "UDP", 0)

print('Cliente Socket Criado com Sucesso!!!')

host = 'localhost'
porta = 5433
mensagem = 'Olá servidor, tudo bem?'
try:
    print(f'Cliente: {mensagem}')
    s.sendto(mensagem.encode(), (host, 5432)) # Envia mensagem para a porta 5432 que o server estará ouvindo

    dados, servidor = s.recvfrom(4096) # Recebe mensagem do server e salva seu endereço, o qual é igual a porta no caso
    dados = dados.decode()
    print(dados)
finally:
    print('Cliente: Fechando a Conexão')
    s.close()
