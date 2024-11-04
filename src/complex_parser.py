from src.config import requests, json


def parse_complex():
    url = "https://a101.ru/api/v2/updated_complex/"

    response = requests.get(url)

    if response.status_code == 200:
        return response.json()['results']
    else:
        print(f'Error complex API request: status_code {response.status_code}')
        exit(1)
