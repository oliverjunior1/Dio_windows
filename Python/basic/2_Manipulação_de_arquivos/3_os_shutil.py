import os
import shutil
from pathlib import Path

ROOT_PATH = Path(__file__).parent

os.mkdir(ROOT_PATH/"novo.txt", 'w')

arquivo = open(ROOT_PATH/"novo.txt", 'w')
arquivo.close()

os.rename(ROOT_PATH/"novo.txt", ROOT_PATH/"alterado.txt")

os.rename(ROOT_PATH/"alterado.txt")

os.rename(ROOT_PATH/"novo.txt", ROOT_PATH/"novo-diretorio"/'novo.txt')


