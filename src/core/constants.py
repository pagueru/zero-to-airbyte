from pathlib import Path

# Atribui as constantes raízes
FILE_PATH = Path(__file__).resolve()
PROJECT_PATH = FILE_PATH.parents[2]

# Atribui as constantes de pastas
CONFIG_FOLDER_PATH = PROJECT_PATH / 'config'
DATA_FOLDER_PATH = PROJECT_PATH / 'data'
LOG_FOLDER_PATH = PROJECT_PATH / 'logs'
SRC_FOLDER_PATH = PROJECT_PATH / 'src'

# Atribui as constantes de arquivos
CUSTOMERS_FILE_PATH = DATA_FOLDER_PATH / 'customers.csv'
LOG_FILE_PATH = LOG_FOLDER_PATH / 'app.log'