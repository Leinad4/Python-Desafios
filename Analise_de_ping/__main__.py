from sistema import *
from time import sleep
a = Aplicar()
while True:
    print('-' * 60)
    a.imagem()
    try:
        op = int(input('user$ '))
    except ValueError:
        print('\033[1;31mDígite um valor inteiro válido\033[m') 
        sleep(1)
    else:
        if op != 6:
            a.opc(op)
            time.sleep(2)
        else:
            break
print('-' * 60)
print('ENCERRANDO PROGRAMA...')
    