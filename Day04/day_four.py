def load_data():
    with open('input.txt') as f:
        numbers = [int(x) for x in f.readline().split(',')]
        boards = []
        board = []
        for line in f:
            if line == '\n':
                boards.append(board)
                board = []
            else:
                row = [int(x) for x in line.split()]
                board.append(row)
        return numbers, boards[1:]


def calculate_sum(board, numbers):
    sum_of_unmarked = 0
    for line in board:
        for number in line:
            if number not in numbers:
                sum_of_unmarked += number
    return sum_of_unmarked


def check_row(board, index, numbers):
    for number in board[index]:
        if number not in numbers:
            return -1  
    
    return calculate_sum(board, numbers)


def check_column(board, index, numbers):
    for i in range(5):
        if board[i][index] not in numbers:
            return -1
    
    return calculate_sum(board, numbers)


def task_one(numbers, boards):
    
    for i in range(4, len(numbers)):
        for board in boards:
            for j in range(5):
                
                col_sum = check_column(board, j, numbers[:i+1])
                row_sum = check_row(board, j, numbers[:i+1])
                
                if col_sum != -1:
                    return col_sum * numbers[i]
                
                if row_sum != -1:
                    return row_sum * numbers[i]


def task_two(numbers, boards):
    
    for i in range(4, len(numbers)):
        for board in boards:
            for j in range(5):
                
                col_sum = check_column(board, j, numbers[:i+1])
                row_sum = check_row(board, j, numbers[:i+1])
                
                if col_sum != -1:
                    if len(boards) != 1:
                        boards.remove(board)
                        break
                    else:
                        return col_sum * numbers[i]
                        
                if row_sum != -1:
                    if len(boards) != 1:
                        boards.remove(board)
                        break
                    else:
                        return row_sum * numbers[i]
                        


def main():
    numbers, boards = load_data()
    print(task_one(numbers, boards))
    print(task_two(numbers, boards))


if __name__ == '__main__':
    main()