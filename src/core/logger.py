import logging

from .constants import LOG_FILE_PATH

# Criar um logger
logger: logging.Logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)  # Configura o nível do logger para o menor nível necessário

# Criar um handler para o arquivo
file_handler: logging.FileHandler = logging.FileHandler(LOG_FILE_PATH)
file_handler.setLevel(logging.DEBUG)  # Nível de log para arquivo

# Criar um handler para o console
console_handler: logging.StreamHandler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)  # Nível de log para console

# Criar um formato de log (sem microsegundos)
formatter: logging.Formatter = logging.Formatter(
    '%(asctime)s - %(filename)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'  # Formato de data/hora sem microsegundos
)
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

# Adicionar handlers ao logger
logger.addHandler(file_handler)
logger.addHandler(console_handler)

# Teste de mensagens de log
# logger.debug('Mensagem de debug (aparece apenas no arquivo).')
# logger.info('Mensagem de informação (aparece no terminal e no arquivo).')
