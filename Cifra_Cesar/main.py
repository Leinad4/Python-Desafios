from time import sleep
from sistema import *
while True:
    txt = bug('1.Criptografar \n2.Descriptografar \n3.Sair')
    if txt == 1:
        msg = str(input('Escreva a sua messagem: '))
        chave = bug_chave('Chave: 1-25: ')
        print(f'Cesar criptografa: {cript(msg, chave)}')
        sleep(2)
        
    elif txt == 2:
        msg = str(input('Escreva a messagem criptografada: '))
        chave = bug_chave('Chave: 1-26: ')
        print(f'Cesar descriptografa: {descript(msg, chave)}')
        sleep(2)
    elif txt == 3:
        print('Cesár diz tchau!')
        break







