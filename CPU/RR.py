# Round Robin

# TS = 3
# programs = [['p1', 4, 0], ['p2', 2, 0], ['p3', 6, 0]]

programs = []
TS = int(input("Enter the time slice: "))
num_programs = int(input("Enter the number of programs you want: "))
print()
for i in range(num_programs):
    name = f'p{i+1}'
    execution_time = int(input(f"Enter the execution time of program {i + 1}: "))
    EN = int(input(f"Enter the Entrance of program {i + 1}: "))
    print()
    program = [name, execution_time, EN]
    programs.append(program)


programs = sorted(programs, key=lambda x: x[2])
length = len(programs)
current_time = 0
total = 0

while programs:
    program = programs.pop(0)
    name, execution_time = program[0], program[1]
    if execution_time > TS:
        execution_time -= TS
        print(f"{name} --> {TS} ms (Remaining time: {execution_time} ms)")
        program[1] = execution_time
        programs.append(program)
        current_time += TS
    else:
        print(f"{name} --> {execution_time} ms (Completed)")
        current_time += execution_time
        total += current_time
    print(f"Time passed: {current_time} ms\n")

print(f'Average Waiting Time: {total - current_time}/{length} = {(total - current_time)/length}'
      f'\nAverage Execution Time: {total}/{length} = {total/length}')
