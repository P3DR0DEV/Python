class Funcionarios:
    _quant_funcionarios = 0

    def __init__(self, nome, cpf, salario):
        self._nome = nome
        self._cpf = cpf
        self._salario = salario
        Funcionarios._quant_funcionarios += 1

    def get_bonificacao(self):
        return self._salario * 0.10

    @classmethod
    def get_funcionarios(cls):
        return cls._quant_funcionarios

class Gerente(Funcionarios):

    def __init__(self,nome, cpf, salario, senha, quant_gerenciavel):
        super().__init__(nome, cpf, salario)
        self._senha = senha
        self._quant_gerenciavel = quant_gerenciavel


    def get_bonificacao(self):
        return self._salario * 0.15

    def autenticação(self, senha):
        if self._senha == senha:
            print('Acesso Permitido.')
            return True
        else:
            print('Acesso Negado.')
            return False
