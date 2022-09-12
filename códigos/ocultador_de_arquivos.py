import ctypes

atributo_ocultar = 0x02

arq_ou_pasta = (input(r'Digite o caminho da pasta ou arquivo a ser ocultado, exemplo: C:\Users\grusi\Gabriel\Programacao\MeusProjetos\Python-Seguranca-da-Informacao\códigos\arquivo_ocultado.txt: '))
print()
retorno = ctypes.windll.kernel32.SetFileAttributesW(arq_ou_pasta, atributo_ocultar)

if retorno:
    print('Arquivo foi ocultado')
else:
    print('Arquivo não foi ocultado')