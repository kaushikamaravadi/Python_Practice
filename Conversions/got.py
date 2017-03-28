import json

sum_of_episodes = []


def parse(path):
    got = json.loads(open(path).read())
    for key, value in got.items():
        if "_embedded" in key:
            for name, element in value.items():
                for i in element:
                    # print(i.keys())
                    for iol in i.values():
                        print(iol)
                    episode_numbers = i['number']
                    sum_of_episodes.append(episode_numbers)


print("total number of episodes is ", len(sum_of_episodes))

print(parse('/home/ubuntu/Downloads/got.json'))
