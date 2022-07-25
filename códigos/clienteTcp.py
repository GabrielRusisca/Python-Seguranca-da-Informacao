import socket # Biblioteca que nos conecta com a placa de rede e o OS
import sys

def __main__() -> None:
    """Cria uma conexão socket e verifica se o cliente TCP se conectou corretamente (de acordo com o princípio de integridade) ao Host por uma determinada Porta"""
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0) # s = socket.socket(socket.AF_INET "IPV4", socket.SOCK_STREAM "TCP", 0)
    except socket.error as e:
        print('A conexão falhou')
        print(f'Erro: {e}')
        sys.exit()

    print('Socket criado com sucesso!')

    hostAlvo = input('Digite o Host ou Ip a ser conectado: ')
    portaAlvo = input('Digite a porta TCP a ser conectada: ')

    try:
        s.connect((hostAlvo, int(portaAlvo)))
        print(f'Cliente TCP conectado com Sucesso no Host: {hostAlvo} e na Porta: {portaAlvo}')
        s.shutdown(2)
    except socket.error as e:
        print(f'A conexão falhou devido ao Erro: {e}')
        sys.exit()

if __name__ == '__main__':
    __main__()