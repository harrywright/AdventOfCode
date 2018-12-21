logs = [line.strip() for line in open("input.txt", 'r').readlines()]

logs = sorted(logs)

guard = None
date = None
first = True

for log in logs:
    entry = log.split()
    
    if entry[3][0] == '#':
        if not first:
            state = '.' * 60
            flag = True
            for i in sleep:
                if flag:
                    state = state[:i] + '#'  * (60 - i)
                else:
                    state = state[:i] + '.' * (60 - i)
                flag = not flag
            print(date, guard, state)
        guard = entry[3][1:]
        sleep = []
        first = False
        continue
    
    date = entry[0][1:]
    minute = int(entry[1][3:5])
    
    if entry[2] in ('falls','wakes'):
        sleep.append(minute)
    
    #print(date, guard, sleep, log)

state = '.' * 60
flag = True
for i in sleep:
    if flag:
        state = state[:i] + '#'  * (60 - i)
    else:
        state = state[:i] + '.' * (60 - i)
    flag = not flag
print(date, guard, state)

