import sys


def word_count(file_name):
    word_count_dict = {}

    with open(file_name) as f:
        for line in f:
            words = line.strip().split(' ')

            for word in words:
                if word in word_count_dict:
                    word_count_dict[word] += 1
                else:
                    word_count_dict[word] = 1

    for word, count in word_count_dict.items():
        print(word, count)


if __name__ == '__main__':
    word_count(sys.argv[1])
