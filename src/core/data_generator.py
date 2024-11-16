import pandas as pd
import random
import string

# Função para gerar strings aleatórias
def random_string(length):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

# Criando um dataset grande o suficiente para atingir 1MB
rows = 10000  # Estimativa inicial de linhas para atingir o tamanho
data = {
    "CustomerID": [i for i in range(1, rows + 1)],
    "FirstName": [random_string(8) for _ in range(rows)],
    "LastName": [random_string(10) for _ in range(rows)],
    "Email": [random_string(5) + "@example.com" for _ in range(rows)],
    "Country": [random.choice(["USA", "Canada", "UK", "Germany", "France"]) for _ in range(rows)]
}

# Convertendo para um DataFrame
customers_large_df = pd.DataFrame(data)

# Salvando como um arquivo CSV e ajustando o número de linhas até atingir ~1MB
file_path_large = r"C:\Users\rapha\Documents\Github\zero-to-airbyte\customers.csv"
customers_large_df.to_csv(file_path_large, index=False)

# Verificando o tamanho do arquivo e ajustando se necessário
import os

file_size = os.path.getsize(file_path_large)
while file_size < 1 * 1024 * 1024:  # 1MB = 1 * 1024 * 1024 bytes
    more_data = {
        "CustomerID": [i for i in range(rows + 1, rows + 1001)],
        "FirstName": [random_string(8) for _ in range(1000)],
        "LastName": [random_string(10) for _ in range(1000)],
        "Email": [random_string(5) + "@example.com" for _ in range(1000)],
        "Country": [random.choice(["USA", "Canada", "UK", "Germany", "France"]) for _ in range(1000)]
    }
    rows += 1000
    more_df = pd.DataFrame(more_data)
    customers_large_df = pd.concat([customers_large_df, more_df])
    customers_large_df.to_csv(file_path_large, index=False)
    file_size = os.path.getsize(file_path_large)