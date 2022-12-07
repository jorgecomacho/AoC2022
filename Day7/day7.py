filename = 'day7.txt'
#filename = 'test.txt'

def read_file(fname):
    f = open(fname,"r")
    lines = f.readlines()
    return lines

def parse_dirs(lines):
    cwd = []
    dirs = {}
    last_cmd = ''

    for line in lines:
        if '$' in line:
            last_cmd = line.split()[1]
            if last_cmd == 'cd':
                dest = line.strip().split()[2]
                if dest == '..':
                    cwd.pop()
                    continue
                cwd.append(dest)
                dirs['/'.join(cwd)] = []
                continue
            continue
        if last_cmd == 'ls':
            entry = line.split()[0]
            for i in range(1, len(cwd)):
                dirs['/'.join(cwd[0:i])].append(entry)
            dirs['/'.join(cwd)].append(entry)
    return dirs

def dirsum(dirs):
    sum = 0
    for key in dirs.keys():
        tempsum = 0
        for item in dirs[key]:
            if item != 'dir':
                tempsum += int(item)
        if tempsum < 100000:
            sum += tempsum
    print(sum)

def make_way(dirs):
    big_enough = []
    total_used = 0
    for item in dirs['/']:
        if item != 'dir':
            total_used += int(item)
    for key in dirs.keys():
        tempsum = 0
        for item in dirs[key]:
            if item != 'dir':
                tempsum += int(item)
        if tempsum >= total_used + 30000000 - 70000000:
            big_enough.append(tempsum)
    print(sorted(big_enough)[0])


if __name__ == "__main__":
    lines = read_file(filename)
    d = parse_dirs(lines)
    dirsum(d)
    make_way(d)