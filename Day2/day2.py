filename = 'day2.txt'

def read_file(fname):
    f = open(fname,"r")
    lines = f.readlines()
    return lines

def check(lines):
    action = {'X':1, 'Y':2, 'Z':3}
    outcome = {'AX':3, 'AY':6, 'AZ':0,
               'BX':0, 'BY':3, 'BZ':6,
               'CX':6, 'CY':0, 'CZ':3}
    sum = 0
    for line in lines:
        temp_line = line.strip().split(" ")
        them = temp_line[0]
        me = temp_line[1]
        sum += action[me] + outcome[them + me]
    
    return sum

def mod_check(lines):
    result = {'X':0, 'Y':3, 'Z':6}
    outcome = {'AX':3, 'AY':1, 'AZ':2,
               'BX':1, 'BY':2, 'BZ':3,
               'CX':2, 'CY':3, 'CZ':1}
    sum = 0
    for line in lines:
        temp_line = line.strip().split(" ")
        them = temp_line[0]
        me = temp_line[1]
        sum += result[me] + outcome[them + me]
    
    return sum

if __name__ == "__main__":
    lines = read_file(filename)
    print(check(lines))
    print(mod_check(lines))
    