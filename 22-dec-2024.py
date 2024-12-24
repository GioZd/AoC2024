from itertools import accumulate, repeat, pairwise, product
from time import time

def task_1(numbers: list[int]) -> int:
    C = 16777216
    tot = 0
    for num in numbers:
        new = num
        for i in range(2000):
            new = ((new * 64) ^ new) % C
            new = ((new // 32) ^ new) % C
            new = ((new * 2048) ^ new) % C
        tot += new
    return tot

def task_2_slooow(numbers: list[int]) -> int:
    t0 = time()
    C = 16777216
    # print(len(set(numbers)) == len(numbers))
    # secret numbers are all different
    secret_numbers = dict.fromkeys(numbers) 
    differences = secret_numbers.copy()
    def nextgen(num: int, mod: int = C) -> int:
        num = ((num * 64) ^ num) % mod
        num = ((num // 32) ^ num) % mod
        num = ((num * 2048) ^ num) % mod
        return num
         
    for first_secret in secret_numbers:
        secret_numbers[first_secret] = (
            list(accumulate(
                repeat(C, 2000),
                nextgen,
                initial = first_secret
            ))
        )
        secret_numbers[first_secret] = [
            n%10 for n in secret_numbers[first_secret]
        ]
        differences[first_secret] = [
            y - x for x, y in pairwise(secret_numbers[first_secret])
        ]

    # print(differences)
    # print(secret_numbers)

    def sublist_index(all_items: list[int], 
                      sublist: list[int]) -> int:
        for idx, el in enumerate(all_items):
            try:
                if all_items[idx:(idx+len(sublist))] == list(sublist):
                    return idx
            except:
                return -1
        return -1
    # print(sublist_index([1,2,3,4,5,6,7,8], [3,4,5,6]))
    # print(sublist_index([1,2,3,4,5,6,7,8], [3,4,4,6]))

    def check_validity(seq: list[int]) -> bool:
        for i in range(1, len(seq)+1):
            for j in range(len(seq)-i+1):
                if abs(sum(seq[j:(j+i)])) >= 10:
                    return False
        return True
    # print(check_validity([1,2,3,3]), check_validity([3,3,3,3]))
    sequences = list(
        filter(check_validity, # most sequences are impossible
            product(range(-9, 10), range(-9, 10), 
                    range(-9, 10), range(-9, 10))
        )
    )
    # print(sequences[:5], sequences[-6:])
    # print(len(sequences))

    # for num, diffs in differences.items():
    #     print(sublist_index(diffs, [-1, -1, 0, 2]))
    #     print(secret_numbers[num][sublist_index(diffs, [-1, -1, 0, 2])+4])
    # print(
    #     sum(
    #         secret_numbers[num][sublist_index(diffs, [-1, -1, 0, 2])+4] 
    #         for num, diffs in differences.items() 
    #         if sublist_index(diffs, [-1, -1, 0, 2]) != -1
    #     )
    # )
    n_bananas: list[int] = []
    for i, seq in enumerate(sequences):
        n_bananas.append(
            sum(
                secret_numbers[num][sublist_index(diffs, seq)+4] 
                for num, diffs in differences.items()
                if sublist_index(diffs, seq) != -1
            )
        )
        if i % 5000 == 0:
            print(i)

    # print(n_bananas)

    print(time()-t0)
    return max(n_bananas)



def task_2(numbers: list[int]) -> int:
    t0 = time()
    C = 16777216
    # print(len(set(numbers)) == len(numbers))
    # secret numbers are all different
    secret_numbers = dict.fromkeys(numbers) 
    differences = secret_numbers.copy()
    def nextgen(num: int, mod: int = C) -> int:
        num = ((num * 64) ^ num) % mod
        num = ((num // 32) ^ num) % mod
        num = ((num * 2048) ^ num) % mod
        return num
         
    for first_secret in secret_numbers:
        secret_numbers[first_secret] = (
            list(accumulate(
                repeat(C, 2000),
                nextgen,
                initial = first_secret
            ))
        )
        secret_numbers[first_secret] = [
            n%10 for n in secret_numbers[first_secret]
        ]
        differences[first_secret] = [
            y - x for x, y in pairwise(secret_numbers[first_secret])
        ]

    # print(differences)
    # print(secret_numbers)

    def check_validity(seq: list[int]) -> bool:
        for i in range(1, len(seq)+1):
            for j in range(len(seq)-i+1):
                if abs(sum(seq[j:(j+i)])) >= 10:
                    return False
        return True
    # print(check_validity([1,2,3,3]), check_validity([3,3,3,3]))
    sequences = list(
        filter(check_validity, # most sequences are impossible
            product(range(-9, 10), range(-9, 10), 
                    range(-9, 10), range(-9, 10))
        )
    )
    n_bananas: dict[tuple[int, int, int, int], int] = dict.fromkeys(sequences, 0)
    for num, diff in differences.items():
        saleseq = set()
        for i in range(len(diff)-4):
            t = tuple(diff[i:(i+4)])
            if t not in saleseq:
                n_bananas[t] += secret_numbers[num][i+4]
                saleseq.add(t)

    print(time()-t0)
    return max(n_bananas.values())
  

if __name__ == '__main__':
    with open('22-dec-2024-input.txt') as data_input:
        secrets = [int(num.strip()) for num in data_input.readlines()]
    print(task_1(secrets))
    print(task_2(secrets))