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
    return count.most_common(1)[0]


def how_many(list, indexes):

    ones, zeroes = 0, 0
    for i, value in enumerate(list):
        if i in indexes:
            if value == '1':
                ones += 1
            else:
                zeroes += 1
    return zeroes, ones


def task_one(dict):
    dict_count = {}
    for key in dict.keys():
        dict_count[key] = most_frequent(dict[key])[0]
    epsilon_rate = [str(1 - int(x)) for x in dict_count.values()]

    gamma_rate = "".join(dict_count.values())
    epsilon_rate = "".join(epsilon_rate)
    
    return int(gamma_rate, 2) * int(epsilon_rate, 2)


def calculate_rating(dict, mode="oxygen"):
    indexes = {x for x in range(len(dict[0]))}
    default = '1'
    for key in dict.keys():
        zeroes, ones = how_many(dict[key], indexes)
        if zeroes > ones:
            value = '0'
        elif zeroes < ones:
            value = '1'
        else:
            value = default
        if mode == "CO2":
            value = str(1 - int(value))
        valids = {i for i, x in enumerate(dict[key]) if x == value and i in indexes}
        indexes = valids.intersection(indexes)
        if len(indexes) == 1:
            return list(indexes)[0]
    return -1


def task_two(dict):
    oxygen_rating_index = calculate_rating(dict)
    co2_rating_index = calculate_rating(dict, "CO2")
    oxygen_rating, co2_rating = [], []
    
    for key in dict.keys():
        oxygen_rating.append(dict[key][oxygen_rating_index])
        co2_rating.append(dict[key][co2_rating_index])
    
    oxygen_rating = "".join(oxygen_rating)
    co2_rating = "".join(co2_rating)

    return int(oxygen_rating, 2) * int(co2_rating, 2)


def main():
    dict = load_data()
    print(task_one(dict))
    print(task_two(dict))


if __name__ == '__main__':
    main()
