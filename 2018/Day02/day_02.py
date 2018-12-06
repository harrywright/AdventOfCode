box_ids = [line.strip() for line in open("input.txt", 'r').readlines()]

twice = 0
thrice = 0

for box_id in box_ids:
    print(sorted(box_id))
    flag_2 = False
    flag_3 = False
    for char in box_id:
        if box_id.count(char) == 2:
            flag_2 = True
        if box_id.count(char) == 3:
            flag_3 = True
        print(char + ": " + str(box_id.count(char)))
    if flag_2:
        twice += 1
        print("Twice!")
    if flag_3:
        thrice += 1
        print("Thrice!")

print(twice * thrice)



print(sorted(box_ids))


print(len(box_ids))

number_of_boxes = len(box_ids)
