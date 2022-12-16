#filename = 'day15.txt'
filename = 'test.txt'

import os

def read_file(fname):
    directory = os.path.dirname(os.path.realpath(__file__))
    full_path = '/'.join([directory, fname])
    f = open(full_path,"r")
    lines = [i.strip() for i in f.readlines()]
    return lines

def build_lists(lines):
    sensor = []
    beacon = []
    for line in lines:
        s_x = int(line.split('x=')[1].split(',')[0])
        s_y = int(line.split('y=')[1].split(':')[0])
        b_x = int(line.split('x=')[2].split(',')[0])
        b_y = int(line.split('y=')[2])
        sensor.append([s_x, s_y])
        beacon.append([b_x, b_y])
    return sensor, beacon

def gridify(sensor, beacon):
    x_shift = 2
    grid = [['.']*4000000 for i in range(4000000)]
    for a, b in zip(sensor, beacon):
        grid[a[1]][a[0] + x_shift] = 'S'
        grid[b[1]][b[0] + x_shift] = 'B'
        distance = abs(a[0] - b[0]) + abs(a[1] - b[1])
        for i in range(len(grid)):
            for j in range(-1*x_shift, len(grid[i])-x_shift):
                if grid[i][j+x_shift] == 'B' or grid[i][j+x_shift] == 'S':
                    continue
                if abs(j-a[0]) + abs(i-a[1]) <= distance:
                    grid[i][j+x_shift] = '#'
    print(grid[2000000].count('#'))

def count_it(sensor, beacon, row):
    line = ['.']*6000000
    x_shift = 0
    for a, b in zip(sensor, beacon):
        #print(a, b)
        if a[1] == row:
            line[a[0] + x_shift] = 'S'
        if b[1] == row:
            line[b[0] + x_shift] = 'B'
        distance = abs(a[0] - b[0]) + abs(a[1] - b[1])
        for i in range(-1*x_shift, len(line)-x_shift):
            if line[i+x_shift] == 'B' or line[i+x_shift] == 'S':
                continue
            #print(f'sensor: [{a[0]}, {a[1]}] beacon: [{b[0]}, {b[1]}] distance: {distance} overlap: {abs(i-a[0]) + abs(row-a[1])} index: {i}')
            if abs(i-a[0]) + abs(row-a[1]) <= distance:
                line[i+x_shift] = '#'
    #print(''.join(line), len(line))
    print(line.count('#'))

def count_it_harder(sensor, beacon, row):
    nums = []
    for a, b in zip(sensor, beacon):
        distance = abs(a[0] - b[0]) + abs(a[1] - b[1])
        if abs(a[1] - row) > distance:
            continue
        offset = abs(a[1] - row)
        nums += range(a[0]-distance + offset, a[0]+distance -offset +1)
    print(len(set(nums)))

if __name__ == "__main__":
    lines = read_file(filename)
    sensor, beacon = build_lists(lines)
    count_it_harder(sensor, beacon, 10)

    
    