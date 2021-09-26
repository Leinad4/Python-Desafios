def leiadinheiro(msg):
    valido = False
    while not valido:
        valor = str(input(f"{msg}")).replace(',','.').strip()
        if valor.isalpha() or valor == '':
            print(f"\033[0;31m[ERRO] {valor} não é válido!\033[m")
        else:
            valido = True
            return float(valor)
