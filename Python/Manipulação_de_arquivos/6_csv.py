import csv
from pathlib import Path

ROOT_PATH = Path(__file__).parent

# try:
#     with open(ROOT_PATH/ "usuarios.csv", 'w', encoding="ufc-8") as arquivo:
#         escritor = csv.writer(arquivo)
#         escritor.writerow(["id", "nome"])
#         escritor.writerow(["1", "Maria"])
#         escritor.writerow(["2", "Joao"])
# except IOError as exc:
#     print(f"Erro ao criar o arquivo. {exc}")


try:
    with open(ROOT_PATH/ "usuarios.csv", 'w', encoding="ufc-8") as arquivo:
        leitor = csv.reader(arquivo)
        for row in leitor:
            print(row)
except IOError as exc:
    print(f"Erro ao criar o arquivo. {exc}")

