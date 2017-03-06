import csv
class Movie:
    movie_id_list = []
    def __init__(self,user_id,movie_id,rating,junk,time_stamp):
        self.user_id = user_id
        self.movie_id = movie_id
        self.rating = rating
        self.junk = junk
        self.time_stamp = time_stamp

    def movie(self):
        with open("/home/kaushik/Downloads/Vote.txt", "r") as tsv:
            for line in csv.reader(tsv, dialect="excel-tab"):
                self.movie_id = line[1]
                self.rating = line[2]
                self.time_stamp = line[4]

    def user(self):
        with open("/home/kaushik/Downloads/Vote.txt", "r") as tsv:
            for line in csv.reader(tsv, dialect="excel-tab"):
                self.user_id = line[0]


movie = Movie
print(movie.user)







