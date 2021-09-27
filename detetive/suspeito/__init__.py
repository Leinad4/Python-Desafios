from time import sleep
def linha(t=30):
    print('-' * t)

def investigar(msg):
    positivo = 0
    p = ['Telefonou para a vítima:', 'Esteve no local do crime:', 'Mora perto da vítima:', 'Devia para a vítima', 'Já trabalhou com a vítima:']
    nome = str(input(msg)).upper()
    linha()
    print(f'Interrogando: {nome}')
    linha()
    for i in range(5):
        while True:
            pergunta = str(input(f'{p[i]} [S/N] ')).upper()[0]

            if pergunta not in "SN":
                print('\033[0;31mApenas S ou N\033[m')
                continue
            else:
                if pergunta in 'S':
                    positivo += 1
                break

    linha()
    print('ANALISANDO EVIDÊNCIAS...')
    linha()
    sleep(2)
    print(f'SUSPEITO {nome}: ', end='')
    return positivo
    