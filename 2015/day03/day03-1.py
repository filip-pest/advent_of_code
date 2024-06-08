current_position = (0, 0)
visited_positions = {current_position}


def get_new_position(char, curr_pos):
    x, y = curr_pos
    match char:
        case '^':
            return x + 1, y
        case 'v':
            return x - 1, y
        case '>':
            return x, y + 1
        case '<':
            return x, y - 1
        case _:
            return x, y


with open('/home/filip/Workspace/advent_of_code/2015/day03/input.txt') as file:
    for line in file.readlines():
        for character in line.strip():
            new_position = get_new_position(character, current_position)
            if tuple(new_position) not in visited_positions:
                visited_positions.add(new_position)
            current_position = new_position

print(len(visited_positions))
# Result: 2592
