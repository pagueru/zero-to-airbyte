import os
import platform
from typing import NoReturn

from .logger import logger

def start_config() -> NoReturn:
    """
    Limpa o terminal e registra o início do script.

    Raises:
        OSError: Se houver um erro ao limpar o terminal.
    """
    try:
        # Detecta o sistema operacional e limpa a tela
        os.system('cls' if platform.system() == 'Windows' else 'clear')

    except Exception as e:
        logger.error(f'Erro ao limpar a tela: {e}')
        raise

    # Registra o início do script
    logger.info('Iniciando o script.')
