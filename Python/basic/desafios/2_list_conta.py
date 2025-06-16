# TODO: institui a conta e o depósio ou saque
saldo = 0
conta = input("Coloque o saque com (+) e os depósitos com (-) separados com ',': ")

# TODO: transforma os números recebidos em uma lista com números
dados_lista = [float(x) for x in conta.split(',') ]

# TODO: retira os valoers da lista e os calcula
for y in dados_lista:
    saldo += y

print(f"Saldo R$ {saldo:.2f}")
