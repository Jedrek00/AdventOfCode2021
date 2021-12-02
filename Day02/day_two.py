def load_data():
    with open('input.txt', 'r') as f:
        data = [[line.split()[0], int(line.split()[1])] for line in f]
        return data


def task_one(courses):
    depth = 0
    horizontal = 0
    for course in courses:
        if course[0] == 'up':
            depth -= course[1]
        elif course[0] == 'down':
            depth += course[1]
        else:
            horizontal += course[1]
    
    return depth * horizontal


def task_two(courses):
    depth = 0
    horizontal = 0
    aim = 0
    for course in courses:
        if course[0] == 'up':
            aim -= course[1]
        elif course[0] == 'down':
            aim += course[1]
        else:
            horizontal += course[1]
            depth += aim * course[1]
    
    return depth * horizontal


def main():
    data = load_data()
    print(task_one(data))
    print(task_two(data))


if __name__ == '__main__':
    main()
