from typing import List


def run_program(program: List[int]) -> List[int]:
    step = 0
    opcode = 0

    while opcode != 99:
        opcode = program[step] % 100
        parmode = program[step] // 100

        par_1_mode = parmode % 10
        par_2_mode = parmode // 10 % 10
        par_3_mode = parmode // 100 % 10

        if opcode == 1:
            program[program[step + 3]] = (program[program[step + 1]] if not par_1_mode else program[step + 1]) \
                                         + (program[program[step + 2]] if not par_2_mode else program[step + 2])
            step += 4
        elif opcode == 2:
            program[program[step + 3]] = (program[program[step + 1]] if not par_1_mode else program[step + 1]) \
                                         * (program[program[step + 2]] if not par_2_mode else program[step + 2])
            step += 4
        elif opcode == 3:
            data_input = input("Input:")
            program[program[step + 1]] = int(data_input)
            step += 2
        elif opcode == 4:
            print(f'Output: {program[step+1] if par_1_mode else program[program[step + 1]]}')
            step += 2
        elif opcode == 5: # jump-if-true
            pass

    return program


with open('input.txt', 'r') as f:
    initial_data = f.readline().split(',')
    initial_data = [int(i) for i in initial_data]

# Part 1
data = initial_data.copy()
# data[1] = 12
# data[2] = 2
print(f'Part 1: {run_program(data)}')
#
# # Part 2
# for i in range(0, 100):
#     for j in range(0, 100):
#         data = initial_data.copy()
#         data[1] = i
#         data[2] = j
#         if run_program(data)[0] == 19690720:
#             print(f'Part 2: {100*i+j}')


#print(run_program([3, 0, 4, 0, 99]))

#print(run_program([1002, 4, 3, 4, 33]))
