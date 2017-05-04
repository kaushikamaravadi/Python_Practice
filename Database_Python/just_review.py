from bs4 import BeautifulSoup
import requests
from afinn import Afinn
afinn = Afinn()
path = 'http://www.imdb.com/title/tt0848228/reviews-index?start=0;count=1731'
page = requests.get(path)
soup = BeautifulSoup(page.text, 'html.parser')
head = []

for tabs in soup.find_all(class_='reviews'):
    for info in tabs.find_all('tr'):
        for headers in info.find_all('h2'):
            new = headers.get_text()
            head.append(new)

positve = []
negative = []
neutral = []
for words in head:
    analysis = afinn.score(words)
    if words > '0.0':
        positve.append(words)
    elif words < '0.0':
        negative.append(words)
    elif words == '0.0':
        neutral.append(words)

print(len(positve))
print(len(negative))
print(len(neutral))