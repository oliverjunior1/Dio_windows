try:
    arquivo = open('meu_arquivo.py')
except FileNotFoundError as exc:
    print("Arquivo não encontrado")
    print(exc)