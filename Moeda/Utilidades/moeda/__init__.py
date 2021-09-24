def metade(n=0, f=False):
    '''
    metade(n=0, f=False):
        -> Recebe um valor que será dividido por 2
        Para n: Um valor a ser recebido
        Para f: True para formatar a moeda.
                False para não formatar a moeda. 
    '''
    m = n / 2
    return m if f is False else moeda(m)
def dobro(n=0, f=False):
    '''
    dobro(n=0, f=False):
        -> Recebe um valor que será multiplicado por 2
        Para n: Um valor a ser recebido
        Para f: True para formatar a moeda
                False para não formatar a moeda
    '''
    d = n * 2
    return d if f is False else moeda(d)
def aumento(n=0, taxa=0, f=False):
    '''
    aumento(n=0, taxa=0, f=False):
        -> Recebe 2 valores, o preço e a taxa
        Para n: Um valor a ser recebido
        Para taxa: Um porcentual a ser recebido
        Para f: True para formatar a moeda
                False para não formatar a moeda 
    '''
    a = n + (n * taxa / 100)
    return a if f is False else moeda(a) 
def reducao(n=0, r=0, f=False):
    r = n - (n * r / 100)
    return r if f is False else moeda(r)
def moeda(v=0, moeda="R$"):
    return f'{moeda:<3}{v:5.2f}'.replace(".",",")

def titulo(msg):
    
    print("~" * 30)
    print(f" {msg:^30}")
    print("~" * 30)

def resumo(n=0, a=0, r=0):
    '''
    resumo(n=0, a=0, r=0):
        -> Passando os três parâmetros para o resumo funcionar 
        Para n: O preço
        Para a: O aumento em porcentagem
        Para r: A redução em porcentagem 
    '''
    titulo("Resumo do Valor")
    print(f"Preço analisado: \t{moeda(n)}")
    print(f"Dobro do preço: \t{dobro(n, True)}")
    print(f"Metade do preço: \t{metade(n, True)}")
    print(f"{a}% de aumento: \t{aumento(n, a, True)}")
    print(f"{r}% de redução: \t{reducao(n, r, True)}")

