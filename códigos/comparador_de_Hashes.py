import hashlib as hs

arquivo1 = 'códigos\\a.txt'
arquivo2 = 'códigos\\b.txt'

hash1 = hs.new('sha256') # O professor utilizou o hs.new('ripemd160') na aula. Já testei e hs.sha256() == hs.new('sha256')
hash2 = hs.sha256()

arquivo1_abre = open(arquivo1, 'rb')
arquivo1_dados = arquivo1_abre.read()
arquivo1_abre.close()
arquivo2_abre = open(arquivo2, 'rb')
arquivo2_dados = arquivo2_abre.read()
arquivo2_abre.close()


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

