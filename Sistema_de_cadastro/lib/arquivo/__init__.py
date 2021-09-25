from lib.interface import * 

def existe(arquivo):
    '''
    existe(arquivo):
        -> Verifica se o arquivo existe 
    '''
    try:
        o = open(arquivo, 'rt')
        o.close()
    except (FileNotFoundError):
        print('\033[0;31mArquivo não existe\033[m')
    else:
        return o

def criando(arquivo):
    '''
    criando(arquivo):
        -> CSerá criado o arquivo para o cadastro
    '''
    try:
        o = open(arquivo, 'wt+') # wt+ -> escreva ou crie o arquivo
        o.close()
    except (FileNotFoundError):
        print("\033[0;31mHouve um erro ao criar o arquivo\033[m")
        
    else:
        return o

def mostrar(arquivo):
    '''
    mostrar(arquivo):
        -> Será aberto o arquivo com seus respectivos cadastros
    '''
    try:
        o = open(arquivo, 'rt')
    except (FileNotFoundError):
        print('\033[0;31mNão foi possível abrir o arquivo\033[m')
    else:
        titulo('TODOS OS CADASTROS')
        for i in o:
            dado = i.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<20}{dado[1]:>3} anos')
    finally:
        o.close()

def cadastro(arquivo, nome='Desconhecido', idade=0):
    try:
        o = open(arquivo, 'at')
    except:
        print('Houve um erro ao abrir o arquivo')
    else:
        try:
            o.write(f'{nome};{idade}\n')
        except:
            print('Houve um erro ao adiciona o novo cadastro')
        else:
            print(f'{nome} adicionado com sucesso')
            o.close()

