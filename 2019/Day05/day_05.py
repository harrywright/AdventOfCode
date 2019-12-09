from typing import List


def run_program(program: List[int]) -> List[int]:
    step = 0
    opcode = 0

    while opcode != 99:
        opcode = program[step] % 100
        parmode = program[step] // 100

        param_1_mode = parmode % 10
        param_2_mode = parmode // 10 % 10
        param_3_mode = parmode // 100 % 10

        if opcode == 1:  # addition
            param_1 = program[step + 1] if param_1_mode else program[program[step + 1]]
            param_2 = program[step + 2] if param_2_mode else program[program[step + 2]]
            param_3 = program[step + 3]

            program[param_3] = param_1 + param_2
            step += 4

        elif opcode == 2:  # multiplication
            param_1 = program[step + 1] if param_1_mode else program[program[step + 1]]
            param_2 = program[step + 2] if param_2_mode else program[program[step + 2]]
            param_3 = program[step + 3]

            program[param_3] = param_1 * param_2
            step += 4

        elif opcode == 3:  # Input
            param_1 = program[step + 1]

            data_input = input("Input:")
            program[param_1] = int(data_input)
            step += 2

        elif opcode == 4:  # Output
            param_1 = program[step + 1] if param_1_mode else program[program[step + 1]]

            print(f'Output: {param_1}')
            step += 2

        elif opcode == 5:  # jump-if-true
            param_1 = program[step + 1] if param_1_mode else program[program[step + 1]]
            param_2 = program[step + 2] if param_2_mode else program[program[step + 2]]

            if param_1:
                step = param_2
            else:
                step += 3

        elif opcode == 6:  # jump-if-false
            param_1 = program[step + 1] if param_1_mode else program[program[step + 1]]
            param_2 = program[step + 2] if param_2_mode else program[program[step + 2]]

            if not param_1:
                step = param_2
            else:
                step += 3

        elif opcode == 7:  # less than
            param_1 = program[step + 1] if param_1_mode else program[program[step + 1]]
            param_2 = program[step + 2] if param_2_mode else program[program[step + 2]]
            param_3 = program[step + 3]

            program[param_3] = 1 if param_1 < param_2 else 0
            step += 4

        elif opcode == 8:  # equals
            param_1 = program[step + 1] if param_1_mode else program[program[step + 1]]
            param_2 = program[step + 2] if param_2_mode else program[program[step + 2]]
            param_3 = program[step + 3]

            program[param_3] = 1 if param_1 == param_2 else 0
            step += 4

    return program


with open('input.txt', 'r') as f:
    initial_data = f.readline().split(',')
    initial_data = [int(i) for i in initial_data]


data = initial_data.copy()
run_program(data)


# print(run_program([3, 0, 4, 0, 99]))

# print(run_program([1002, 4, 3, 4, 33]))

#print(run_program([3, 9, 8, 9, 10, 9, 4, 9, 99, -1, 8]))
