from bs4 import BeautifulSoup
import requests

everything = {}


class Avengers(object):
    def __init__(self):
        file_open = open('/home/ubuntu/PycharmProjects/Transcend/imdb2.txt', 'r')
        for link in file_open:
            full_link = 'http://www.imdb.com' + link.strip()
            page = requests.get(full_link)
            self.soup = BeautifulSoup(page.text, 'html.parser')

    def title(self):
        try:
            title = self.soup.find_all("h1")[1].get_text()
            everything['title'] = title[:-7]
        except:
            return "This isn't working"

    def rating(self):
        try:
            rate = self.soup.find_all(class_='ratingValue')
            rating = "".join(rate[0].get_text().strip())
            everything['rating'] = rating
        except:
            return "This isn't Working"

    def director(self):
        try:
            director_wrapper = []
            screen_directors = []
            writers = []
            stars = []
            for director in self.soup.find_all(class_="credit_summary_item"):
                inclass = director.find_all('h4')
                text_inclass = director.find_all(class_="itemprop")
                for result in text_inclass:
                    directors = result.get_text()
                    director_wrapper.append(directors)
            screen_directors.append(director_wrapper[0])
            writers.append(director_wrapper[1:3])
            stars.append(director_wrapper[3:])
            everything['director'] = screen_directors
            everything['writers'] = writers
            everything['stars'] = stars
        except:
            return "this is not working"

    def cast(self):
        try:
            full_cast = []
            for cast in self.soup.find_all(class_="itemprop"):
                for all_cast in cast.find_all('span'):
                    full_cast.append(all_cast.get_text())
            everything['cast'] = full_cast
        except:
            return "This is not working"

    def plot_keywords(self):
        try:
            genre = []
            for line in self.soup.find_all('div', attrs={"class": "see-more inline canwrap"}):
                all_list = line.get_text().replace('\n', "")
                genre.append(all_list)
            filter_keywords = genre[0].replace(" ", "")
            everything['plot_keywords'] = [filter_keywords[13:52].strip()]
            filter_genre = genre[1]
            everything['genre'] = [filter_genre[8:].strip()]
        except:
            return "This is not working"

    def summary(self):
        try:
            summary_text = []
            for d in self.soup.find_all(class_="summary_text"):
                for e in d:
                    summary_text.append(e.strip())
            everything['summary'] = summary_text
        except:
            return "This is not working"

    def stroy_line(self):
        try:
            for line in self.soup.find_all(class_="inline canwrap"):
                story = line.find_all('p')
                for st in story:
                    st_line = st.get_text().strip()
                    everything['story_line'] = st_line
        except:
            return "This is not working"

    def others(self):
        try:
            text_block = []
            details = []
            main_attributes = []
            for budget in self.soup.find_all(class_='txt-block'):
                some = budget.get_text().strip().lstrip().rstrip()
                some_else = some.replace('\n', "").replace('\t', "").replace("  ", "")
                main_attributes.append(some_else)
                main_attributes = []
                for budget in self.soup.find_all(class_='txt-block'):
                    some = budget.get_text().strip().lstrip().rstrip()
                    some_else = some.replace('\n', "").replace('\t', "").replace("  ", "")
                    main_attributes.append(some_else)

            everything['country'] = main_attributes[4][8:]
            everything['language'] = main_attributes[5][9:]
            everything['release'] = main_attributes[6][14:-16]
            everything['budget'] = main_attributes[8][7:]
            everything['opening_weekend'] = main_attributes[9][16:-13]
            everything['gross'] = main_attributes[10][6:-18]
            everything['production'] = main_attributes[11][14:-24]
            everything['runtime'] = main_attributes[13][8:]
            everything['sound'] = main_attributes[14][10:]
            everything['color'] = main_attributes[15][6:]
            everything['aspect_ratio'] = main_attributes[16][14:]

            # for extract in self.soup.find_all(class_="txt-block"):
            #     for j in extract.find_all('a'):
            #         details.append(j.get_text())
        except:
            return "this is not working"


avengers = Avengers()
avengers.title()
avengers.rating()
avengers.director()
avengers.cast()
avengers.plot_keywords()
avengers.stroy_line()
avengers.summary()
avengers.others()
print(everything)
