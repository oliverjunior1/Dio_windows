# Recebe a entrada e armazena na variável "entrada"
entrada = input()

# Função responsável por extrair os domínios dos emails
def extrair_dominios(emails):
    # Separa os emails por ponto e vírgula
    lista_emails = emails.split(';')

    # Extrai os domínios dos emails
    dominios = [email.split("@")[1] for email in lista_emails]

    return dominios

# Imprime a lista de strings com os domínios
print(extrair_dominios(entrada))