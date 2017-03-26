"""Movie"""

import csv
from collections import Counter


class Movie(object):
    def __init__(self):
        self.user_id = []
        self.movie_id = []
        self.rating = []
        with open("/home/ubuntu/Downloads/Vote.txt", 'r') as path:
            reader = csv.reader(path, dialect="excel-tab")
            for content in reader:
                self.user_id.append(content[0])
                self.movie_id.append(content[1])
                self.rating.append(content[2])

    def unique_users(self):
        return len(set(self.user_id))

    def unique_movies(self):
        return len(set(self.movie_id))

    def highest_rating(self):
        data = zip(self.movie_id, self.rating)
        list_of_movies = []
        for k, v in data:
            if v == '1.00':
                list_of_movies.append(k)
        ki = [int(d) for d in list_of_movies]
        return ki[:10]

    def lowest_rating(self):
        delta = zip(self.movie_id, self.rating)
        kiki = []
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


m = Movie()

print(m.unique_users())
print(m.unique_movies())
print(m.highest_rating())
print(m.lowest_rating())
print(m.users_with_most_movies())
# print(m.users_with_less_movies())
