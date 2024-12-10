def task_1(disk: str) -> int:
    ids = []
    for i, c in enumerate(disk):
        ids.extend([i//2]*int(c) if i%2 == 0 else ['.']*int(c))
    # print(ids[:100])
    i = 0
    j = len(ids) - 1
    while i < j:
        while i < j and ids[i] != '.':
            i += 1
        while i < j and ids[j] == '.':
            j -= 1
        ids[i], ids[j] = ids[j], ids[i]
    
    return sum(i*byte_id for i, byte_id in enumerate(ids) if byte_id != '.')  


def task_2(disk: str) -> int:
    memory = []
    ids = []
    for i, c in enumerate(disk):
        ids.extend([i//2]*int(c) if i%2 == 0 else ['.']*int(c))
        memory.extend([int(c)]*int(c))
    # print(ids[:100])
    # print(ids[-100:])
    # print(memory[:100])
    # 2333133121414131402
    # 00...111...2...333.44.5555.6666.777.888899
    # 0099.111...2...333.44.5555.6666.777.8888..
    # 0099.1117772...333.44.5555.6666.....8888..
    # 0099.111777244.333....5555.6666.....8888..
    # 00992111777.44.333....5555.6666.....8888..       
    # for idx in reversed(range(maxidx)):
    i = 0
    rightmost = len(ids) - 1
    maxidx = len(disk.strip())//2 + 1
    while maxidx > 0:
        i = 0
        j = rightmost
        while ids[j] == '.':
            # print(j, memory[j])
            j -= 1 # -= memory[j]
        span = memory[j]
        # print(f"{j=}, {ids[j]=}, {ids[j-span]=}, {span=}")
        while ids[i:(i+span)] != ['.']*span:
            # print(i, ids[i])
            i += 1
        if i < j-span+1:
            ids[i:(i+span)], ids[(j-span+1):(j+1)] = ids[(j-span+1):(j+1)], ids[i:(i+span)]
            memory[i:(i+span)] = memory[(j-span+1):(j+1)]
        else:
            rightmost = j-span
        # print(ids)
        maxidx -= 1
            
    # print(ids[:100])
    # print(ids[-100:])
    
    return sum(i*byte_id for i, byte_id in enumerate(ids) if byte_id != '.')   


if __name__ == '__main__':
    with open('09-dec-2024-input.txt', 'r') as data_input:
        disk = data_input.read().strip()
    print(task_1(disk))
    print(task_2(disk))