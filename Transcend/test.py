from bs4 import BeautifulSoup
import requests
import time
import sys
start = time.time()
list_of_links = []


def path_finder(first_page='http://www.imdb.com/list/ls057823854/?start=9751&view=compact&sort=listorian:asc'):
    page = requests.get(first_page)
    soup = BeautifulSoup(page.text, 'html.parser')

    if first_page == 'http://www.imdb.com/list/ls057823854/?start=1&view=compact&sort=listorian:asc':
        sys.exit()

    for next in soup.find_all(class_='see-more'):
        for links in soup.find_all(class_='pages'):
            for link in links.find_all(class_='pagination'):
                for href in link.find_all('a'):
                    next = href.get_text()
                    print(next)
                    print("yes",href.get('href'))
                    if '« Prev' in next:
                        if '?start=1&view=compact&sort=listorian:asc' == href.get('href'):
                            sys.exit()
                        else:
                            list_of_links.append(href.get('href'))
                            first_page = 'http://www.imdb.com/list/ls057823854/' + href.get('href')
                            list_of_links.append(first_page)
                            # print(first_page)

                            second_page = requests.get(first_page)
                            soup2 = BeautifulSoup(second_page.text, 'html.parser')
                            for title_link in soup2.find_all(class_='title'):
                                for title in title_link.find_all('a'):
                                    ti = []
                                    # print(title.get('href'))
                                    ti.append(title.get('href'))
                                    print(ti)
                                    with open('/home/ubuntu/PycharmProjects/Transcend/imdb2.txt','a') as file_open:
                                        file_open.write(title.get('href'))
                                        file_open.write('\n')

                            path_finder(first_page)
    end = time.time()
    print(end - start)

print(path_finder(first_page='http://www.imdb.com/list/ls057823854/?start=9751&view=compact&sort=listorian:asc'))


