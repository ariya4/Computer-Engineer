# Shortest Seek Time First

# req_lst = [84, 6, 24, 48, 58, 12, 60]
# head_position = 52

head_position = int(input("What's your head Position: "))
req_lst = []
new_req = int(input('How many inputs? '))
for new in range(new_req):
    value = int(input('Enter new Request: '))
    req_lst.append(value)


def get_sorted_diff(lst, head):
    sorted_diff_ls = sorted([(item, abs(item - head)) for item in lst], key=lambda x: x[1])
    print(sorted_diff_ls)
    return sorted_diff_ls[0][0], sorted_diff_ls[0][1]


total_movement = 0
while len(req_lst) > 0:
    dest, diff = get_sorted_diff(req_lst, head_position)
    print('this is print', dest, diff)
    print(f'{head_position} --> {dest} (movement: {diff})')
    total_movement += diff
    head_position = dest
    req_lst.remove(dest)

print(f'-------\ntotal movements: {total_movement}')
