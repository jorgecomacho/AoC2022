filename = 'day11.txt'
#filename = 'test.txt'

import copy, os

def read_file(fname):
    directory = os.path.dirname(os.path.realpath(__file__))
    full_path = '/'.join([directory, fname])
    f = open(full_path,"r")
    lines = [i.strip() for i in f.readlines()]
    return lines

def monkey_parts(lines):
    monkeys = []
    master_divisor = 1
    for i in range(1, len(lines), 7):
        temp_dict = {}
        temp_dict['items'] = [int(x) for x in lines[i].split(': ')[1].split(', ')]
        temp_dict['op'] = eval(f'lambda old: {lines[i+1].split("= ")[1]}')
        temp_dict['divisor'] = int(lines[i+2].split()[-1])
        master_divisor *= temp_dict['divisor']
        temp_dict['true'] = int(lines[i+3].split()[-1])
        temp_dict['false'] = int(lines[i+4].split()[-1])
        temp_dict['count'] = 0
        monkeys.append(temp_dict)
    return monkeys, master_divisor

def show_me_the_monkey(monkeys):
    counts = []
    for monkey in monkeys:
        for entry in monkey.keys():
            print(f'{entry}: {monkey[entry]}')
        print()
        counts.append(monkey['count'])
    counts.sort()
    print(counts[-1] * counts[-2])

def do_monkey_stuff(monkeys, mega_mod=None, divisor=1):
    for monkey in monkeys:
        for item in monkey['items']:
            monkey['count'] += 1
            new = monkey['op'](item)
            new = int(new / divisor)
            if mega_mod:
                new %= mega_mod
            test = new % monkey['divisor'] == 0
            if test:
                monkeys[monkey['true']]['items'].append(new)
            else:
                monkeys[monkey['false']]['items'].append(new)
        for i in range(len(monkey['items'])):
            monkey['items'].pop(0)
    return monkeys

if __name__ == "__main__":
    lines = read_file(filename)
    part1, _ = monkey_parts(lines)
    for i in range(20):
        part1 = do_monkey_stuff(part1, divisor=3)
    show_me_the_monkey(part1)

    part2, master = monkey_parts(lines)
    for i in range(10000):
        part2 = do_monkey_stuff(part2, mega_mod=master)
    show_me_the_monkey(part2)
