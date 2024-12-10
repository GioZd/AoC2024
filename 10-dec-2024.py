import tkinter as tk

BROWNS = [
    '#FEE2C5', '#F9C1A4', '#EDA287',
    '#DD856C', '#C96A55', '#B1503F',
    '#97392D', '#7B241D', '#5D1210', '#400400'
]
def value_to_color(value):
    return BROWNS[value]

def design_map(matrix: list[list[int]]) -> tk.Tk:
    root = tk.Tk()
    root.title("Heatmap")
    canvas = tk.Canvas(root, height=550, width=550)
    canvas.pack(padx=10, pady=10)
    rows = len(matrix)
    cols = len(matrix[0])
    cell_width = 550 // cols
    cell_height = 550 // rows
    for i, row in enumerate(matrix):
        for j, value in enumerate(row):
            color = value_to_color(value)
            x0, y0 = j * cell_width, i * cell_height
            x1, y1 = x0 + cell_width, y0 + cell_height
            canvas.create_rectangle(x0, y0, x1, y1, fill=color, outline='')
    return root


def task_1(matrix: list[list[int]]):
    root = design_map(matrix)
    trailheads: dict[tuple[int, int], list[list[tuple[int, int]]]] = dict()
    for i, lat in enumerate(matrix):
        for j, long in enumerate(lat): 
            if matrix[i][j] == 0:
                trailheads[(i, j)] = []
    # print(list(trailheads.keys()))
    def get_adjacents(p: tuple[int, int]) -> list[tuple[int, int]] | None:
        h = matrix[p[0]][p[1]]
        # print(h)
        adjacents = []
        if p[0] > 0 and matrix[p[0]-1][p[1]] == h+1:
            adjacents.append((p[0]-1, p[1]))
        if p[0] < len(matrix)-1 and matrix[p[0]+1][p[1]] == h+1:
            adjacents.append((p[0]+1, p[1]))
        if p[1] > 0 and matrix[p[0]][p[1]-1] == h+1:
            adjacents.append((p[0], p[1]-1))
        if p[1] < len(matrix[0])-1 and matrix[p[0]][p[1]+1] == h+1:
            adjacents.append((p[0], p[1]+1)) 
        # print(h, adjacents)    
        return adjacents
    
    counter = 0
    for th in trailheads:
        trail = [th]
        visited = {th}
        s = trail.copy()
        while s:
            last = s.pop(-1)
            adjs = get_adjacents(last)
            # print(adjs)
            forks = [(i, j) for i, j in adjs if (i, j) not in visited]
                    # if matrix[i][j] == h+1 and (i, j) not in visited]
            s.extend(forks)
            visited.add(last)
            if matrix[last[0]][last[1]] == 9:
                counter += 1

    print(counter)
    # root.mainloop()


def task_2(matrix: list[list[int]]):
    root = design_map(matrix)
    trailheads: dict[tuple[int, int], list[list[tuple[int, int]]]] = dict()
    for i, lat in enumerate(matrix):
        for j, long in enumerate(lat): 
            if matrix[i][j] == 0:
                trailheads[(i, j)] = []
    # print(list(trailheads.keys()))
    def get_adjacents(p: tuple[int, int]) -> list[tuple[int, int]] | None:
        h = matrix[p[0]][p[1]]
        # print(h)
        adjacents = []
        if p[0] > 0 and matrix[p[0]-1][p[1]] == h+1:
            adjacents.append((p[0]-1, p[1]))
        if p[0] < len(matrix)-1 and matrix[p[0]+1][p[1]] == h+1:
            adjacents.append((p[0]+1, p[1]))
        if p[1] > 0 and matrix[p[0]][p[1]-1] == h+1:
            adjacents.append((p[0], p[1]-1))
        if p[1] < len(matrix[0])-1 and matrix[p[0]][p[1]+1] == h+1:
            adjacents.append((p[0], p[1]+1)) 
        # print(h, adjacents)    
        return adjacents
    
    counter = 0
    for th in trailheads:
        trail = [th]
        visited = {th}
        q = trail.copy()
        while q:
            first = q.pop(0)
            adjs = get_adjacents(first) 
            q.extend(adjs)
            if matrix[first[0]][first[1]] == 9:
                counter += 1

    print(counter)
    # root.mainloop()

if __name__ == '__main__':
    with open('10-dec-2024-input.txt', 'r') as data_input:
        trails = data_input.readlines()
        trails = [list(map(int, lat.strip())) for lat in trails]
    task_1(trails)
    task_2(trails)
