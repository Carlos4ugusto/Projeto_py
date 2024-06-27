from contas import Conta
from clientes import Cliente
cliente1 = Cliente(123, "Joao", "Rua 1")
cliente2 = Cliente(345, "Maria","Rua 2")
cliente3 = Cliente(301, "Carlos", "Rua 3")
conta1 = Conta([cliente1,cliente2, cliente3], 1,0) 
conta1.gerarsaldo()
conta1.depositar(1500)
conta1.sacar(500)
conta1.gerarsaldo()

conta2 = Conta([cliente1,cliente2, cliente3], 2, 0)
conta2.gerarsaldo()
conta2.depositar(2000)
conta2.sacar(200)
conta2.gerarsaldo()

