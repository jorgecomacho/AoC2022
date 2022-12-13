filename = 'day13.txt'
#filename = 'test.txt'

import os

def read_file(fname):
    directory = os.path.dirname(os.path.realpath(__file__))
    full_path = '/'.join([directory, fname])
    f = open(full_path,"r")
    lines = [i.strip() for i in f.readlines()]
    return lines

# so this didnt work with boolean for reasons i dont understand
'''def compare_lists_mod(left, right):
    if isinstance(left, int) and isinstance(right, int):
        print(left < right)     #This prints False for test 3
        return (left < right)   #This returns True for test 3
    if isinstance(left, int) and isinstance(right, list):
        return compare_lists_mod([left], right)
    if isinstance(left, list) and isinstance(right, int):
        return compare_lists_mod(left, [right])
    if isinstance(left, list) and isinstance(right, list):
        lens = sorted([len(left), len(right)])[0]
        for i in range(lens):
            temp = compare_lists_mod(left[i], right[i])
            if temp:
                return temp
        return len(left) < len(right)'''

def compare_listicles(left, right):
    if isinstance(left, int) and isinstance(right, int):
        return left - right 
    if isinstance(left, int) and isinstance(right, list):
        return compare_listicles([left], right)
    if isinstance(left, list) and isinstance(right, int):
        return compare_listicles(left, [right])
    if isinstance(left, list) and isinstance(right, list):
        lens = sorted([len(left), len(right)])[0]
        for i in range(lens):
            temp = compare_listicles(left[i], right[i])
            if temp:
                return temp
        return len(left) - len(right)


def parse_lines(lines):
    index = 0
    right_order = []
    master_list = [[[2]],[[6]]]
    for i in range(0, len(lines), 3):
        index += 1
        left = eval(lines[i])
        right = eval(lines[i+1])
        master_list.append(left)
        master_list.append(right)
        if compare_listicles(left, right) < 0:
            right_order.append(index)
    return right_order, master_list

def line_sort(master_list):
    indeces = []
    for i in range(len(master_list)):
        for j in range(i+1, len(master_list)):
            if compare_listicles(master_list[i], master_list[j]) < 0:
                continue
            else:
                temp = master_list[i]
                master_list[i] = master_list[j]
                master_list[j] = temp
        if master_list[i] == [[2]] or master_list[i] == [[6]]:
            indeces.append(i+1)
    return indeces[0] * indeces[1]

if __name__ == "__main__":
    lines = read_file(filename)
    correct, master = parse_lines(lines)
    print(sum(correct))
    print(line_sort(master))