catalog = [
    {"name": "Смартфон", "price": 45000, "rating": 4.8},
    {"name": "Чехол для телефона", "price": 500, "rating": 4.2},
    {"name": "Беспроводные наушники", "price":7000, "rating": 4.8},
    {"name": "Зарядное устройство", "price":1200, "rating": 4.5},
]

price_sort = sorted(catalog,key = lambda item:item['price'], reverse=False)
#print(result)
rate_sort = sorted(price_sort,key = lambda item:item["rating"], reverse= True)
print(rate_sort)