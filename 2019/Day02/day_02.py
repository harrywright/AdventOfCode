from typing import List


def run_program(program: List[int]) -> List[int]:
    step = 0
    while program[step] != 99:
        if program[step] == 1:
            program[program[step+3]] = program[program[step+1]] + program[program[step+2]]
        elif program[step] == 2:
            program[program[step+3]] = program[program[step+1]] * program[program[step+2]]
        step += 4
    return program


with open('input.txt', 'r') as f:
    initial_data = f.readline().split(',')
    initial_data = [int(i) for i in initial_data]

# Part 1
data = initial_data.copy()
data[1] = 12
data[2] = 2
print(f'Part 1: {run_program(data)[0]}')

# Part 2
for i in range(0, 100):
    for j in range(0, 100):
        data = initial_data.copy()
        data[1] = i
        data[2] = j
        if run_program(data)[0] == 19690720:
            print(f'Part 2: {100*i+j}')
