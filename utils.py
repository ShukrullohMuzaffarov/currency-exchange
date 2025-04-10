import requests
from os import getenv
from dotenv import load_dotenv
load_dotenv()
API_KEY = getenv('Your_API_Key')
async def currency_exchange(_from, _to):
    url = f"https://v6.exchangerate-api.com/v6/{API_KEY}/pair/{_from}/{_to}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data["conversion_rate"]
    return None