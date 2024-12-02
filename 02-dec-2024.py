import csv
from itertools import pairwise

def task_1(input_path: str) -> int:
    with open(input_path, 'r') as data_input:
        data = csv.reader(
            data_input, 
            delimiter = ' '
        )
        data = list(data)
        data = [[int(x) for x in r] for r in data]
    counter = 0
    for row in data:
        increase_flag = True
        if (not all(a > b for a, b in pairwise(row))
            and not all(a < b for a, b in pairwise(row))):
            increase_flag = False
        for a, b in pairwise(row):
            if abs(a-b) > 3 or abs(a-b) < 1:
                increase_flag = False
        if increase_flag:
            counter += 1
    return counter

def task_2(input_path: str) -> int:
    with open(input_path, 'r') as data_input:
        data = csv.reader(
            data_input, 
            delimiter = ' '
        )
        data = list(data)
        data = [[int(x) for x in r] for r in data] 
        counter = 0
        for row in data:
            if ((all(a > b for a, b in pairwise(row)) 
                    or all(a < b for a, b in pairwise(row)))
                    and all(abs(a-b) <= 3 for a, b in pairwise(row))):
                counter += 1
            else:
                for c in range(len(row)):
                    sliced_row = row[:c] + row[c+1:]
                    if ((all(a > b for a, b in pairwise(sliced_row)) 
                            or all(a < b for a, b in pairwise(sliced_row)))
                            and all(abs(a-b) <= 3 for a, b in pairwise(sliced_row))):
                        counter += 1
                        break
        return counter



if __name__ == '__main__':
    print(task_1('02-dec-2024-input.txt'))
    print(task_2('02-dec-2024-input.txt'))
