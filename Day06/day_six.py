def load_data():
    with open('input.txt', 'r') as f:
        data = [int(x) for x in f.readline().split(',')]
    return data


def task_one(data):
    for _ in range(80):
        for i in range(len(data)):
            data[i] -= 1
            if data[i] == -1:
                data.append(8)
                data[i] = 6
    return len(data)


def task_two(data):
    fish = [0] * 9
    for i in data:
        fish[i] += 1
    for day in range(256):
        new_fish = fish[0]
        for i in range(8):
            fish[i] = fish[i + 1]
        fish[8] = new_fish
        fish[6] += new_fish
    return(sum(fish))


data = load_data()
# print(task_one(data))
#data = [3,4,3,1,2]
print(task_two(data))