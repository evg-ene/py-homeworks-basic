from encodings import utf_8

cook_book = {}
with open('recipes.txt',encoding="utf_8") as f:
    recipes = f.read()
    for rec in recipes.split('\n\n'):
        ingredient_list = []
        for item in rec.split('\n'):
            if '|' in item:
                ingredient_list.append({'ingredient_name': item.split(' | ')[0], 'quantity': item.split(' | ')[1], 'measure': item.split(' | ')[2]})
        cook_book[rec.split('\n')[0]] = ingredient_list
print(cook_book)