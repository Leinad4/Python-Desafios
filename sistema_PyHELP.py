def titulo(msg):
    t = len(msg) + 4
    print('~' * t)
    print(f' {msg}')
    print('~' * t)
def ajuda(com):
    help(com)
comando = ''
while True:
    titulo('SISTEMA DE AJUDA PyHELP')
    comando = str(input("PyHELP> "))
    if comando.upper() == 'EXIT':
        break
    else:
        ajuda(comando)
titulo('ATÉ LOGO')

