filename = 'day1.txt'

def read_file(fname):
    f = open(fname,"r")
    lines = f.readlines()
    return lines

def elfest_elf(lines):
    elves = []
    temp_list = []

    for line in lines:
        if len(line.strip()) > 0:
            temp_list.append(int(line.strip()))
        else:
            elves.append(sum(temp_list))
            temp_list = []
    
    elves.sort()
    top3 = sum(elves[-3:])

    return elves[-1], top3

if __name__ == "__main__":
    file_lines = read_file(filename)
    top_elf, top_3 = elfest_elf(file_lines)
    print(top_elf, top_3)
