# Classe PlanoTelefone:
class PlanoTelefone:
    def __init__(self, nome, saldo):
        self.__nome = nome      # Encapsulando com __
        self.__saldo = saldo    # Encapsulando com __

    # Método para verificar o saldo
    def verificar_saldo(self):
        if self.__saldo < 10.0:
            return "Seu saldo está baixo. Recarregue e use os serviços do seu plano."
        elif self.__saldo >= 50.0:
            return "Parabéns! Continue aproveitando seu plano sem preocupações."
        else:
            return "Seu saldo está razoável. Aproveite o uso moderado do seu plano."

    # Método para gerar mensagem personalizada com base no saldo
    def mensagem_personalizada(self, nome_usuario):
        status = self.verificar_saldo()
        return f"{nome_usuario}, {status}"

    # Método getter para o saldo (opcional, caso precise acessar diretamente de fora)
    def get_saldo(self):
        return self.__saldo


# Classe UsuarioTelefone:
class UsuarioTelefone:
    def __init__(self, nome, plano):
        self.nome = nome
        self.plano = plano

    # Método para verificar saldo e gerar mensagem personalizada
    def verificar_saldo(self):
        mensagem = self.plano.mensagem_personalizada(self.nome)
        return self.plano.get_saldo(), mensagem


# Recebendo as entradas do usuário (nome, plano, saldo):
nome_usuario = input()
nome_plano = input()
saldo_inicial = float(input())

# Criando objetos do plano de telefone e do usuário:
plano_usuario = PlanoTelefone(nome_plano, saldo_inicial)
usuario = UsuarioTelefone(nome_usuario, plano_usuario)

# Chamando o método para verificar saldo sem acessar diretamente os atributos:
saldo_usuario, mensagem_usuario = usuario.verificar_saldo()
print(mensagem_usuario)
