# First Fit
memory = [40, 25, 45, 50, 60, 40]
memory_update = memory.copy()

# program_lst = [('p1', 20), ('p2', 30), ('p3', 20), ('p4', 35)]

program_lst = []
num = int(input(f'How many inputs: '))
for i in range(num):
    name = input('Enter new name: ')
    value = int(input(f'Enter size of {name}: '))
    program = (name, value)
    program_lst.append(program)


for i in range(len(program_lst)):
    print(f'memory: {memory_update}')
    for j in range(len(memory_update)):
        if program_lst[i][1] <= memory_update[j]:
            print(f'{program_lst[i][0]} (size: {program_lst[i][1]}) -> {memory_update[j]} (item {int(memory_update.index(memory_update[j])) + 1} in memory) -->  remaining space = {memory_update[j] - program_lst[i][1]}')
            memory_update[j] = memory_update[j] - program_lst[i][1]
            print(f'updated memory: {memory_update}\n')
            break
        else:
            print(f"{program_lst[i][0]} (size: {program_lst[i][1]}) -> {memory_update[j]}: Not Suitable")
