# Shortest Job First
# programs = [['p1', 4, 1], ['p2', 2, 1], ['p3', 6, 0]]

programs = []
num_programs = int(input("Enter the number of programs: "))
for i in range(num_programs):
    name = f'p{i+1}'
    EX2 = int(input(f"Enter the Execution time of program {i+1}: "))
    EN = int(input(f"Enter the Entrance of program {i+1}: "))

    program = [name, EX2, EN]
    programs.append(program)

# print(programs)
programs_sorted = sorted(programs, key=lambda x: (x[2], x[1]))
# print(f'Sorted: {programs_sorted}')

SX1 = 0

for program in programs_sorted:
    # print(program)
    program.append(SX1)
    program.append(SX1+program[1])
    SX1 += program[1]

# print(programs_sorted)
for program in programs_sorted:
    name = program[0]
    print(f'{name} --EX--> {program[3]} to {program[4]}  (EX Time: {program[1]}, EN Time: {program[2]})')

average_en = 0
average_ex = 0
for i in range(len(programs_sorted)):
    program = programs_sorted[i]
    print(program)
    average_en += (program[3] - program[2])
    average_ex += (program[4] - program[2])

print(f'Average Waiting Time: {average_en}/{len(programs)} = {average_en/len(programs)}\nAverage Execution Time: {average_ex}/{len(programs)} = {average_ex/len(programs)}')
