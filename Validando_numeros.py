def leia(n):
    while True:
        num = str(input(n))
        if num.isnumeric() == True:
            num = int(num)
            return num
        elif num.isnumeric != True:
            print("\033[31m[ERRO] dígite um número inteiro válido\033[m")
            continue
nu = leia("Dígite um número: ")
print(f"Você acabou de digitar o número {nu}")
