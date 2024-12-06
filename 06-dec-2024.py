from copy import deepcopy
from itertools import chain

def task_1(labmap: list[list[str]]) -> list[list[str]] | str:
    lab = deepcopy(labmap)
    x, y = 0, 0
    for i, lat in enumerate(lab):
        for j, long in enumerate(lat):
            if lab[i][j] == '^':
                x, y = j, i
    direction = 0
    # print(len(lab), len(lab[0]))
    step_counter = 0
    while (x >= 0 and y >= 0 
           and x < len(lab[0]) and y < len(lab) 
           and step_counter < 8_000): # len(lab)*len(lab[0]):
        if lab[y][x] in ['#', 'O']:
            if direction == 0:
                y += 1  
            if direction == 1:
                x -= 1
            if direction == 2:
                y -= 1
            if direction == 3:
                x += 1
            direction = (direction + 1) % 4
            # print(direction)
        else:
            lab[y][x] = 'X'

        if direction == 0:
            y -= 1  
        if direction == 1:
            x += 1
        if direction == 2:
            y += 1
        if direction == 3:
            x -= 1
        step_counter += 1
    
    if step_counter >= 8_000: # len(lab)*len(lab[0]):
        return 'loop'
    return lab

def task_2(labmap: list[list[str]]) -> int:
    for i, lat in enumerate(labmap):
        for j, long in enumerate(lat):
            if labmap[i][j] == '^':
                first_step = (i, j)
    # print(first_step)
    route = task_1(labmap)
    eligibles_counter = 0
    steps = []
    for i, lat in enumerate(route):
        for j, long in enumerate(lat):
            if route[i][j] == 'X':
                steps.append((i, j))
    while first_step in steps:
        # print('crossing the start point')
        steps.remove(first_step)
    # print(steps)
    for idx, step in enumerate(steps):
        tmp = deepcopy(route)
        tmp[first_step[0]][first_step[1]]='^'
        y, x = step
        tmp[y][x] = 'O'
        # if idx<=2: print(tmp[:6])
        new_route = task_1(tmp)
        print((idx, new_route) if isinstance(new_route, str) else (idx, '-'))
        # print(idx, list(chain.from_iterable(new_route)).count('X'))
        if new_route == 'loop':
            eligibles_counter += 1
    return eligibles_counter



if __name__ == '__main__':
    with open('06-dec-2024-input.txt') as data_input:
        labmap = [list(lat.strip()) for lat in data_input.readlines()]
    print(list(chain.from_iterable(task_1(labmap))).count('X'))
    print(task_2(labmap))
