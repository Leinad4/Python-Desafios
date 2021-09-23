def metade(n=0, f=False):
    m = n / 2
    return m if f is False else moeda(m)
def dobro(n=0, f=False):
    d = n * 2
    return d if f is False else moeda(d)
def aumento(n=0, taxa=0, f=False):
    a = n + (n * taxa / 100)
    return a if f is False else moeda(a) 
def moeda(v=0, moeda="R$"):
    return f'{moeda:<3}{v:5.2f}'.replace(".",",")

