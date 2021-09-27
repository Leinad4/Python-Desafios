from suspeito import *
pessoa = investigar('Nome do suspeito: ')
if pessoa == 2:
    print('SUSPEITO')
elif pessoa == 3 or pessoa == 4:
    print('CUMPLICE')
elif pessoa == 5:
    print('ASSASSINA(O)')
else:
    print('INOCENTE')
linha()
