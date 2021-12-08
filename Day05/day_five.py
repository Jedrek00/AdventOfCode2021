def load_data():
    with open('input.txt', 'r') as f:
        lines = [line.strip().replace(' -> ', ',').split(',') for line in f]
        lines = [[int(x) for x in line] for line in lines]
        return lines


def max_height_and_width(lines):
    max_h, max_w = 0, 0
    for line in lines:
        max_w = max([max_w, line[0], line[2]])
        max_h = max([max_h, line[1], line[3]])
    return max_w, max_h


def create_matrix(height, width):
    matrix = [[0 for _ in range(width + 1)] for _ in range(height + 1)]
    return matrix


def task_one(lines, matrix):
    counter = 0
    for line in lines:
        if line[0] == line[2]:
            lower = min(line[1], line[3])
            for number in range(lower, lower + abs(line[1] - line[3]) + 1):
                matrix[number][line[0]] += 1
                if matrix[number][line[0]] == 2:
                    counter += 1
        if line[1] == line[3]:
            lower = min(line[0], line[2])
            for number in range(lower, lower + abs(line[0] - line[2]) + 1):
                matrix[line[1]][number] += 1
                if matrix[line[1]][number] == 2:
                    counter += 1
    return counter


def task_two(lines, matrix):
    counter = 0
    for line in lines:
        
        if line[0] == line[2]:
            lower = min(line[1], line[3])
            for number in range(lower, lower + abs(line[1] - line[3]) + 1):
                matrix[number][line[0]] += 1
                if matrix[number][line[0]] == 2:
                    counter += 1
        
        elif line[1] == line[3]:
            lower = min(line[0], line[2])
            for number in range(lower, lower + abs(line[0] - line[2]) + 1):
                matrix[line[1]][number] += 1
                if matrix[line[1]][number] == 2:
                    counter += 1

        else:
            sign_h, sign_w = 1, 1
            min_h, min_w = line[1], line[0]
            if line[0] > line[2]:
                #min_w = line[2]
                sign_w = -1
            if line[1] > line[3]:
                #min_h = line[3]
                sign_h = -1
            for number in range(abs(line[0] - line[2]) + 1):
                matrix[min_h + number * sign_h][min_w + number * sign_w] += 1
                if matrix[min_h + number * sign_h][min_w + number * sign_w] == 2:
                    counter += 1
    #print(matrix)
    return counter
    

def main():
    data =  load_data()
    max_w, max_h = max_height_and_width(data)
    matrix = create_matrix(max_h, max_w)
    print(task_two(data, matrix))


main()