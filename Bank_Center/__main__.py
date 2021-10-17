from sistema_banco import *
from front import *
from time import sleep
a = Interface()
while True:
    a.mostrando()
    opc = int(input('Qual é a sua opção: '))
    if opc == 1:
        q = float(input('Depositando R$: '))
        a.deposito(q)
    elif opc == 2:
        s = float(input('Saque R$: '))
        a.saque(s)
    elif opc == 3:
        e = float(input('Emprestimo R$: '))
        a.pedindo(e)
    elif opc == 4:
        print('Finalizando sessão...')
        break
    else:
        print('Digite apenas as opções do menu')
        sleep(2)
