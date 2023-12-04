# Round Robin

TS = 3
programs = [['p1', 4], ['p2', 2], ['p3', 6]]

# programs = []
# TS = int(input("Enter the time slice: "))
# num_programs = int(input("Enter the number of programs you want: "))
# for i in range(num_programs):
#     name = f'p{i+1}'
#     execution_time = int(input(f"Enter the execution time of program {i + 1}: "))
#     program = [name, execution_time]
#     programs.append(program)


programs_copy = programs.copy()
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

print(f'Sum of the programs completed time: {total}')
print(f'Average Waiting Time: {total - current_time}/{len(programs_copy)} = {(total - current_time)/len(programs_copy)}\nAverage Execution Time: {total}/{len(programs_copy)} = {total/len(programs_copy)}')
