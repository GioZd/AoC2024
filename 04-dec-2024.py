from typing import Iterable

def task_1(input_path) -> int:
    with open(input_path) as data_input:
        lines = data_input.readlines()
    counter = 0
    for line in lines:
        counter += line.count('XMAS') + line.count('SAMX')
    columns = [''.join(l[i] for l in lines) for i in range(len(lines[0]))]
    for column in columns:
        counter += column.count('XMAS') + column.count('SAMX')
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            desc_str = ''
            asc_str = ''
            for k in range(min(4, len(lines)-i , len(lines[i])-j)):
                desc_str += lines[i+k][j+k]
                asc_str += lines[-i-1-k][j+k]
            if desc_str == 'XMAS' or desc_str == 'SAMX':
                counter += 1
            if asc_str == 'XMAS' or asc_str == 'SAMX':
                counter += 1
    return counter

def task_2(input_path) -> int:
    def matrix_window(arr: list[str], size: int = 3) -> Iterable:
        flattened = ''
        for i in range(len(arr[:-size+1])):
            for j in range(len(arr[i][:-size+1])):
                flattened = [line[j:j+size] for line in arr[i:i+size]]
                yield flattened

    with open(input_path) as data_input:
        lines = data_input.readlines()
    counter = 0
    for win in matrix_window(lines):
        desc_diag = win[0][0] + win[1][1] + win[2][2]
        asc_diag = win[2][0] + win[1][1] + win[0][2]
        if (desc_diag in ['MAS', 'SAM']) and (asc_diag in ['MAS', 'SAM']):
            counter += 1
    return counter



if __name__ == '__main__':
    print(task_1('04-dec-2024-input.txt'))
    print(task_2('04-dec-2024-input.txt'))