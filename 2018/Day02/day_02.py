box_ids = [line.strip() for line in open("input.txt", 'r').readlines()]

twice = 0
thrice = 0

for box_id in box_ids:
    flag_2 = False
    flag_3 = False
    for char in box_id:
        if box_id.count(char) == 2:
            flag_2 = True
        if box_id.count(char) == 3:
            flag_3 = True
    if flag_2:
        twice += 1
    if flag_3:
        thrice += 1

print(twice * thrice)


for box_1 in box_ids:
    for box_2 in box_ids:
        differences = 0
        flag = None
        for i in range(len(box_1)):
            if box_1[i] != box_2[i]:
                differences += 1
                if differences > 1:
                    break
                else:
                    flag = i
        if differences == 1:
            print(box_1[:flag]+box_1[flag+1:])

