# C-Scan

head_position = 52
req_lst = [84, 6, 24, 48, 58, 12, 60]

# head_position = int(input("What's your head Position: "))
# req_lst = []
# new_req = int(input('How many inputs? '))
# for new in range(new_req):
#     value = int(input('Enter new Request: '))
#     req_lst.append(value)

req_lst.extend([0, 99])
req_lst.sort()
index = None
for i in req_lst:
    if i >= head_position:
        index = req_lst.index(i)
        break
len_R = len(req_lst)
req_lst1 = req_lst[0:index:]
# req_lst1.reverse()
req_lst2 = req_lst[index:len_R:]
req_lst2.extend(req_lst1)


total_movement = 0
for i in req_lst2:
    movement = abs(head_position - i)
    print(f'{head_position} -> {i}  (movement: {movement})')
    head_position = i
    total_movement += movement

print(f'-------\ntotal movements: {total_movement}')
