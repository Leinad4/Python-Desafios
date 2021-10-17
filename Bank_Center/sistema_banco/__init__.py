from time import sleep
class Bank(object):
    '''
        Estrutura do banco
    '''
    __total = 10000 # Valor total que o banco possui
    __taxa_Exigida = 0.1 # Valor limite que banco deve ter 
    def __init__(self):
        pass   
    def adicionando(self, valor):
        Bank.__total += valor
    def tirando(self, valor):
        Bank.__total -= valor
    def __calculo(self):
        return self.__total * self.__taxa_Exigida
    def emprestimo(self, valor):
        if valor <= self.__calculo():
            Bank.__total -= valor
            print('Emprestimo foi aceito')
            sleep(2)
            return True
        else:
            print('Emprestimo recusado!')
            sleep(2)
            return False


class Conta(Bank):
    '''
        Estutura da conta do usuário
    '''
    def __init__(self):
        Bank.__init__(self)
        self.__saldo = 0

    def deposito(self, valor):
        self.__saldo += valor
        Conta.adicionando(self, valor)
        
    def saque(self, valor):
        if self.__saldo > 0:
            self.__saldo -= valor
            Conta.tirando(self, valor)
        else:
            print('Saldo Insuficiente')
    def pedindo(self, valor):
        a = Conta.emprestimo(self, valor)
        if a == True:
            self.__saldo += valor
    def saldo(self):
        print(f'Saldo: {self.__saldo}')
        



