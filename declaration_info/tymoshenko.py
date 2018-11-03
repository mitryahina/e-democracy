import requests
import json

candidates = ['Тимошенко Юлія Володимирівна']

data = []

for name in candidates:
    r = requests.get('https://declarations.com.ua/search?q={}&format=opendata&page=1'.format(name)).json()

    data += r["results"]["object_list"]

with open ("tymoshenko.txt", "w") as json_txt:
    print (r, file=json_txt)
