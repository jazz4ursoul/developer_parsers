from src.config import requests, json


def parse_flats():
    page_limit = 1000
    offset = 0

    data = dict()
    data['next'] = 1

    flats = []

    while data['next'] is not None:
        url = f"https://a101.ru/api/v2/flat/?ordering=actual_price&limit={page_limit}&offset={offset}"
        response = requests.get(url)

        if response.status_code != 200:
            print(f"Error: {response.status_code}")
            exit(1)

        data = response.json()

        cur_flats = data['results']
        flats.extend(cur_flats)

        offset += page_limit

    print(len(flats))
    print(flats[0])

    flats_to_json = []

    for flat in flats:
        flat_id = flat['id']

        DeveloperUrl = f"https://a101.ru/kvartiry/{flat_id}/"
        Floor = flat['floor']
        Price = flat['actual_price']
        Area = flat['area']
        Rooms = flat['room']
        Deadline = flat['stage']  # TODO ?
        PlanImage = flat['plan_image']
        ComplexName = flat['complex']

        cur_flat = {
            "developerUrl": DeveloperUrl,
            "floor": Floor,
            "price": Price,
            "area": Area,
            "rooms": Rooms,
            "buildingDeadline": Deadline,
            "layoutImage": PlanImage,
            "ComplexName": ComplexName
        }

        flats_to_json.append(cur_flat)

    return flats_to_json
