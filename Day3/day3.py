filename = 'day3.txt'

def read_file(fname):
    f = open(fname,"r")
    lines = f.readlines()
    return lines

def ruck_sackify(lines):
    common = ''
    for line in lines:
        half_1 = line[0:int(len(line)/2)]
        half_2 = line[int(len(line)/2):len(line)]
        for c in half_1:
            if c in half_2:
                common += c
                break
    return common

def group_rucking(lines):
    common = ''
    for i in range(0, len(lines), 3):
        for c in lines[i]:
            if c in lines[i+1] and c in lines[i+2]:
                common += c
                break
    return common

def summify(items):
    sum = 0
    for c in items:
        if ord(c) > 96:
            sum += ord(c) - 96
        else:
            sum += ord(c) - 38
    return sum

if __name__ == "__main__":
    lines = read_file(filename)
    part1 = ruck_sackify(lines)
    print(summify(part1))
    part2 = group_rucking(lines)
    print(summify(part2))