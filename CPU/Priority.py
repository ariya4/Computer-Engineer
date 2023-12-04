# Priority
# programs = [['p1', 4, 3], ['p2', 2, 6], ['p3', 6, 2]]


programs = []
num_programs = int(input("Enter the number of programs: "))

for i in range(num_programs):
    name = f'p{i+1}'
    EX2 = int(input(f"Enter the Execution time of program {i+1}: "))
    priority = int(input(f"Enter the Priority of program {i+1}: "))

    program = [name, EX2, priority]
    programs.append(program)

programs_sorted = sorted(programs, key=lambda x: x[2])
SX1 = 0

for program in programs_sorted:
    program.append(SX1)
    program.append(SX1+program[1])
    SX1 += program[1]

for program in programs_sorted:
    name = program[0]
    print(f'{name} --EX--> {program[3]} to {program[4]}  (EX Time: {program[1]}, Priority: {program[2]})')

print(programs_sorted)

average_en = 0
average_ex = 0
for i in range(len(programs_sorted)):
    program = programs_sorted[i]
    average_en += program[3]
    average_ex += program[4]

print(f'Average Waiting Time: {average_en}/{len(programs)} = {average_en/len(programs)}\nAverage Execution Time: {average_ex}/{len(programs)} = {average_ex/len(programs)}')
