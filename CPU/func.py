def ordering(lst, sjf=False):
    p_sorted = []
    entry = 0
    i = 0
    while len(lst) != 0:
        if sjf:
            programs_sorted = sorted(lst, key=lambda x: (not x[2] <= entry, x[1], x[2]))
        else:
            programs_sorted = sorted(lst, key=lambda x: (not x[3] <= entry, x[2], x[3]))
        p = programs_sorted[i]
        entry += p[1]
        lst.remove(p)
        p_sorted.append(p)
    return p_sorted

# lstp = [
#         ['p1', 3, 2, 0],
#         ['p2', 4, 0, 0],
#         ['p3', 1, 5, 0],
#         ['p4', 3, 1, 4],
#         ]
# print(ordering(lstp))
