class ContaBancaria:
    def __init__(self, titular):
        self.titular = titular
        self.saldo = 0
        self.operacoes = []

    def depositar(self, valor):
        self.saldo += valor
        if valor == 0:
            self.operacoes.append("0")
        else:
            self.operacoes.append(f"+{valor}")

    def sacar(self, valor):
        valor_abs = abs(valor)
        if self.saldo >= valor_abs:
            self.saldo -= valor_abs
            self.operacoes.append(f"-{valor_abs}")
        else:
            self.operacoes.append("Saque não permitido")

    def extrato(self):
        operacoes_formatadas = ", ".join(self.operacoes)
        print(f"Operações: {operacoes_formatadas}; Saldo: {self.saldo}")


# Entrada de dados
nome_titular = input().strip()
conta = ContaBancaria(nome_titular)

entrada_transacoes = input().strip()
transacoes = [int(valor) for valor in entrada_transacoes.split(",")]

for valor in transacoes:
    if valor >= 0:
        conta.depositar(valor)
    else:
        conta.sacar(valor)

conta.extrato()