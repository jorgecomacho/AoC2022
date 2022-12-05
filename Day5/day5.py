filename = 'day5.txt'
#filename = 'test.txt'

def read_file(fname):
    f = open(fname,"r")
    lines = f.readlines()
    return lines

def build_stacks(lines):
    endline = 0
    while len(lines[endline]) > 1:
        endline+=1
    temp = {}
    for c in range(1, len(lines[endline-1]), 4):
        temp[lines[endline-1][c]] = []
    endline -= 1
    for i in range(endline-1, -1, -1):
        for j in range(1, len(lines[i]), 4):
            if lines[i][j] != ' ':
                temp[str(j/4 +1)].append(lines[i][j])
    return temp, endline + 2

def parse_instruct(stacks, index, lines):
    for i in range(index, len(lines)):
        command = lines[i].strip().split()
        count = int(command[1])
        source = command[3]
        dest = command[5]
        for j in range(count):
            stacks[dest].append(stacks[source].pop())
    return stacks

def parse_modified(stacks, index, lines):
    for i in range(index, len(lines)):
        command = lines[i].strip().split()
        count = int(command[1])
        source = command[3]
        dest = command[5]
        stacks[dest] += stacks[source][count*-1:]
        for j in range(count):
            stacks[source].pop()
    return stacks

def print_last(stacks):
    tops = ''
    for i in range(len(stacks)):
        tops += stacks[str(i+1)].pop()
    print(tops)

if __name__ == "__main__":
    lines = read_file(filename)
    stacks, i = build_stacks(lines)
    #print_last(parse_instruct(stacks, i, lines))
    print_last(parse_modified(stacks, i, lines))
    