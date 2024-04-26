current_floor = 0

with open('input.txt') as file:
    for line in file.readlines():
        for character in line.strip():
            if character == '(':
                current_floor += 1
            else:
                current_floor -= 1
print(current_floor)
