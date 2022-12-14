filename = 'day8.txt'
#filename = 'test.txt'

def read_file(fname):
    f = open(fname,"r")
    lines = f.readlines()
    return lines

def DOYOUSEE(lines):
    max_score = 0
    visible_count = len(lines) * 2 + (len(lines[0]) - 2) * 2
    for i in range(1, len(lines) - 1):
        for j in range(1, len(lines[i]) - 1):
            visible = {'up': True, 'down': True, 'left': True, 'right': True}
            count = [0, 0, 0, 0]
            value = int(lines[i][j])
            for k in range(i-1, -1, -1): #up
                if int(lines[k][j]) >= value:
                    visible['up'] = False
                    count[0] += 1
                    break
                count[0] += 1
            for k in range(i+1, len(lines)): #down
                if int(lines[k][j]) >= value:
                    visible['down'] = False
                    count[1] += 1
                    break
                count[1] += 1
            for k in range(j-1, -1, -1): #left
                if int(lines[i][k]) >= value:
                    visible['left'] = False
                    count[2] += 1
                    break
                count[2] += 1
            for k in range(j+1, len(lines[i])): #right
                if int(lines[i][k]) >= value:
                    visible['right'] = False
                    count[3] += 1
                    break
                count[3] += 1
            if True in visible.values():
                visible_count += 1
            product = count[0]*count[1]*count[2]*count[3]
            if product > max_score:
                max_score = product
    print(visible_count)
    print(max_score)

if __name__ == "__main__":
    lines = [i.strip() for i in read_file(filename)]
    DOYOUSEE(lines)
