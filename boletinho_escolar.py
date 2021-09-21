d = dict()
l = list()
opc = 0
def main():
    inicio()
def inicio():
    global opc
    while True:
        num = float(input("Dígite um número: "))
        l.append(num)
        while True:
            r = str(input("Quer continuar: [Y/N] ")).upper()[0]
            if r in "YN":
                break
            else:
                print("\033[0;31m[ERRO] somente Y ou N\033[m")
                continue
        if r in "N":
            break
    print("-=" * 20)
    print("[1] Somente estatistica de notas \n[2] Com a situação \n[3] Help ")
    print("-=" * 20)
    opc = int(input("Qual é a sua opção: "))
    if opc == 1:
        notas(l)
    if opc == 2:
        notas(l, sit=True)
    if opc == 3:
        help(notas)

def notas(*n, sit=False):
    """
    notas(*n, sit=False):
        -> Função que irá analisar a notas de uma sala de alunos
        Para *n: São as notas informadas pelo usuário
        Para sit(opcional): [True} para ver a situação da classe
                            [False] para não ver situação da classe  
            
    """
    global d, l
    total = 0
    media = soma = 0
    for i in l:
        soma += i
        total += 1
    media = soma / total
    d["Total"] = total
    d["Maior"] = max(l)
    d["Menor"] = min(l)
    d["Média"] = media
    if sit:
        if media <= 4:
            d["situação"] = "Ruim"
            return d
        elif media <= 6:
            d["situação"] = "Razoável"
            return d
        elif media <= 10:
            d["situação"] = "Boa" 
            return d
    else:
        return d

main()
if opc == 3:
    main()
else:
    print(d)
    



