from itertools import batched

def task_1(key_and_locks: list[str]) -> int:
    """
    #####
    ###..
    #.#..
    ..#..
    .....
    .....
    """
    keys: list[str] = []
    locks: list[str] = []
    for kl in key_and_locks:
        if kl[0] == '#':
            locks.append(kl)
        else:
            keys.append(kl)
    counter = 0
    for key in keys:
        key_pattern = [
            col.count('#')-1 for col in [
                [row[i] for row in batched(key, 5)] for i in range(5)
            ]
        ]
        # print(key_pattern)
        for lock in locks:
            lock_pattern = [
                col.count('#')-1 for col in [
                    [row[i] for row in batched(lock, 5)] for i in range(5)
                ]
            ]
            # print(lock_pattern)   
            if max(sum(x) for x in zip(lock_pattern, key_pattern)) <= 5: 
                counter += 1
    return counter    

if __name__ == '__main__':
    with open('25-dec-2024-input.txt') as data_input:
        key_and_locks = data_input.read().strip().split('\n\n')
        key_and_locks = [kl.replace('\n', '') for kl in key_and_locks]
    print(task_1(key_and_locks))
