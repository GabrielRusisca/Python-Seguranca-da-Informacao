import os

print('#' * 60)
ip_ou_host = input('Digite o Ip ou host a ser verificado: ') # Podemos testar nosso conexão com o site do Google: www.google.com
num_pings = input('Quantos teste deseja fazer (recomendado: mais que 4): ') 
print('-' * 60)
os.system(f'ping -n {num_pings} {ip_ou_host}')
print('-' * 60)