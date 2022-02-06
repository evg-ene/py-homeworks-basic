from encodings import utf_8
from collections import Counter


cook_book = {}

with open('recipes.txt' ,encoding="utf_8") as f:
    recipes = f.read()
    for rec in recipes.split('\n\n'):
        ingredient_list = []
        for item in rec.split('\n'):
            if '|' in item:
                ingredient_list.append({'ingredient_name': item.split(' | ')[0], 'quantity': item.split(' | ')[1], 'measure': item.split(' | ')[2]})
        cook_book[rec.split('\n')[0]] = ingredient_list

def get_shop_list_by_dishes(dishes, person_count):
    need_items = {}
    double_dish = Counter(dishes)
    for dishe in dishes:
        for item in cook_book.get(dishe):
            need_items[item['ingredient_name']] = {'quantity': int(cook_book.get(dishe)[0]['quantity'])*int(person_count)*double_dish[dishe], 'measure': cook_book.get(dishe)[0]['measure']}
    print(need_items)

get_shop_list_by_dishes(['Запеченный картофель', 'Омлет', 'Омлет'], 3)
