import requests

api = 'https://superheroapi.com/api/2619421814940190/search'
superheroes = ['Hulk', 'Captain America', 'Thanos']
dict_heroes_int = {}

for hero in superheroes:
    r = r = requests.get(api + '/' + hero)
    dict_heroes_int[hero] = int(r.json()['results'][0]['powerstats']['intelligence'])

print(max(dict_heroes_int, key=dict_heroes_int.get))
