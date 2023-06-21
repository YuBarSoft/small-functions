# Задача: зная ID видеоролика на Youtube сохранить превью.

import requests

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'
}

id_video = 'jpVpmg7qci0'
url = f'https://i.ytimg.com/vi/{id_image}/hq720.jpg'

r = requests.get(url, stream=True)
with open(f'{id_video}.jpg', 'wb') as f:
    for chunk in r.iter_content(8192):
        f.write(chunk)
