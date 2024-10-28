def ordering(lst, sjf=False, priority=False):
    p_sorted = []
    entry = 0
    i = 0
    while len(lst) != 0:
        if sjf:
            programs_sorted = sorted(lst, key=lambda
                x: (not x[2] <= entry, x[1], x[2]))
        elif priority:
            programs_sorted = sorted(lst, key=lambda
                x: (not x[3] <= entry, x[2], x[3]))
        else:
            programs_sorted = sorted(lst, key=lambda
                x: (not x[1] <= entry, x[1]))

        p = programs_sorted[i]
        entry += p[1]
        lst.remove(p)
        p_sorted.append(p)
    return p_sorted
