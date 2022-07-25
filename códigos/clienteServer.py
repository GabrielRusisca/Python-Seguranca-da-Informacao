# Se conecta com o cliente UDP
# Primeiro rodamos o servidor e depois o cliente UDP
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print('Socket Criado com Sucesso')

host = 'localhost'
port = 5432
s.bind((host, port)) # conecta o cliente e o servidor
mensagem = 'Servidor: Olá, Cliente e aí, beleza?'
cont = 0
while True:
    dados, end = s.recvfrom(4096) # Recebe mensagem do cliente e salva seu endereço
    if dados:
        cont += 1
        msg = f'Server Log: {cont}'
        print(msg)
        print(f'Cliente: {dados.decode()}')
        print('Servidor enviando mensagem...')
        print(mensagem)
        print()
        s.sendto((f'{msg}\n').encode() + mensagem.encode(), end)
