from bs4 import BeautifulSoup
import requests
import re
path = 'http://www.imdb.com/title/tt0848228/reviews?ref_=tt_ov_rt'
title = []
user_review = []

page = requests.get(path)
print(page.status_code)
soup = BeautifulSoup(page.text, 'html.parser')
# for node in soup.find_all(class_='reviews'):
#     for child in node.find_all('h2'):
#         title.append(child.get_text())
#     for para in node.find_all("p"):
#         par = para.get_text().replace("\n", ",")
#         # print(par.strip())
#         user_review.append(par)

# for tables in soup.find_all('td'):
#     for links in tables.find_all('a'):
#         print(links)
print(title)
# print(user_review)

