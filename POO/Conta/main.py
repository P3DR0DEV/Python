from classe import Conta, Cliente
from funcionarios import Funcionarios,Gerente

cliente1 = Cliente('João', 'Oliveira', '11111111111-11')
cliente2 = Cliente('José', 'Azevedo', '222222222-22')
conta1 = Conta('123-4', cliente1.nome, 1000.0)
conta2 = Conta('123-5', cliente2.nome, 1000.0)

gerente = Gerente('José','000',5000, '1234s',0)
print(gerente.get_bonificacao())

funcionario1 = Funcionarios('Pedro', '00002', 2000)
print(funcionario1.get_bonificacao())