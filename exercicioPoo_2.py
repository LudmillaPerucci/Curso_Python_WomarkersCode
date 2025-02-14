from abc import ABC, abstractmethod

class Cliente:
    def __init__(self, nome: str, telefone: str, renda_mensal: float, genero: str):
        self.nome = nome
        self.telefone = telefone
        self.renda_mensal = renda_mensal
        self.genero = genero

class ContaCorrente(ABC):
    def __init__(self, titulares: list):
        self.titulares = titulares  # Lista de clientes
        self.saldo = 0.0
        self.operacoes = []
    
    @abstractmethod
    def sacar(self, valor: float):
        pass
    
    def depositar(self, valor: float):
        if valor > 0:
            self.saldo += valor
            self.operacoes.append(f"Depósito: +{valor}")
        else:
            print("Valor inválido para depósito.")

    def extrato(self):
        print(f"Saldo atual: {self.saldo}")
        for operacao in self.operacoes:
            print(operacao)

class ContaMulher(ContaCorrente):
    def __init__(self, titulares: list):
        super().__init__(titulares)
        self.cheque_especial = sum(cliente.renda_mensal for cliente in titulares if cliente.genero.lower() == 'feminino')
    
    def sacar(self, valor: float):
        limite_disponivel = self.saldo + self.cheque_especial
        if valor > 0 and valor <= limite_disponivel:
            self.saldo -= valor
            self.operacoes.append(f"Saque: -{valor}")
        else:
            print("Saldo insuficiente para saque.")

class ContaHomem(ContaCorrente):
    def sacar(self, valor: float):
        if valor > 0 and valor <= self.saldo:
            self.saldo -= valor
            self.operacoes.append(f"Saque: -{valor}")
        else:
            print("Saldo insuficiente para saque.")

# Entrada de dados do usuário
nome = input("Nome: ")
telefone = input("Telefone: ")
renda_mensal = float(input("Renda mensal: "))
genero = input("Gênero (Feminino/Masculino): ").strip().lower()

cliente = Cliente(nome, telefone, renda_mensal, genero)

if genero == "feminino":
    conta = ContaMulher([cliente])
else:
    conta = ContaHomem([cliente])

while True:
    print("\n1. Depositar\n2. Sacar\n3. Extrato\n4. Sair")
    opcao = input("Escolha uma opção: ")
    
    if opcao == "1":
        valor = float(input("Valor do depósito: "))
        conta.depositar(valor)
    elif opcao == "2":
        valor = float(input("Valor do saque: "))
        conta.sacar(valor)
    elif opcao == "3":
        conta.extrato()
    elif opcao == "4":
        break
    else:
        print("Opção inválida.")
