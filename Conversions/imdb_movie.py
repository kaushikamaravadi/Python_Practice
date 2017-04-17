from bs4 import BeautifulSoup
import requests
import json
import logging

movie_info = {}
imdb_movie_list = []
cast_list = []


class Movie(object):

    """Scraping on crawled websites"""

    def __init__(self):
        file_open = open('/home/ubuntu/PycharmProjects/cloudera/imdb2.txt', 'r')
        count = 0
        for link in file_open:
            self.everything = {}
            full_link = 'http://www.imdb.com' + link.strip()
            count = count + 1
            print(count, full_link)
            page = requests.get(full_link)
            print(page.status_code)
            self.soup = BeautifulSoup(page.text, 'html.parser')
            Movie.title(self)
            Movie.rating(self)
            Movie.director(self)
            Movie.plot_keywords(self)
            Movie.others(self)
            Movie.summary(self)
            imdb_movie_list.append(self.everything)
            print("Appended")

    def title(self):

        """Extracting title of the movie"""

        try:
            title = self.soup.find_all("h1")[1].get_text()
            self.everything['title'] = title[:-7]
        except IndexError:
            self.everything['title'] = ""

    def rating(self):

        """Extracting rating of the movie """

        try:
            rate = self.soup.find_all(class_='ratingValue')
            rating = "".join(rate[0].get_text().strip())
            self.everything['rating'] = rating
        except IndexError:
            self.everything['rating'] = ""

    def director(self):

        """Extracting director, Writers and Stars"""

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
        except IndexError:
            self.everything['stars'] = ""
            self.everything['writers'] = ""
            self.everything['director'] = ""

    def plot_keywords(self):

        """Extracting Plot Keywords and genre of the movie"""

        try:
            genre = []
            for line in self.soup.find_all('div', attrs={"class": "see-more inline canwrap"}):
                all_list = line.get_text().replace('\n', "")
                genre.append(all_list)
            filter_keywords = genre[0].replace(" ", "")
            self.everything['plot_keywords'] = filter_keywords[13:-15].strip()
            filter_genre = genre[1]
            self.everything['genre'] = filter_genre[8:].strip()
        except IndexError:
            self.everything['genre'] = ""
            self.everything['plot_keywords'] = ""

    def summary(self):

        """Extracting Summary of the movie"""

        try:
            summary_text = []
            for d in self.soup.find_all(class_="summary_text"):
                for e in d:
                    summary_text.append(e.strip())
            self.everything['summary'] = summary_text
        except IndexError:
            self.everything['summary'] = ""

    def stroy_line(self):

        """Extracting Story Line of the movie"""

        try:
            for line in self.soup.find_all(class_="inline canwrap"):
                story = line.find_all('p')
                for st in story:
                    st_line = st.get_text().strip()
                    self.everything['story_line'] = st_line
        except IndexError:
            self.everything['story_line'] = ""

    def others(self):

        """Extracting Gross, Country, Language, Release, Opening,
         Runtime, Sound, Color and Aspect ratio of the movie"""
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

avengers = Movie()
movie_info['movie'] = imdb_movie_list


class Cast(object):

    def __init__(self):
        file_open = open('/home/ubuntu/PycharmProjects/cloudera/imdb2.txt', 'r')
        count = 0
        for link in file_open:
            self.casting = []
            full_link = 'http://www.imdb.com' + link.strip() + 'fullcredits?ref_=tt_cl_sm#cast'
            # full_link = 'http://www.imdb.com/title/tt0848228/fullcredits?ref_=tt_cl_sm#cast'
            count = count + 1
            page = requests.get(full_link)
            print(page.status_code)
            self.soup = BeautifulSoup(page.content, 'html.parser')
            Cast.extract(self)
            print(len(self.casting))
            cast_list.append(self.casting)

    def extract(self):
        for kaushik in self.soup.find_all(class_='odd'):
            full = kaushik.get_text().replace("\n", "").replace("  ", "").replace("...", "|")
            self.casting.append(full)
        for ka in self.soup.find_all(class_='even'):
            full_cast = ka.get_text().replace("\n", "").replace("  ", "").replace("...", "|")
            self.casting.append(full_cast)

cast = Cast()
movie_info['cast'] = cast_list
imdb_movie_list.append(movie_info)
print(movie_info)