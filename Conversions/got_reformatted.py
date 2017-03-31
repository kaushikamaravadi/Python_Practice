import json

sum_of_episodes = []
got = json.loads(open('/home/ubuntu/Downloads/got.json').read())


def parse(got):

    for key, value in got.items():
        if isinstance(value, dict):
            print(parse(value))
        if isinstance(value, list):
            for items in value:
                if isinstance(items, list):
                    for i in items:
                        print(i)
                if isinstance(items, dict):
                    print(parse(items))
                else:
                    for ite in value:
                        print(ite)
        if isinstance(value, int):
            print(value)
        if isinstance(value, str):
            print(value)


print("total number of episodes is ", len(sum_of_episodes))

parse(got)
