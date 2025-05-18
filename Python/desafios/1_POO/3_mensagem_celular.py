# Classe UsuarioTelefone e o encapsulamento dos atributos nome, numero e plano:
class UsuarioTelefone:
    def __init__(self, nome, numero, plano):
        self.nome = nome
        self.numero = numero
        self.plano = plano

    def fazer_chamada(self, destinatario, duracao):
        custo = self.plano.custo_chamada(duracao)
        if self.plano.verificar_saldo() >= custo:
            self.plano.deduzir_saldo(custo)
            return f"Chamada para {destinatario} realizada com sucesso. Saldo: ${self.plano.verificar_saldo():.2f}"
        else:
            return "Saldo insuficiente para fazer a chamada."

# Classe Plano representa o plano de um usuário de telefone:
class Plano:
    def __init__(self, saldo_inicial):
        self.saldo = saldo_inicial

    def verificar_saldo(self):
        return self.saldo

    def custo_chamada(self, minutos):
        return minutos * 0.10  # Custo de $0.10 por minuto

    def deduzir_saldo(self, valor):
        self.saldo -= valor

# Classe UsuarioPrePago com herança de UsuarioTelefone:
class UsuarioPrePago(UsuarioTelefone):
    def __init__(self, nome, numero, saldo_inicial):
        super().__init__(nome, numero, Plano(saldo_inicial))

# Recebendo as informações do usuário:
nome = input().strip()
numero = input().strip()
saldo_inicial = float(input().strip())
destinatario = input().strip()
duracao = int(input().strip())

# Criando objeto UsuarioPrePago com os dados fornecidos:
usuario_pre_pago = UsuarioPrePago(nome, numero, saldo_inicial)

# Realizando a chamada e imprimindo o resultado:
print(usuario_pre_pago.fazer_chamada(destinatario, duracao))
