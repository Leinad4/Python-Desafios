# NESTED FUNCTIONS E NONLOCAL
def tabuada():
    n = int(input("Dígite um número: "))
    def const():
        nonlocal n # Avisa que a variável 'n' foi criada na função tabuada
        c = 1
        while c <= n:
            print(f"Tabuada do número {c}")
            for i in range(1, 11):
                print(f"{c} x {i} = {c*i}")
            c += 1
    return const()
tabuada()