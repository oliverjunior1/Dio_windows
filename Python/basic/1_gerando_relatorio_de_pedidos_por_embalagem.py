import re
import sys

# Lê o número de pedidos
try:
    N = int(sys.stdin.readline().strip())
except Exception:
    N = 0

# Tipos válidos
tipos = ["saco", "papelao ondulado", "papel kraft"]

# Dicionário para armazenar totais por tipo de embalagem
totais = {t: 0.0 for t in tipos}

# Regex para capturar número (inteiro ou decimal)
num_re = re.compile(r"[-+]?\d+(?:\.\d+)?")

for _ in range(N):
    linha = sys.stdin.readline()
    if not linha:
        continue
    linha = linha.strip()

    # 1) tenta achar o tipo de embalagem nas palavras da linha (case-insensitive)
    embalagem_encontrada = None
    lower = linha.lower()
    for t in tipos:
        if t in lower:
            embalagem_encontrada = t
            break

    # 2) tenta achar a quantidade como o primeiro número da linha
    m = num_re.search(linha)
    if m:
        quantidade = float(m.group(0))
    else:
        # fallback: se não achar número, assume 0
        quantidade = 0.0

    # 3) se não encontrarmos embalagem, tentamos fazer split por ","
    if embalagem_encontrada is None:
        parts = [p.strip() for p in linha.split(",")]
        if len(parts) >= 3:
            embalagem_encontrada = parts[1].lower()
        elif len(parts) == 2:
            # se só tiver dois campos, tenta inferir se o segundo é embalagem ou quantidade
            # já temos a quantidade pelo regex, então assumimos o segundo como embalagem
            embalagem_encontrada = parts[1].lower()

    # 4) se ainda não reconheceu o tipo válido, ignoramos esta linha
    if embalagem_encontrada not in tipos:
        # opcional: você pode imprimir uma mensagem de aviso,
        # mas em ambientes de juízes automáticos é melhor apenas ignorar.
        continue

    totais[embalagem_encontrada] += quantidade

# Imprime o resultado no formato solicitado
for tipo in tipos:
    valor = totais[tipo]
    if valor.is_integer():
        valor = int(valor)
    print(f"{tipo}: {valor}")
