# import requests
# from bs4 import BeautifulSoup

# url = 'https://akashigakki.github.io/'
# response = requests.get(url=url)
# html = response.text

# soup = BeautifulSoup(html, 'lxml')
# print(soup.prettify)
# print(soup.title.string)

from bs4 import BeautifulSoup

html = '''
<html><head><title>The Title</title></head>
<body>
<div>
    <p class='item'>Akashi</p>
    <a href='https://r1.example.com' class='site'>site_1</a>
    <a href='https://r2.example.com' class='site'>site_2</a>
</body>
</html>
'''

soup = BeautifulSoup(html, 'lxml')
# print(soup.title)
# print(soup.title.string)
# print(soup.p)
# print(soup.div.name)

# print(soup.p.attrs)
# print(soup.p.attrs['class'])

# print(soup.head.title)
# print(soup.div.contents)
# print(soup.div.children)
# for item in soup.div.children:
#     print(item)

# print(soup.select('a'))
for a in soup.select('a'):
    # print(a['class'])
    # print(a.attrs['class'])
    print(a.get_text())
    print(a.string)
