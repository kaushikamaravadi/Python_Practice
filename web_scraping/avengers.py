from bs4 import BeautifulSoup
import requests
import json


imdb_movie_list = []


class Avengers(object):
    def __init__(self):
        file_open = open('/home/ubuntu/PycharmProjects/Transcend/imdb2.txt', 'r')
        count = 0
        for link in file_open:
            self.everything = {}
            full_link = 'http://www.imdb.com' + link.strip()
            count = count + 1
            print(count, full_link)
            page = requests.get(full_link)
            print(page.status_code)
            self.soup = BeautifulSoup(page.text, 'html.parser')
            Avengers.title(self)
            Avengers.rating(self)
            Avengers.director(self)
            print("yes")
            # Avengers.stroy_line(self)
            # Avengers.json_dump(self)
            Avengers.cast(self)
            Avengers.plot_keywords(self)
            Avengers.others(self)
            Avengers.summary(self)
            imdb_movie_list.append(self.everything)
            print("Appended")

    def title(self):
        try:
            title = self.soup.find_all("h1")[1].get_text()
            self.everything['title'] = title[:-7]
        except:
            return "This isn't working"

    def rating(self):
        try:
            rate = self.soup.find_all(class_='ratingValue')
            rating = "".join(rate[0].get_text().strip())
            self.everything['rating'] = rating
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
            for direc in screen_directors:
                self.everything['director'] = direc
            for writer in writers:
                self.everything['writers'] = writer
                # print(writer)
            for st in stars:
                self.everything['stars'] = st
        except:
            return "this is not working"

    def cast(self):
        try:
            full_cast = []
            for cast in self.soup.find_all(class_="itemprop"):
                for all_cast in cast.find_all('span'):
                    full_cast.append(all_cast.get_text())
            self.everything['cast'] = full_cast
        except:
            return "This is not working"

    def plot_keywords(self):
        try:
            genre = []
            for line in self.soup.find_all('div', attrs={"class": "see-more inline canwrap"}):
                all_list = line.get_text().replace('\n', "")
                genre.append(all_list)
            filter_keywords = genre[0].replace(" ", "")
            self.everything['plot_keywords'] = filter_keywords[13:52].strip()
            filter_genre = genre[1]
            self.everything['genre'] = filter_genre[8:].strip()
        except:
            return "This is not working"

    def summary(self):
        try:
            summary_text = []
            for d in self.soup.find_all(class_="summary_text"):
                for e in d:
                    summary_text.append(e.strip())
            self.everything['summary'] = summary_text
        except:
            return "This is not working"

    # def stroy_line(self):
    #     try:
    #         for line in self.soup.find_all(class_="inline canwrap"):
    #             story = line.find_all('p')
    #             for st in story:
    #                 st_line = st.get_text().strip()
    #                 self.everything['story_line'] = st_line
    #     except:
    #         return "This is not working"

    def others(self):
        try:
            main_attributes = []
            for budget in self.soup.find_all(class_='txt-block'):
                some = budget.get_text().strip().lstrip().rstrip()
                some_else = some.replace('\n', "").replace('\t', "").replace("  ", "")
                main_attributes.append(some_else)
            for i in main_attributes:
                if 'Gross' in i:
                    gross, number, year = i.split()
                    self.everything['Gross'] = gross[6:-2]
                if "Country" in i:
                    self.everything['country'] = i[8:]
                if 'Language' in i:
                    self.everything['Language'] = i[9:]
                if 'Release' in i:
                    self.everything["Release_Date"] = i[14:-16]
                if 'Opening' in i:
                    self.everything['Opening'] = i[17:-13]
                if 'Runtime' in i:
                    self.everything['Runtime'] = i[8:]
                if 'Sound' in i:
                    self.everything['Sound'] = i[10:]
                if 'Color' in i:
                    self.everything['Color'] = i[6:]
                if 'Aspect Ratio' in i:
                    self.everything["Aspect_Ratio"] = i[14:]
        except:
            return "this is not working"


        # print(everything)


avengers = Avengers()
print(imdb_movie_list)


with open('/home/ubuntu/imdb4.json', 'w') as final_file:
    json.dump(imdb_movie_list, final_file)

