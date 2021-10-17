from sistema_banco import *
class Interface(Conta):
    '''
        Chama todas as funcionalidades do banco e da conta 
    '''
    def __init__(self):
        Conta.__init__(self)
    def linha(self, tam=15):
        print('-' * tam)
    def mostrando(self):
        self.linha()
        Interface.saldo(self)
        print('[1]Depositar \n[2]Saque \n[3]Emprestimo \n[4]Sair')
        self.linha()
    def dep(self, valor):
        Interface.deposito(self, valor)
    def sac(self, valor):
        Interface.saque(self, valor)
            

    
        

