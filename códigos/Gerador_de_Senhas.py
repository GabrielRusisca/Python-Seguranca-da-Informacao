import random, string # Vamos usar o random para gerar senhas, lembrando apenas que ele não é um CSPRNG e apenas um PRNG

tamanho = int(input('Digite o tamanho da senha desejada: '))

chars = string.ascii_letters + string.digits + '!@#$%¨&*()_+-=§°/?;:\|]º}~^[{ª´`.>,<'

rnd = random.SystemRandom() # criou um seed

senha_lista = [rnd.choice(chars) for i in range(tamanho)]

senha = ''.join(senha_lista)

print(senha)

