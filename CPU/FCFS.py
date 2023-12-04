# First Come First Service

# programs = [('p1', 0, 4, 0, 4), ('p2', 4, 6, 1, 2), ('p3', 6, 12, 2, 6)]

programs = []
num_programs = int(input("Enter the number of programs: "))
EX1 = 0

for i in range(num_programs):
    name = f'p{i+1}'
    EX = int(input(f"Enter the Execution time of program {i + 1}: "))

    program = (name, EX1, EX1 + EX, i, EX)
    programs.append(program)
    EX1 += EX

for program in programs:
    name = program[0]
    print(f'{name} --EX--> {program[1]} to {program[2]}  (EX Time: {program[4]}, EN Time: {program[3]})')

average_en = 0
average_ex = 0
for i in range(len(programs)):
    program = programs[i]
    average_ex += (program[2] - program[3])
    average_en += (program[1] - program[3])


print(f'Average Waiting Time: {average_en}/{len(programs)} = {average_en/len(programs)}\nAverage Execution Time: {average_ex}/{len(programs)} = {average_ex/len(programs)}')
# programs_sorted = sorted(programs, key=lambda x: x[2])
