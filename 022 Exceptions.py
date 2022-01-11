import requests
import time
from datetime import datetime

while True:
    try:
        a = requests.get('https://yandex.ru')
        print(a)
        time.sleep(60)
        if a == '<Response [200]>':
            pass
        elif a == '<Response [503]>':
            print('ошибка сайта')
        else:
            print('иная ошибка')
    except requests.exceptions.ConnectionError:
        error_time = datetime.now()
        print('Сервер упал!\n' + str(error_time))