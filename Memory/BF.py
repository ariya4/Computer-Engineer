# Best Fit
memory = [[40, 0], [25, 1], [45, 2], [50, 3], [60, 4], [40, 5]]
memory_update = memory.copy()

# program_lst = [('p1', 20), ('p2', 30), ('p3', 20), ('p4', 35)]

program_lst = []
num = int(input(f'How many inputs: '))
for i in range(num):
    name = input('Enter new name: ')
    value = int(input(f'Enter size of {name}: '))
    program = (name, value)
    program_lst.append(program)

print(f'\nProgram list: {program_lst}')
for i in range(len(program_lst)):
    print(f'\nMemory: {memory_update}')
    memory_update = sorted(memory_update, key=lambda x: abs(x[0] - program_lst[i][1]))
    print(f'sorted memory: {memory_update}')
    for j in range(len(memory_update)):
        if program_lst[i][1] <= memory_update[j][0]:
            print(f'{program_lst[i][0]} (size: {program_lst[i][1]}) -> {memory_update[j][0]} -->  remaining space = {memory_update[j][0] - program_lst[i][1]}')
            memory_update[j] = [memory_update[j][0] - program_lst[i][1], memory_update[j][1]]
            print(f'updated sorted memory: {memory_update}')
            memory_update = sorted(memory_update, key=lambda x: x[1])
            print(f'updated memory: {memory_update}\n')
            break
        else:
            print(f"{program_lst[i][0]} (size: {program_lst[i][1]}) -> {memory_update[j][0]}: Not Suitable")
