from classe import Conta, Cliente

cliente1 = Cliente('João', 'Oliveira', '11111111111-11')
cliente2 = Cliente('José', 'Azevedo', '222222222-22')
conta1 = Conta('123-4', cliente1.nome, 1000.0)
conta2 = Conta('123-5', cliente2.nome, 1000.0)


conta1.depositar(100.0)
conta1.sacar(50.0)
conta1.tranfere_para(conta2, 200.0)
conta1.extrato()
conta1.historico.imprime()