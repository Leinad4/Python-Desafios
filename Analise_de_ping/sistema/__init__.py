import os
import time
# Classe onde está todas as funcionalidades de pings 
class Host:
    def __init__(self):
        pass
    def mostrar(self, valor):
        print('-' * 60)
        return os.system(f'ping {valor}') # Efetuará o ping ao endereço IP passado pelo usuário
    def mostrar_todos(self):
        # Realizará pings para todos os IPs gravados no arquivo "host.txt"
        with open('host.txt') as file:
            a = file.read()
            a = a.splitlines()
            for i in a:
                print('-' * 60)
                os.system(f'ping {i}')
                time.sleep(2)
    def adicionar(self, ip):
        # Será adicionado os novos endereços IPs no arquivo "host.txt"
        try:
            a = open('host.txt', 'at')
        except FileNotFoundError:
            print('Houve um problema com o arquivo')
        else:
            a.write(f'{ip}\n')
        finally:
            a.close()
    def lista(self):
        # Apresenta ao usuário todos os endereços IPs registrados no arquivo "host.txt"
        print('-' * 60)
        print('IPs ADICIONADOS')
        a = open('host.txt', 'rt')
        ler = a.read()
        for i in ler:
            print(i, end="")
        a.close()
        time.sleep(2)

class Aplicar(Host):
    def __init__(self):
        Host.__init__(self)
    def imagem(self):
        return print('[1]Ping \n[2]Ping nos IPs da lista \n[3]Adicionar \n[4]Ver Lista \n[5]Ajuda \n[6]Sair')
    def opc(self, esc):
        if esc == 1:
            ip_host = input('root~# ')
            Host.mostrar(self, ip_host)
        elif esc == 2:
            Host.mostrar_todos(self)
        elif esc == 3:
            print('IPv4/IPv6')
            n_ip = input('root~# ') 
            Host.adicionar(self, n_ip)
        elif esc == 4:
            Host.lista(self)
        elif esc == 5:
            print('-' * 60)
            print('''SOMENTE IPv4/IPv6  \nOBS: Não ultrapasse os limites''')
        else:
            print('Essa opção nâo existe')


        
        

