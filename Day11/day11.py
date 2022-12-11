#filename = 'day11.txt'
filename = 'test.txt'

import copy

def read_file(fname):
    f = open(fname,"r")
    lines = [i.strip() for i in f.readlines()]
    return lines

def parse_monkeys(lines):
    monkeys = []
    temp_dict = {}
    i = 0
    for line in lines:
        if 'Monkey' in line:
            i = int(line.split()[1].split(':')[0])
            continue
        if 'Starting items' in line:
            temp_dict['starting'] = [int(i) for i in line.split(': ')[1].split(', ')]
            continue
        if 'Operation' in line:
            temp_dict['op'] = line.split(': ')[1].split()[-2:]
            continue
        if 'Test' in line:
            temp_dict['divisor'] = int(line.split()[-1])
            continue
        if 'true' in line:
            temp_dict['true'] = int(line.split()[-1])
            continue
        if 'false' in line:
            temp_dict['false'] = int(line.split()[-1])
            temp_dict['inspect'] = 0
            monkeys.append(copy.deepcopy(temp_dict))
            continue
    return monkeys

def print_monkeys(monkeys):
    for monkey in monkeys:
        for i in monkey.keys():
            print(i, monkey[i])
        print()

def monkey_rounds(monkeys, worry_adjust):
    for i in range(len(monkeys)):
        for j in range(len(monkeys[i]['starting'])):
            worry = monkeys[i]['starting'][0]
            monkeys[i]['inspect'] += 1
            new = worry
            if '+' in monkeys[i]['op'][0]:
                new = worry + int(monkeys[i]['op'][1])
            elif 'old' == monkeys[i]['op'][1]:
                new = worry * worry
            else:
                new = worry * int(monkeys[i]['op'][1])
            #new = int(new/worry_adjust)
            if new % monkeys[i]['divisor'] == 0:
                monkeys[i]['starting'].pop(0)
                monkeys[monkeys[i]['true']]['starting'].append(new)
            else:
                monkeys[i]['starting'].pop(0)
                monkeys[monkeys[i]['false']]['starting'].append(new)
    return monkeys

def two_most(monkeys):
    tries = []
    for monkey in monkeys:
        tries.append(monkey['inspect'])
    tries.sort()
    print(tries[-1]*tries[-2])

if __name__ == "__main__":
    lines = read_file(filename)
    monkeys = parse_monkeys(lines)

    #for i in range(20):
    #   monkeys = monkey_rounds(monkeys,3) #monkey

    for j in range(100):
        for i in range(100):
            monkeys = monkey_rounds(monkeys,1) #monkey
        print(j)
    print_monkeys(monkeys)
    two_most(monkeys)

