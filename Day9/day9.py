filename = 'day9.txt'
#filename = 'test.txt'

def read_file(fname):
    f = open(fname,"r")
    lines = f.readlines()
    return lines

def this_blows(lines, followers):
    node = []
    for i in range(1+followers):
        node.append([[0,0]])
    for line in lines:
        direction, dist = line.split()
        for i in range(int(dist)):
            if direction == 'R':
                node[0].append([node[0][-1][0]+1,node[0][-1][1]])
            elif direction == 'L':
                node[0].append([node[0][-1][0]-1,node[0][-1][1]])
            elif direction == 'U':
                node[0].append([node[0][-1][0],node[0][-1][1]+1])
            elif direction == 'D':
                node[0].append([node[0][-1][0],node[0][-1][1]-1])
            for j in range(1, len(node)):
                node[j].append(move_tail(node[j-1][-1], node[j][-1]))
    
    res = []
    for i in node[-1]:
        if i not in res:
            res.append(i)
    print(len(res))


def move_tail(new_head, old_tail):
    if new_head[0] == old_tail[0]:
        if abs(new_head[1] - old_tail[1]) <= 1:
            return old_tail
        if new_head[1] - old_tail[1] > 1:
            return [old_tail[0], old_tail[1]+1]
        if new_head[1] - old_tail[1] < -1:
            return [old_tail[0], old_tail[1]-1]
    if new_head[1] == old_tail[1]:
        if abs(new_head[0] - old_tail[0]) <= 1:
            return old_tail
        if new_head[0] - old_tail[0] > 1:
            return [old_tail[0]+1, old_tail[1]]
        if new_head[0] - old_tail[0] < -1:
            return [old_tail[0]-1, old_tail[1]]
    x_offset = new_head[0] - old_tail[0]
    y_offset = new_head[1] - old_tail[1]
    if abs(x_offset) <= 1 and abs(y_offset) <= 1:
        return old_tail
    if x_offset > 0:
        x_offset = 1
    elif x_offset < 0:
        x_offset = -1
    if y_offset > 0:
        y_offset = 1
    elif y_offset < 0:
        y_offset = -1
    return [old_tail[0]+x_offset, old_tail[1]+y_offset]

if __name__ == "__main__":
    lines = [i.strip() for i in read_file(filename)]
    this_blows(lines, 1)
    this_blows(lines, 9)
   