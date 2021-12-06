import numpy as np
from scipy import sparse

claims = [line.strip().split(' ') for line in open("input.txt", 'r').readlines()]

# claims = [['#1', '@', '1,3:', '4x4'],
#        ['#2', '@', '3,1:', '4x4'],
#        ['#3', '@', '5,5:', '2x2']]

fabric = sparse.lil_matrix((1000, 1000), dtype=np.int8)


for claim in claims:
    overlap = False
    x = int(claim[2].split(',')[0])
    y = int(claim[2].split(',')[1][:-1])
    dx = int(claim[3].split('x')[0])
    dy = int(claim[3].split('x')[1])

    for i in range(x, x+dx):
        for j in range(y, y+dy):
            fabric[j, i] += 1


multiclaim = 0
for r in range(fabric.shape[0]):
    for c, d in zip(fabric.rows[r], fabric.puzzle_input[r]):
        if d > 1:
            multiclaim += 1
print(multiclaim)


no_overlap = set()
for claim in claims:
    flag = 0
    x = int(claim[2].split(',')[0])
    y = int(claim[2].split(',')[1][:-1])
    dx = int(claim[3].split('x')[0])
    dy = int(claim[3].split('x')[1])

    for i in range(x, x+dx):
        for j in range(y, y+dy):
            if fabric[j, i] > 1:
                flag = 1

    if flag == 0:
        no_overlap.add(claim[0])
print(no_overlap)

