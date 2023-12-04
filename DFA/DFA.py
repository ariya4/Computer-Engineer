a = int(input("Enter number of states: "))
state = []
for i in range(0, a):
    state.append(input("Enter states in order: "))

b = int(input("Enter number of alphabets: "))
alphabet = []
for i in range(0, b):
    alphabet.append(input("Enter them: "))

c = int(input("How Many final states: "))
final_states = []
for i in range(0, c):
    final_states.append(input("Enter them: "))

d = [0 for i in range(len(state))]

for i in range(len(state)):
    d[i] = [0 for j in range(len(alphabet))]
    for j in range(len(alphabet)):
        d[i][j] = input(f'from {state[i]}  if  {alphabet[j]} go: ')


def machine(q, end):
    hello.append(d[state.index(q)][alphabet.index(end)])
    return d[state.index(q)][alphabet.index(end)]


while True:
    hello = []
    start = state[0]
    string = input("\nType the String to Check: ")
    for i in string:
        start = machine(start, i)
    if hello[-1] in final_states:
        print(f'ACCEPTED ( {state[0]} -->' + ' --> '.join(hello) + ' )')
    else:
        print(f'!! NOT ACCEPTED ( {state[0]} -->' + ' --> '.join(hello) + ' )')
