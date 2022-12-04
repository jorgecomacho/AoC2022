filename = 'day4.txt'
#filename = 'test.txt'


def read_file(fname):
    f = open(fname,"r")
    lines = f.readlines()
    return lines

def fully_contained(lines):
    count = 0
    for line in lines:
        first, second = line.strip().split(',')
        start1, stop1 = [int(i) for i in first.split('-')]
        start2, stop2 = [int(i) for i in second.split('-')]
        if start1 <= start2 <= stop2 <= stop1 or start2 <= start1 <= stop1 <= stop2:
            count += 1
    return count

def overlap(lines):
    count = 0
    for line in lines:
        first, second = line.strip().split(',')
        start1, stop1 = [int(i) for i in first.split('-')]
        start2, stop2 = [int(i) for i in second.split('-')]
        if start1 <= start2 <= stop1 or start2 <= start1 <= stop2:
            count += 1
    return count

if __name__ == "__main__":
    lines = read_file(filename)
    print(fully_contained(lines))
    print(overlap(lines))
    
