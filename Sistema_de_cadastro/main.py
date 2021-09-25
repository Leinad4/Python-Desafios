from lib.interface import *
from lib.arquivo import *

arquivo = 'leinad.txt'

if not existe(arquivo):
    criando(arquivo)
    

from time import sleep
while True:
    opc = menu(['TODOS OS CADASTROS', 'NOVO CADASTRO', 'SAIR'])
    if opc == 1:
        mostrar(arquivo)
    elif opc == 2:
        titulo('NOVO CADASTRO')
        n = str(input('Nome: '))
        i = leia('Idade: ')
        cadastro(arquivo, n, i)
       
    elif opc == 3:
        titulo('SAINDO DO SISTEMA...')
        break
    else:
        print('\033[0;31mNão tem essa opção\033[m')
    sleep(2)
