### Парсеры для Yakupi.ru

Застройщик: A101

`src/complex_parser` -- парсер ЖК; все ЖК собираются с помощью одного запроса

`src/flats_parser` -- последовательно парсит страницы с квартирами по 20 штук, данные по квартирам собирает в массив flats

### TODO: 

1. Последняя страница не попадает в flats
2. Информация не выводится в нормальном виде