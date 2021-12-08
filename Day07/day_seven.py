def load_data():
    with open('input.txt', 'r') as f:
        data = [int(x) for x in f.readline().split(',')]
        return data


def median(list):
    if len(list) == 0:
        return -1
    middle = len(list) // 2
    if len(list) % 2 == 0:
        return (list[middle] + list[middle - 1]) / 2.0
    else:
        return list[middle]


def calculate_new_distance(x, data):
    diff = 0
    for i in data:
        diff += (abs(x - i) + (x - i) ** 2) / 2
    return diff


def task_one(data):
    m = median(sorted(data))
    if m % 1 != 0:
        diff_lower = [abs(int(m) - x) for x in data]
        diff_higher = [abs(int(m) + 1 - x) for x in data]
        return min(diff_higher, diff_lower)
    diff = [abs(m - x) for x in data]
    return sum(diff)


def task_two(data):
    lb = min(data)
    up = max(data)
    mid = 0
    while up - lb > 1:
        mid = (lb + up) // 2
        if calculate_new_distance(up, data) < calculate_new_distance(lb, data):
            lb = mid
        else:
            up = mid
    return calculate_new_distance(mid, data)


def main():
    data = load_data()
    print(task_one(data))
    print(task_two(data))


if __name__ == '__mian__':
    main()
