"""Vote. txt contains Five Columns would look something like 
1       1       0.60    1.00    4/15/96 13:16:00
1       2       0.60    1.00    10/22/96 16:37:31
1       10      0.40    1.00    10/26/96 15:07:36
1       13      0.00    0.20    4/15/96 12:13:36
1       17      0.80    1.00    9/18/96 9:22:08

Find total number of Unique Users
Find total number of Unique Movies
Find  10 Movies with Highest Rating
Find 10 Movies with Lowest Rating
Find 10 Users who watched most movies
Find 10 Users who watched less movies
"""


import csv
from collections import Counter


users = []
movies = []
ratings = []
with open("/home/ubuntu/Downloads/Vote.txt", 'r') as path:
    reader = csv.reader(path, dialect="excel-tab")
    for content in reader:
        users.append(content[0])
        movies.append(content[1])
        ratings.append(content[2])


class Movie(object):
    def __init__(self, user_id, movie_id, rating):
        self.user_id = user_id
        self.movie_id = movie_id
        self.rating = rating

    def unique_users(self):
        return len(set(self.user_id))

    def unique_movies(self):
        return len(set(self.movie_id))

    def highest_rating(self):
        data = zip(self.movie_id, self.rating)
        list_of_movies= []
        for k, v in data:
            if v == '1.00':
                list_of_movies.append(k)
        ki = [int(d) for d in list_of_movies]
        return ki[:10]

    def lowest_rating(self):
        delta = zip(self.movie_id, self.rating)
        kiki= []
        for k, v in delta:
            if v == '0.00':
                kiki.append(k)
        ki = [int(d) for d in kiki]
        return ki[:10]

    def users_with_most_movies(self):
        users_with_mm = Counter(self.user_id)

        return users_with_mm.most_common(10)

    def users_with_less_movies(self):
        users_with_lm = Counter(self.user_id)
        return users_with_lm


m = Movie(users, movies, ratings)

print(m.unique_users())
print(m.unique_movies())
print(m.highest_rating())
print(m.lowest_rating())
print(m.users_with_most_movies())
#print(m.users_with_less_movies())
