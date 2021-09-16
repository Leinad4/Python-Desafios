saldo = 0

def main():
    conta()
def conta():
    global saldo
    print("""
    +=====================================+
    +           \033[32mBANCO DO BARRIL\033[m           +
    +=====================================+
    + (1) DEPOSITAR (2) RETIRAR (3) EXIT  +
    +=====================================+
    """)
    opc = int(input("O que você deseja: "))
    if opc == 1:
        depositando()
    if opc == 2:
        retirando()
    if opc == 3:
        termino()
def depositando():
    global saldo
    while True:
        quanto = float(input("Valor do deposito:R$ "))
        saldo += quanto
        print(f"""
        +========================+
              SALDO [{saldo:5.2f}]         
        +========================+
        + (1) DEPOSITO  (2) EXIT +
        +========================+
        """)
        r = int(input("O que você deseja: "))
        if r == 2:
            break
    conta()
def retirando():
    global saldo
    while True:
        print(f"""
        +============================+
                SALDO [{saldo:5.2f}]
        +============================+
        """)
        retirar = float(input("Valor a ser retirado: "))
        saldo -= retirar

        if saldo <= 0:
            break
        
        print("""
        +======================+
        + (1) RETIRAR (2) EXIT +
        +======================+
        """)
        r = int(input("O que você deseja: "))
        if r == 2:
            break
    conta()
def emprestimo():
    global saldo
    r = str(input("Aceita um emprestimo: Y/n ")).upper()[0]
    if r in 'Y':
        i = float(input("De quanto é o emprestimo:R$ "))
        saldo += i
        conta()
    if r in "N":
        conta()
def termino():
    print("SESSÃO ENCERRADA")
main()
        



