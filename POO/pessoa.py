class Pessoa:
    ano_atual = 2022
    def __init__(self, nome, idade, comendo =False, falando = False):
        self.nome = nome
        self.idade = idade
        self.comendo = comendo
        self.falando = falando 


    def comer(self, alimento):
        if self.falando:
            print(f'{self.nome} não pode comer enquanto estiver falando.')
            return
        if self.comendo:
            print(f'{self.nome} já está comendo')
            return
        print(f'{self.nome} está comendo {alimento}.')
        self.comendo = True


    def parar_comer(self):
        if not self.comendo:
            print(f'{self.nome} não está comendo.')
            return
        print(f'{self.nome} parou de comer.')
        self.comendo = False


    def falar(self, assunto):    
        if self.comendo:
            print(f'{self.nome} não pode falar enquanto come.')
            return
        if self.falando:
            print(f'{self.nome} já está falando')
            return
        print(f'{self.nome} está falando sobre {assunto}')
        self.falando = True


    def parar_falar(self):

        if not self.falando:
            print(f'{self.nome} não está falando.')
            return
        print(f'{self.nome} parou de falar.')
        self.falando = False


    #Método de Classe
    @classmethod
    def ano_nasc(cls, nome, ano_nascimento):
        idade = cls.ano_atual - ano_nascimento
        return cls(nome, idade)
