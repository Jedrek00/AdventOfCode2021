def load_data():
    with open('input.txt', 'r') as f:
        data = [int(line) for line in f]
        return data


def task_one(measurements):
    counter = 0
    for i in range(1, len(measurements)):
        if measurements[i] > measurements[i - 1]:
            counter += 1
    return counter


def task_two(measurements):
    counter = 0
    for i in range(0, len(measurements) - 3):
        if measurements[i] < measurements[i + 3]:
            counter += 1
    return counter
        

def main():
    data = load_data()
    print(task_one(data))
    print(task_two(data))


if __name__ == '__main__':
    main()
