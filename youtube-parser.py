# Получить ID и название ролика с Yutube.
# Передаем HTML-код в объект BeautifulSoup, затем извлекаем значения из тега iframe.
# Используем метод split для получения конечной части значения src (jpVpmg7qci0).

from bs4 import BeautifulSoup

html = '<iframe width="560" height="315" src="https://www.youtube.com/embed/jpVpmg7qci0" title="YouTube video player" frameborder="0" allow="accelerometer"></iframe>'
soup = BeautifulSoup(html, 'html.parser')

src = soup.iframe['src'].split('/')[-1]
title = soup.iframe['title']

print(src)
print(title)
