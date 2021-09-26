salto = list()
def linha(tam=30):
    print('-' * tam)

def inicio(nome):
    '''
    inicio(nome):
        -> Função que receberá o nome do atleta e suas 5 pontuação
    '''
    linha()
    n = str(input(nome))
    for i in range(5):
        num = float(input(f'{i+1}º salto: '))
        salto.append(num)
    meio(n, salto )

def meio(nome, pontos):
    '''
    meio(nome, pontos):
        Para nome: Só recebemos, mas não utilizamos.
        Para pontos: A partir dela será retirado: maior e menor pontuação e a media 
    '''
    soma = media = 0
    maior = max(pontos)
    menor = min(pontos)
    for i in pontos:
        if maior != i or menor != i:
            soma += i
    media = soma / 5
    fim(nome, media, maior, menor, pontos)

def fim(n, med, mai, man, pont):
    '''
    fim(n, med, mai, man, pont):
    Para n: Nome do atleta 
    Para med: A média final do atleta
    Para mai e man: Maior e Menor pontuação
    Para pont: Estão armazenados os pontos dos saltos
    '''
    c = 1
    linha()
    print(f'Atleta: {n}')
    print('Pontuação : ', end="")
    for i in pont: 
        print(f'{i}', end="") # Mostra os pontos dos saltos em sequência
        if c < 5:
            print('-', end="")
        c += 1
    print(f'\nMaior pontuação: {mai} \nMenor pontuação: {man}')
    print(f'Média final: {med}')
    linha()




    



        