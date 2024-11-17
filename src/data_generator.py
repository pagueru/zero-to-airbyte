from pathlib import Path

import pandas as pd
from mimesis import Person, Address
from mimesis.locales import Locale

from core.constants import CUSTOMERS_FILE_PATH
from core.logger import logger
from core.utils import start_config


# Inicializa geradores da biblioteca Mimesis
person = Person(locale=Locale.PT_BR)
address = Address(locale=Locale.PT_BR)


def generate_dataset(
    rows: int, 
    start_id: int = 1
) -> pd.DataFrame:
    '''
    Gera um dataset com o número especificado de linhas.

    Args:
        rows (int): Número de linhas para o dataset.
        start_id (int): ID inicial para o CustomerID.

    Returns:
        pd.DataFrame: Dataset gerado.
    '''
    logger.info(f'Iniciando geração do dataset com {rows} linhas e start_id {start_id}')
    dataset = pd.DataFrame({
        'CustomerID': range(start_id, start_id + rows),
        'FirstName': [person.first_name() for _ in range(rows)],
        'LastName': [person.last_name() for _ in range(rows)],
        'Email': [person.email() for _ in range(rows)],
        'Country': [address.country() for _ in range(rows)],
    })
    logger.debug(f'Dataset gerado com {len(dataset)} linhas')
    return dataset


def adjust_dataset_size(
    file_path: Path, 
    dataset: pd.DataFrame, 
    target_size_mb: int
) -> pd.DataFrame:
    '''
    Ajusta o dataset para atingir aproximadamente o tamanho de arquivo desejado.

    Args:
        file_path (Path): Caminho para salvar o arquivo CSV.
        dataset (pd.DataFrame): Dataset inicial.
        target_size_mb (int): Tamanho alvo em megabytes.

    Returns:
        pd.DataFrame: Dataset ajustado.
    '''
    logger.info(f'Ajustando dataset para atingir aproximadamente {target_size_mb} MB')
    file_path.parent.mkdir(parents=True, exist_ok=True)
    target_size_bytes = target_size_mb * 1024 * 1024

    logger.debug(f'Tamanho alvo em bytes: {target_size_bytes}')
    while True:
        dataset.to_csv(file_path, index=False)
        current_size = file_path.stat().st_size
        logger.debug(f'Tamanho atual do arquivo: {current_size} bytes')
        if current_size >= target_size_bytes:
            logger.info(f'Tamanho alvo alcançado: {current_size} bytes')
            break
        logger.debug('Adicionando mais linhas ao dataset para alcançar o tamanho desejado')
        dataset = pd.concat(
            [dataset, generate_dataset(1000, dataset['CustomerID'].iloc[-1] + 1)],
            ignore_index=True
        )

    logger.info(f'Dataset ajustado salvo em: {file_path}')
    return dataset


def main() -> None:
    # Limpa o terminal e registra o início do script
    start_config()
    
    # Parâmetros
    initial_rows = 10000
    target_size_mb = 1

    # Gera e ajusta o dataset
    dataset = generate_dataset(initial_rows)
    final_dataset = adjust_dataset_size(
        file_path=CUSTOMERS_FILE_PATH, 
        dataset=dataset, 
        target_size_mb=target_size_mb
    )

    logger.info(f'Arquivo salvo com sucesso em: {CUSTOMERS_FILE_PATH}')