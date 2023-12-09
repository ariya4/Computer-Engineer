# Shortest Job First
import func

programs = []
num_programs = int(input("Enter the number of programs: "))
for i in range(num_programs):
    name = f'p{i+1}'
    EX2 = int(input(f"Enter the Execution time of program {i+1}: "))
    EN = int(input(f"Enter the Entrance of program {i+1}: "))

    program = [name, EX2, EN]
    programs.append(program)

# programs = [['p1', 4, 0], ['p2', 2, 0], ['p3', 6, 0]]

programs_sorted = func.ordering(programs, True)
# print(programs_sorted)

SX1 = 0

for program in programs_sorted:
    program.append(SX1)
    program.append(SX1+program[1])
    SX1 += program[1]
# print(programs_sorted)

for program in programs_sorted:
    print(f'{program[0]} --EX--> {program[3]} to {program[4]}  (EX Time: {program[1]}, EN Time: {program[2]})')

average_en = 0
average_ex = 0
for program in programs_sorted:
    print(program)
    average_en += (program[3] - program[2])
    average_ex += (program[4] - program[2])

print(f'Average Waiting Time: {average_en}/{len(programs_sorted)} = {average_en/len(programs_sorted)}\nAverage '
      f'Execution Time: {average_ex}/{len(programs_sorted)} = {average_ex/len(programs_sorted)}')
