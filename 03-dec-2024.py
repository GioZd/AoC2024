import re

def task_1(input_path: str) -> int:
    with open(input_path, 'r') as data_input:
        data = data_input.read()
    occurences = re.findall("mul\(\d+,\d+\)", data)
    mul = lambda a,b: a*b
    return(sum(map(eval, occurences)))

def task_2(input_path: str) -> int:
    with open(input_path, 'r') as data_input:
        data = data_input.read()
    i = 0
    start = 0
    end = data.find("don't()")
    occurences = []
    while i != -1:
        print(start, end)
        occurences += re.findall("mul\(\d+,\d+\)", data[start:end])
        start = data.find("do()", end)
        end = data.find("don't()", start)
        i = min(start, end)
    mul = lambda a,b: a*b
    return(sum(map(eval, occurences)))


if __name__ == '__main__':
    print(task_1('03-dec-2024-input.txt'))
    print(task_2('03-dec-2024-input.txt'))