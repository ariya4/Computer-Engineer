# Priority
import func

# programs = [['p1', 8, 3, 2],
#             ['p2', 2, 4, 0],
#             ['p3', 5, 1, 3],
#             ['p4', 3, 3, 1],
#             ]
programs = []
num_programs = int(input("Enter the number of programs: "))

for i in range(num_programs):
    name = f'p{i+1}'
    EX2 = int(input(f"Enter the Execution time of program {i+1}: "))
    priority = int(input(f"Enter the Priority of program {i+1}: "))
    EN = int(input(f"Enter the Entrance of program {i + 1}: "))
    print()
    program = [name, EX2, priority, EN]
    programs.append(program)

programs_sorted = func.ordering(programs)


SX1 = 0
for program in programs_sorted:
    program.append(SX1)
    program.append(SX1+program[1])
    SX1 += program[1]

print(end='\n\n')
for program in programs_sorted:
    print(f'{program[0]} --EX--> {program[4]} to {program[5]}  (EX Time: {program[1]}, Priority: {program[2]}, EN: '
          f'{program[3]})')


average_en = 0
average_ex = 0
for i in range(len(programs_sorted)):
    program = programs_sorted[i]
    average_en += program[4]
    average_ex += program[5]

print(f'Average Waiting Time: {average_en}/{len(programs_sorted)} = {average_en/len(programs_sorted)}'
      f'\nAverage Execution Time: {average_ex}/{len(programs_sorted)} = {average_ex/len(programs_sorted)}')
