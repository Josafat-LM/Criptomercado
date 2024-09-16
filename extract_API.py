import requests
import csv
import pandas as pd

api_key = 'd4970e9f-a541-4fd0-8dbf-926c730fec28'

# Encabezados 
headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': api_key
}

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'

# Parámetros para la solicitud
params = {
    'start': '1',
    'limit': '5000',
    'convert': 'USD' 
}

# Solicitud GET
response = requests.get(url, headers=headers, params=params)
data = response.json()['data']

# Crear un archivo CSV y escribir los datos
with open('criptomonedas_con_categoria.csv', mode='w', newline='', encoding='utf-8') as file:
    fieldnames = ['name', 'symbol', 'quote', 'category', 'market_cap', 'price', 'volume_24h', 'circulating_supply']
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()

    # Iterar sobre las criptomonedas y extraer los datos
    for coin in data:
        writer.writerow({
            'name': coin['name'],
            'symbol': coin['symbol'],
            'quote': coin['quote']['USD']['price'],  # Valor en USD
            'category': coin['tags'][0] if coin['tags'] else 'Desconocida',  # Categoría 
            'market_cap': coin['quote']['USD']['market_cap'],
            'price': coin['quote']['USD']['price'],
            'volume_24h': coin['quote']['USD']['volume_24h'],
            'circulating_supply': coin['circulating_supply']
        })
#FILTRADOOOO
df = pd.read_csv('criptomonedas_con_categoria.csv')

# Categorías
categorias_filtrar = ['ai-big-data', 'memes', 'real-world-assets', 'gaming']

# Filtrar
df_filtrado = df[df['category'].isin(categorias_filtrar)]

# Guardar
df_filtrado.to_csv('criptomonedas_filtradas.csv', index=False)
