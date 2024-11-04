# implement me
import json

from src import flats_parser
from src import complex_parser

complexes = complex_parser.parse_complex()

res = dict()

res['developer'] = {
    "systemName": "A101",
    "name": "Группа компаний «А101»",
    "residentialComplexes": []
}

for comp in complexes:
    cur_comp = {
        'internalId': comp['id'],
        'name': comp['title'],
        'geoLocation': {
            'latitude': comp['latitude'],
            'longitude': comp['longitude']
        },
        'renderImageUrl': comp['preview'],
        'presentationUrl': None,
        'flats': []
    }
    res['developer']['residentialComplexes'].append(cur_comp)


print('Complexes parsed')

flats = flats_parser.parse_flats()

print('Flats parsed')

for flat in flats:
    for comp in res['developer']['residentialComplexes']:
        if comp['name'] == flat['ComplexName']:
            comp['flats'].append(flat)

with open('A101.json', 'w') as file:
    json.dump(res, file)
