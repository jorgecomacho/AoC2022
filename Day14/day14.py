filename = 'day14.txt'
#filename = 'test.txt'

import os

def read_file(fname):
    directory = os.path.dirname(os.path.realpath(__file__))
    full_path = '/'.join([directory, fname])
    f = open(full_path,"r")
    lines = [i.strip() for i in f.readlines()]
    return lines

def make_grid(lines):
    grid = [['.']*1000 for i in range(500)]
    max_y = 0
    for line in lines:
        pairs = line.split(' -> ')
        for i in range(len(pairs) - 1):
            x_start, y_start = [int(q) for q in pairs[i].split(',')]
            x_end, y_end = [int(q) for q in pairs[i+1].split(',')]
            if x_start == x_end:
                if y_start > y_end:
                    y_end -= 1
                    y_inc = -1
                else:
                    y_end += 1
                    y_inc = 1
                for j in range(y_start, y_end, y_inc):
                    grid[j][x_start] = '#'
                    if j > max_y:
                        max_y = j
                continue
            if y_start == y_end:
                if y_start > max_y:
                    max_y = y_start
                if x_start > x_end:
                    x_end -= 1
                    x_inc = -1
                else:
                    x_end += 1
                    x_inc = 1
                for j in range(x_start, x_end, x_inc):
                    grid[y_start][j] = '#'
                continue
    for i in range(len(grid[0])):
        grid[max_y+2][i] = '#'
    return grid
    '''grid[0][500] = '+'
    for i in range(10):
        print(grid[i][494:])'''

def sand_drop(grid, x, y):
    if y+1 > len(grid) -1 or x-1 < 0 or x+1 > len(grid[0]):
        return True, grid
    if grid[y+1][x] == '.':
        return sand_drop(grid, x, y+1)
    if grid[y+1][x-1] == '.':
        return sand_drop(grid, x-1, y+1)
    if grid[y+1][x+1] == '.':
        return sand_drop(grid, x+1, y+1)
    grid[y][x] = 'O'
    if grid[y][x] == 'O' and y == 0:
        return True, grid
    return False, grid

def count_it(grid):
    i = 0
    done = False
    while not done:
        i+=1
        done, grid = sand_drop(grid, 500, 0)
    print(i)
        
'''def sand_drop(grid):
    while True:
        new_sand = [500, 0]
        i = 0
        while grid[i+1][500] == '.':
            i += 1'''


if __name__ == "__main__":
    lines = read_file(filename)
    #grid = [['.']*503 for i in range(10)]
    grid = make_grid(lines)
    for i in range(12):
        print(grid[i][494:505])
    count_it(grid)
    
    #print(grid)
    
