import hashlib

string = input('Digite o texto a ser gerado a hash: ')

while True:
    try:
        menu = input("""#### MENU - ESCOLHA O TIPO DE HASE ####
1) MD5
2) SHA1
3) SHA256
4) SHA512
Digite o número do hash desejado: """)
        if int(menu) in [1, 2, 3, 4]:
            menu = int(menu)
            break
        raise ValueError
    except ValueError:
        print('\nEscreva direito\n')


if menu == 1:
    hash = 'md5'
elif menu == 2:
    hash = 'sha1'
elif menu == 3:
    hash = 'sha256'
else:
    hash = 'sha512'

resultado = hashlib.new(hash)
resultado.update(string.encode('utf-8'))

print(f'O hash {hash.upper()} da string é: ', resultado.hexdigest())