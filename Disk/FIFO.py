# First In First Out

# head_position = 52
# req_lst = [84, 6, 24, 48, 58, 12, 60]

req_lst = []
head_position = int(input("What's your head Position: "))
new_req = int(input('How many inputs? '))
for new in range(new_req):
    value = int(input('Enter new Request: '))
    req_lst.append(value)

print(head_position, end=' -> ')
for i in req_lst:
    print(f'{i} -> ', end='')

# -------------------------------

movement_counter = 0
print(f"\ninitiate: {head_position}")
for item in req_lst:
    movement = abs(item - head_position)
    movement_counter += movement
    head_position = item
    print(head_position, end=' -> ')
    print(f"movement: {movement}")

print(f"total movement: {movement_counter}")
