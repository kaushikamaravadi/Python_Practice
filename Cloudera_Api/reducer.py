import sys
from itertools import groupby
from operator import itemgetter


def read_mapper_output(file, separator='\t'):
    for line in file:
        yield line.rstrip().split(separator, 1)


def main(seperator='\t'):
    data = read_mapper_output(sys.stdin, separator=seperator)

    for current_word, group in groupby(data, itemgetter(0)):
        try:
            total_count = sum(int(count) for current_word, count in group)
            print(current_word, seperator, total_count)
        except ValueError:
            pass


if __name__ == "__main__":
    main()
