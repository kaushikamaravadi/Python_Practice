import json
import csv


def movie_to_json():
    with open("/home/ubuntu/Downloads/Vote.txt", 'r') as path, open('/home/ubuntu/PycharmProjects/Transcend/movie.json',
                                                                    'w') as json_path:
        csv_rows = []
        reader = csv.DictReader(path, dialect="excel-tab")
        reader.fieldnames = ['uid', 'mid', 'rating', 'junk', 'time_stamp']
        title = reader.fieldnames
        for row in reader:
            csv_rows.extend([{title[i]: row[title[i]] for i in range(len(title))}])
        json_path.write(json.dumps(csv_rows))
