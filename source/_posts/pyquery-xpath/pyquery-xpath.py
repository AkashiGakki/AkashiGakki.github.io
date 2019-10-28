import requests
from pyquery import PyQuery as pq

url = 'https://akashigakki.github.io'
html = requests.get(url=url)
doc = pq(html.text)
print(doc('title'))
