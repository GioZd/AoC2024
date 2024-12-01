import csv

def task_1_and_2(input_path: str) -> int:
    with open(input_path, 'r') as data_input:
        data = csv.reader(
            data_input, 
            delimiter = ' '
        )
        data = list(data)
    id1 = sorted(int(r[0]) for r in data)
    id2 = sorted(int(r[3]) for r in data)
    # print(id1[:5])
    # print(id2[:5])
    return (
        sum(map(lambda t: abs(t[1]-t[0]), zip(id1, id2))),
        sum(map(lambda x: x*id2.count(x), id1))
    )


if __name__ == '__main__':
    print(task_1_and_2('01-dec-2024-input.txt'), sep='\n')