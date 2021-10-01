from time import sleep
def titulo(msg, tam=20):
    print('-' * tam)
    print(msg)
    print('-' * tam)

def bug(msg):
    '''
    Função que verifica a legibilidade de entrada do usuário
    '''
    titulo(msg)
    while True:
        try:
            opc = int(input('Sua opção: '))  
        except (ValueError, TypeError):
            print('Somente valores inteiros')
            sleep(2)
        else:
            if opc >= 4 or opc <= 0:
                print('Somente 1 ou 3')
                sleep(2)
                continue
            else:
                return opc

def bug_chave(msg):
    '''
    -> Função de verificação do número da chave dígitado pelo usuário
    '''
    while True:
        try:
            chave = int(input(f'{msg}: '))
        except (TypeError, ValueError):
            print('Dígite um número inteiro válido')
            sleep(2)
        else:
            if chave <= 0 or chave > 26:
                print('Entre 1 e 25')
                sleep(2)
            else:
                return chave

def cript(msg, chave):
    '''
    cript(msg='', chave=0)
        -> msg: Mensagem que o usuário escreveu para ser criptografada
           chave: Número de vezes que uma letras da mensagem irá avançar
        -> A criptografia ocorrerá aos números, letras maiúsculas e minúsculas  

        -> EQUAÇÃO: (ord(i) + chave - 97) % 26 + 97
            -> ord(i): Valor referente a tabela ASCII
            -> 97: Referente ao caractere 'a' minúsculo
            -> ((d=100) + (chave=2) - 97) = 5 
            -> (5 % 26) = 5 
            -> (5 + 97) = 102 -> Referente ao caractere 'f' minúsculo 
        -> Do 'd' pulando 2 é igual a 'f'

    '''
    
    cifra = ''
    for i in msg:
        if i == chr(32):
            cifra += i
            continue
        if i.isnumeric():
            code = (ord(i) + chave - 48) % 10 + 48 
        elif i.isupper():
            code = (ord(i) + chave - 65) % 26 + 65
        elif i.islower():
            code = (ord(i) + chave - 97) % 26 + 97
        cifra += chr(code)
    return cifra

def descript(msg, chave):
    '''
    descript(msg, chave):
        -> msg: Mensagem que o usuário escreveu para ser descriptografada
           chave: Número de vezes que uma letra irá recuar
        -> A descriptografia ocorrerá aos números, letras maiúsculas e minúsculas 

        -> EQUAÇÃO: (ord(i) - chave - 97) % 26 + 97
            -> ord(i): Valor referente a tabela ASCII
            -> 97: Referente ao caractere 'a' minúsculo
            -> ((d=100) - (chave=2) - 97) = 1
            -> (1 % 26) = 1 
            -> (1 + 97) = 98 -> Referente ao caractere 'b' minúsculo 
        -> Do 'd' recuando 2 é igual a 'b'
    '''
    cifra = ''
    for i in msg:
        if i == chr(32):
            cifra += i
            continue
        if i.isnumeric():
            code = (ord(i) - chave - 48) % 10 + 48
        elif i.isupper():
            code = (ord(i) - chave - 65) % 26 + 65
        elif i.islower():
            code = (ord(i) - chave - 97) % 26 + 97
        cifra += chr(code)
    return cifra

