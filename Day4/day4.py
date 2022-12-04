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
        start1, stop1 = first.split('-')
        start2, stop2 = second.split('-')
        if (int(start1) >= int(start2) and int(stop1) <= int(stop2)) or (int(start1) <= int(start2) and int(stop1) >= int(stop2)):
            count += 1
    return count

def overlap(lines):
    count = 0
    for line in lines:
        first, second = line.strip().split(',')
        start1, stop1 = first.split('-')
        start2, stop2 = second.split('-')
        if (int(start1) >= int(start2) and int(start1) <= int(stop2)) or (int(start2) >= int(start1) and int(start2) <= int(stop1)):
            count += 1
    return count

if __name__ == "__main__":
    lines = read_file(filename)
    print(fully_contained(lines))
    print(overlap(lines))
    