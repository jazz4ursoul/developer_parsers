from src.config import requests, json


def parse_flats():
    page_limit = 20
    offset = 0
    url = "https://a101.ru/api/v2/flat/?ordering=actual_price"

    response = requests.get(url)

    if response.status_code != 200:
        print(f"Error: {response.status_code}")
        exit(1)

    data = response.json()

    flats = []

    while data['next'] is not None:
        cur_flats = data['results']
        flats.extend(cur_flats)

        offset += page_limit
        url = f"https://a101.ru/api/v2/flat/?ordering=actual_price&limit={page_limit}&offset={offset}"

        response = requests.get(url)

        if response.status_code != 200:
            print(f"Error: {response.status_code}")
            exit(1)

        data = response.json()

        print(len(flats))
