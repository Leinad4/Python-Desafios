from time import sleep
def contador():
    print("-=" * 20)
    print("Contagem de 1 até 10 de 1 em 1")
    for i in range(1, 10+1):
        print(f"{i}", end="-")
        sleep(1)
    print("Fim!")
    print("-=" * 20)
    print("Contagem de 10 até 0 de 2 em 2")
    for i in range(10, -1, -2):
        print(f"{i}", end="-")
        sleep(1)
    print("Fim!")
    print("-=" * 20)
    print("Agora é a sua vez de personalizar a contagem!")
    i = int(input("Inicio: "))
    f = int(input("Fim: "))
    p = int(input("Passo: "))
    if i < f:
        for i in range(i, f+1, p):
            print(f"{i}", end="-")
            sleep(1)
        print("Fim!")
    if i > f:
        for j in range(i, f-1, -p):
            print(f"{j}", end="-")
            sleep(1)
        print("Fim!")
contador()
