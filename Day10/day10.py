filename = 'day10.txt'
#filename = 'test.txt'

def read_file(fname):
    f = open(fname,"r")
    lines = [i.strip() for i in f.readlines()]
    return lines

def compute_me(lines):
    reg_x = [1]
    for line in lines:
        if line == 'noop':
            reg_x.append(reg_x[-1])
            continue
        reg_add = int(line.split()[-1])
        reg_x.append(reg_x[-1])
        reg_x.append(reg_x[-1] + reg_add)
    sum = 0
    for i in range(19, len(reg_x), 40):
        sum += (i+1) * reg_x[i]
    print(sum)
    return(reg_x)

def dafuk(x):
    drawing = []
    for i in range(6):
        word = ''
        for j in range(40):
            if abs(x[i*40+j] - j) < 2:
                word += '#'
            else:
                word += '.'
        drawing.append(word)
    for line in drawing:
        print(line)     

if __name__ == "__main__":
    lines = read_file(filename)
    x = compute_me(lines)
    dafuk(x)

