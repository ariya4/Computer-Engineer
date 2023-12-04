# Aria Code
# DFA code

Q = ['q0', 'q1', 'q2']  # ! States
E = ['0', '1']  # ! Alphabet
F = ['q0', 'q2']  # ! final States
s = [['q1', 'q2'], ['q1', 'q0'], ['q1', 'q0']]  # ! Pattern


def AAA(q, end):
    natige.append(s[Q.index(q)][E.index(end)])
    return s[Q.index(q)][E.index(end)]


while 1 == 1:
    natige = [Q[0]]
    start = Q[0]
    reza = (input("what's the string bro: "))
    for i in reza:
        start = AAA(start, i)
    if natige[-1] in F:
        print('Accepted')
    else:
        print('Not Accepted')
    print(natige)