# Leitura do número de exportações
n = int(input())

# Inicializa o dicionário para armazenar toneladas por país
exportacoes = {}

# Loop para ler os dados de cada exportação
for _ in range(n):
    linha = input().strip()
    pais, toneladas = linha.split(",")

    pais = pais.strip()
    toneladas = float(toneladas.strip())

    # Acumula as toneladas de exportação de cada país
    if pais not in exportacoes:
        exportacoes[pais] = 0
    exportacoes[pais] += toneladas

# Imprime o total de toneladas por país na ordem de inserção
for pais, total in exportacoes.items():
    # converte para inteiro se não houver decimais
    if total.is_integer():
        total = int(total)
    print(f"{pais}: {total} toneladas")
