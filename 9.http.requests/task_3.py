import datetime
import time
import requests


def get_stackoverflow_questions(range_day: int, tagged: str):
    list_questions = []
    url = 'https://api.stackexchange.com/2.3/questions'
    max_time = int(time.mktime(datetime.datetime.now().timetuple()))
    min_time = int(max_time - (range_day * 24 * 60 * 60))
    param = {'site': 'stackoverflow', 'order': 'desc', 'min': min_time, 'max': max_time, 'tagged': tagged}
    r = requests.get(url, params=param)
    for item in r.json()['items']:
        list_questions.append(item['link'])
    return list_questions


print(get_stackoverflow_questions(2, 'Python'))