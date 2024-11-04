from src.config import requests, json


def parse_complex():
    url = "https://a101.ru/api/v2/updated_complex/"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        with open("complexes.json", 'w') as file:
            json.dump(data, file)
    else:
        print(f'Error: {response.status_code}')
