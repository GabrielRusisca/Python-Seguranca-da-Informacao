from threading import Thread
from time import sleep

def carro(velocidade, piloto):
    trajeto = 0
    while trajeto <= 100:
        trajeto += velocidade
        sleep(0.25)
        print(f'Carro: {piloto} e {trajeto}\n')


t_carro1 = Thread(target=carro, args=[5, 'Gabriel'])
t_carro2 = Thread(target=carro, args=[10, 'Shirley'])

t_carro1.start()
t_carro2.start()