import csv
u = []
k = []
p = []
with open("/home/ubuntu/Downloads/Vote.txt", 'r') as path:
    reader = csv.reader(path, dialect="excel-tab")
    for content in reader:
        u.append(content[0])
        k.append(content[1])
        p.append(content[2])


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
        d = zip(self.movie_id, self.rating)
        kiki= []
        for k, v in d:
            if v == '1.00':
                kiki.append(k)
        ki = [int(d) for d in kiki]
        return ki[:10]

    def lowest_rating(self):
        d = zip(self.movie_id, self.rating)
        kiki= []
        for k, v in d:
            if v == '0.00':
                kiki.append(k)
        ki = [int(d) for d in kiki]
        return ki[:10]




m = Movie(u,k,p)

print(m.unique_users())
print(m.unique_movies())
print(m.highest_rating())
