from time import sleep

def leia(msg):
    valido = False
    while not valido:
        try:
            num = int(input(msg))
        except (TypeError, ValueError):
            print('\033[0;31mDígite um número inteiro válido\033[m')
        else: 
            return num

def linha(tam=30):
    print('-' * tam)

def titulo(msg):
    '''
    titulo(msg):
        -> Será passado um texto a ser formatado
    '''
    linha()
    print(msg.center(30))
    linha()
   
def opc(lista):
    '''
    opc(lista):
        -> Recebe uma lista com as opções do menu que serão formatadas 
    '''
    c = 1
    for i in lista:
        print(f'\033[0;32m{c}\033[m - \033[0;34m{i}\033[m')
        c += 1
    linha()

def menu(msg):
    '''
    menu(msg):
        -> Recebe as opções de execução do menu principal
        -> Verifica se ocorrerá algum erro de digitação 
    '''
    valido = False
    while not valido:
        titulo('MENU PRINCIPAL')
        opc(msg)
        try:
            r = int(input("\033[0;33mSua opção:\033[m "))
        except (ValueError, TypeError):
            print('\033[0;31mDígite um valor inteiro válido!\033[m')
            sleep(2)
            continue
        else:
            return r