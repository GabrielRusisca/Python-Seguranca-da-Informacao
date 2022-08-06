import hashlib as hs

arquivo1 = 'códigos\\a.txt'
arquivo2 = 'códigos\\b.txt'

hash1 = hs.sha256() # O professor utilizou o hs.new('ripemd160') na aula
hash2 = hs.sha256()

arquivo1_dados = open(arquivo1, 'rb').read()
arquivo2_dados = open(arquivo2, 'rb').read()

hash1.update(arquivo1_dados)
hash2.update(arquivo2_dados)
print('-'*30)
if hash1.digest() != hash2.digest():
    print(f'O arquivo: {arquivo1} é diferente do arquivo: {arquivo2}')
else:
    print(f'Os arquivos: {arquivo1} e {arquivo2} são iguais!')
print()
print(f'O hash do arquivo {arquivo1} (em número hex) é: {repr(hash1.hexdigest())}')
print()
print(f'O hash do arquivo {arquivo2} (em número hex) é: {repr(hash2.hexdigest())}')
print('-'*30)