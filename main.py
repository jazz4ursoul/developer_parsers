import json

import requests

# PARSE COMPLEXES

def parse_complex():
    # url = "https://a101.ru/api/v2/updated_complex/"
    #
    # response = requests.get(url)
    #
    # if response.status_code == 200:
    #     data = response.json()
    #     with open("a.json", 'w') as file:
    #         json.dump(data, file)
    # else:
    #     print(f'Error: {response.status_code}')

    with open("a.json", 'r') as file:
        data = json.load(file)["results"]
        for i in range(len(data)):
            title = data[i]['title']
            lat = data[i]['latitude']
            long = data[i]['longitude']

    return

# PARSE FLATS

def parse_flats():

    page_limit = 20

    offset = 0
    url = "https://a101.ru/api/v2/flat/?ordering=actual_price"
    response = requests.get(url)

    if response.status_code == 200:
        with open("b.json", 'w') as file:
            json.dump(response.json(), file)
            print("Success")
    else:
        print(f'Error: {response.status_code}')

    # with open('b.json', 'r') as file:
    #     data = json.load(file)
    #     print(data)
