filename = 'day6.txt'

def read_file(fname):
    f = open(fname,"r")
    lines = f.readlines()
    return lines

def unique(lines, length):
    for i in range(length,len(lines[0])):
        match = True
        for c in lines[0][i-length:i]:
            if lines[0][i-length:i].count(c) > 1:
                match = False
                break
        if match:
            return i

if __name__ == "__main__":
    lines = read_file(filename)
    print(unique(lines, 4))
    print(unique(lines, 14))