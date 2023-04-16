import csv
from typing import List


def read_data(path: str) -> List[List[str]]:
    """
    Lê a base de dados de um arquivo CSV e retorna o conteúdo no formato de lista.

    Args:
        path: Uma string contendo o caminho relativo do arquivo csv.

    Returns:
        Uma lista de listas com as linhas do arquivo no formato string.
    """
    with open(path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        return [row for row in reader]
