# retrieve the latest news from radiology website (auntminnie.com)
from bs4 import BeautifulSoup
import requests

content = 'https://www.auntminnie.com/'

try:
    a = requests.get(content)
    if a.status_code == 200:
        print('Accessable')

except Exception:
    print('error')


soup = BeautifulSoup(a.text, 'html.parser')

print(soup.find('title').string)

print('This is the recent news:')
news = soup.find_all('span', attrs={'class': 'Head'})
for i in news:
    print(i.get_text())


