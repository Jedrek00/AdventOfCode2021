from collections import Counter

def load_data():
    with open("input.txt", "r") as f:
        d = {}
        for line in f:
            for i, char in enumerate(list(line[:-1])):
                d[i] = d.get(i, []) + [char]
        return d


def most_frequent(list):
    count = Counter(list)
    return count.most_common(1)[0][0]


def task_one(dict):
    for key in dict.keys():
        dict[key] = most_frequent(dict[key])
    epsilon_rate = [str(1 - int(x)) for x in dict.values()]

    gamma_rate = "".join(dict.values())
    epsilon_rate = "".join(epsilon_rate)
    
    return int(gamma_rate, 2) * int(epsilon_rate, 2)


def main():
    dict = load_data()
    print(task_one(dict))

if __name__ == '__main__':
    main()
