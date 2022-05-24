from datetime import datetime


class Cliente:
    def __init__(self, nome, sobrenome, cpf):
        self.nome = nome 
        self.sobrenome = sobrenome
        self.cpf = cpf


class Historico:
    def __init__(self) -> None:
        self.data_abertura = datetime.today()
        self.transações = []

    def imprime(self):
        print(f'Data de Abertura de Conta: {self.data_abertura}')
        print('Transações: ')
        for t in self.transações:
            print('-', t)

class Conta:

    #método init inicia o objeto, já o __new__ cria um objeto
    def __init__(self,numero, cliente, saldo, limite = 500.0): 
        self.numero = numero
        self.titular = cliente
        self.saldo = saldo
        self.limite = limite
        self.historico = Historico()   #Variável passa a retomar a Classe Histórico 


    def sacar(self, quant):
        #Utiliza apenas o Saldo Disponível 
        if quant < self.saldo:
            self.saldo -= quant
            self.historico.transações.append(f'Saque de {quant}.')
            return True
            
        
        #Utiliza o limite da conta para efetuar o saque
        if quant < self.saldo + self.limite:
            self.saldo -= quant
            print('Limite Utilizado.')
            self.historico.transações.append(f'Saque de {quant}.')
            return True

        #Quantidade desejada maior que a Disponível e Limite     
        else:
            print('Não é possível sacar mais do que se tem na conta.')
            return False
        


    def tranfere_para(self, destino, quant):
        #Transfere a quantia para uma outra conta instanciada
        if quant < self.saldo:
            self.saldo -= quant
            destino.saldo += quant #destino.saldo = outra conta
            self.historico.transações.append(f'Transferencia feita de {quant}.')
            return True

        else:
            return False


    def depositar(self, quant):
        self.saldo += quant
        self.historico.transações.append(f'Desposito de {quant}')

    def extrato(self):
        print('-'*20)
        print(f'Número = {self.numero} \nTitular = {self.titular} \nSaldo = {self.saldo} \nLimite = {self.limite}')
        print('-'*20)


    