from itertools import combinations
from math import gcd

def task_1(field: list[list[str]]) -> int:
    antennas: dict[str, list[tuple[int, int]]] = dict()
    for i, row in enumerate(field):
        for j, col in enumerate(row):
            if field[i][j] != '.':
                try:
                    antennas[field[i][j]].append((i, j))
                except:
                    antennas[field[i][j]] = [(i, j)]
    antinodes: set[tuple[int, int]] = set()
    def check_validity(pos: tuple[int, int]):
        return all([
            int(pos[0]) == pos[0], 
            int(pos[1]) == pos[1], 
            pos[0] >= 0, pos[1] >= 0,
            pos[0] < len(field), pos[1] < len(field[0])
        ])
    for antenna, loc in antennas.items():
        for p, q in combinations(loc, 2):
            an1 = (p[0] - (q[0]-p[0]), p[1] - (q[1]-p[1])) 
            an2 = (q[0] + (q[0]-p[0]), q[1] + (q[1]-p[1])) 
            an3 = (p[0] + (q[0]-p[0])/3, p[1] + (q[1]-p[1])/3)
            an4 = (q[0] - (q[0]-p[0])/3, q[1] - (q[1]-p[1])/3)
            if check_validity(an1):
                antinodes.add(an1)
            if check_validity(an2):
                antinodes.add(an2)
            if check_validity(an3):
                antinodes.add(an3)
            if check_validity(an4):
                antinodes.add(an4)
    return len(antinodes)

def task_2(field: list[list[str]]) -> int:
    antennas: dict[str, list[tuple[int, int]]] = dict()
    for i, row in enumerate(field):
        for j, col in enumerate(row):
            if field[i][j] != '.':
                try:
                    antennas[field[i][j]].append((i, j))
                except:
                    antennas[field[i][j]] = [(i, j)]
    # print(antennas)
    antinodes: set[tuple[int, int]] = set()
    def check_validity(pos: tuple[int, int]):
        return all([ 
            pos[0] >= 0, pos[1] >= 0,
            pos[0] < len(field), pos[1] < len(field[0])
        ])
    for antenna, locations in antennas.items():
        for p, q in combinations(locations, 2):
            # if antenna == 'V':
            #     print(p,q)
            deltax = q[1] - p[1]
            deltay = q[0] - p[0]
            dx = deltax//gcd(abs(deltax), abs(deltay))
            dy = deltay//gcd(abs(deltax), abs(deltay))
            new_antinodes: set[tuple[int, int]] = {p}#, q}
            start = p
            while check_validity(start):
                # if antenna == 'V':
                #     print(start, dy, dx, new_antinodes)
                new_antinodes.add(start)
                start = (start[0]+dy, start[1]+dx)
            start = p
            while check_validity(start):
                # if antenna == 'V':
                #     print(start, dy, dx, new_antinodes)
                new_antinodes.add(start)
                start = (start[0]-dy, start[1]-dx)
            antinodes.update(new_antinodes)

    return len(antinodes)


if __name__ == '__main__':
    with open('08-dec-2024-input.txt') as data_input:
        field = data_input.readlines()
        field = [list(lat.strip()) for lat in field]
    # print(field)
    print(task_1(field))
    print(task_2(field))