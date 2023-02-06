"""
4. *Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
Каждый кортеж хранит информацию об отдельном товаре.
В кортеже должно быть два элемента — номер товара и словарь с параметрами
(характеристиками товара: название, цена, количество, единица измерения).
Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.

Пример готовой структуры:
[
(1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
(2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
(3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
]

Далее необходимо собрать аналитику о товарах. Реализовать словарь,
в котором каждый ключ — характеристика товара,
например название,
а значение — список значений-характеристик, например список названий товаров.

Пример:

{
“названия”: [“компьютер”, “принтер”, “сканер”],
“цены”: [20000, 6000, 2000],
“количества”: [5, 2, 7],
“ед”: [“шт.”]
}
"""

goods = []


def fill_goods_database():
    i = 1
    ans = input("Enter new element? yes/no: ")
    while ans == 'yes':
        tur = (i, {"name": input(f"Enter good name:"),
                   "price": input(f"Enter good price:"),
                   "quantity": input(f"Enter good quantity:"),
                   "unit": input(f"Enter good unit:")})
        goods.append(tur)
        i += 1
        ans = input("Enter new element? yes/no: ")
    return goods


def goods_database_analytics(goods):
    result_dict = {}
    temp_list_names = []
    temp_list_prices = []
    temp_list_quantities = []
    temp_list_unit = []
    for element in goods:
        temp_list_names.append(element[1]['name'])
        temp_dict_names = {"names": temp_list_names}
        temp_list_prices.append(element[1]['price'])
        temp_dict_prices = {"prices": temp_list_prices}
        temp_list_quantities.append(element[1]['quantity'])
        temp_dict_quantities = {"quantities": temp_list_quantities}
        temp_list_unit.append(element[1]['unit'])
        temp_dict_unit = {"unit": temp_list_unit}
        result_dict.update(temp_dict_names)
        result_dict.update(temp_dict_prices)
        result_dict.update(temp_dict_quantities)
        result_dict.update(temp_dict_unit)
    return result_dict


print(goods_database_analytics(fill_goods_database()))




