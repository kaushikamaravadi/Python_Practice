import json
import csv

csv_file = open('got.csv', 'w')
field_names = ["id", "url", "name", "season", "number", "airdate", "airtime", "airstamp", "runtime", "summary"]
writer = csv.DictWriter(csv_file, delimiter=',', fieldnames=field_names)
writer.writeheader()


def parse(path):
    sum_of_episodes = []
    got = json.loads(open(path).read())
    for key, value in got.items():
        if "_embedded" in key:
            # print("values of embedded", value)
            for name, element in value.items():
                if "episodes" in name:
                    print(element)
                for episode in element:
                    row = {}
                    sum_of_episodes.append(episode['number'])
                    row["id"] = episode['id']
                    row["url"] = episode['url']
                    row["name"] = episode['name']
                    row["season"] = episode['season']
                    row["number"] = episode['number']
                    row["airdate"] = episode['airdate']
                    row["airtime"] = episode['airtime']
                    row["airstamp"] = episode['airstamp']
                    row["runtime"] = episode['runtime']
                    row["summary"] = episode['summary']
                    writer.writerow(row)
    print("total number of episodes is ", len(sum_of_episodes))


parse('/home/ubuntu/Downloads/got.json')
