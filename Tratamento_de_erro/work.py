def inteiro(msg):
    valido = False
    while not valido:
        try:
            num = int(input(f'{msg}'))
        except (TypeError, ValueError):
            print('\033[0;31mDígite um número inteiro válido\033[m')
            continue
        except (KeyboardInterrupt):
            print("\n\033[0;33mO usuário não quis dígitar\033[m")
            return 0
        else:
            valido = True
            return num

def real(msg):
    valido = False
    while not valido:
        try:
            num2 = float(input(f'{msg}'))
        except (ValueError, TypeError):
            print('\033[0;31mDígite um valor real válido!\033[m')
            continue
        except (KeyboardInterrupt):
            print(f'\n\033[0;33mO usuário não quis digitar\033[m')
            return 0
        else:
            valido = True
            return num2

            