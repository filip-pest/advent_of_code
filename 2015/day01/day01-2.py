current_floor = 0
character_position = 0

with open('input.txt') as file:
    for line in file.readlines():
        for character in line.strip():
            character_position += 1
            if character == '(':
                current_floor += 1
            else:
                current_floor -= 1
            if current_floor == -1:
                print(character_position)
                break
