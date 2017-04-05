from bs4 import BeautifulSoup
import requests

path = 'http://www.imdb.com/title/tt0848228/'
everything = []


class Avengers(object):

    def __init__(self, path):
        page = requests.get(path)
        self.soup = BeautifulSoup(page.text, 'html.parser')

    def title(self):
        title = self.soup.find_all("h1")[1].get_text()
        everything.append(title)

    def rating(self):
        rate = self.soup.find_all(class_='ratingValue')
        rating = "".join(rate[0].get_text().strip())
        everything.append(rating)

    def director(self):
        for director in self.soup.find_all(class_="credit_summary_item"):
            inclass = director.find_all('h4')
            text_inclass = director.find_all(class_="itemprop")
            for result in text_inclass:
                everything.append(result.get_text())

    def cast(self):
        casting = []
        for k in self.soup.find_all(class_="itemprop"):
            cast = (k.find_all('span'))
            casting.append(cast)
        all_cast = []
        for i in casting:
            for j in i:
                all_cast.append((j).get_text())
        everything.append(all_cast)

    def plot_keywords(self):
        genre = []
        plot_keywords = []
        for gen in self.soup.find_all(class_="inline"):
            for fen in gen.find_all('a'):
                genre.append(fen.get_text())

        everything.append(genre[10:12])
        everything.append(genre[4:9])

    def summary(self):
        summary_text = []
        for d in self.soup.find_all(class_="summary_text"):
            for e in d:
                summary_text.append(e)
        everything.append(summary_text)

    def stroy_line(self):
        for line in self.soup.find_all(class_="inline canwrap"):
            story = line.find_all('p')
            for st in story:
                st_line = st.get_text().strip()
                everything.append(st_line)

    def others(self):
        text_block = []
        details = []
        box_office = []
        for extract in self.soup.find_all(class_="txt-block"):
            for i in extract.find_all('h4'):
                text_block.append(i.get_text())
        for extract in self.soup.find_all(class_="txt-block"):
            for j in extract.find_all('a'):
                details.append(j.get_text())


avengers = Avengers(path)
avengers.title()
avengers.rating()
avengers.director()
avengers.cast()
avengers.plot_keywords()
avengers.stroy_line()
avengers.summary()
avengers.others()
print(everything)



