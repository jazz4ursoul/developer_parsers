from config import requests, json


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
