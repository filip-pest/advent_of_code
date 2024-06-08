santa_position = (0, 0)
robo_santa_position = (0, 0)
visited_positions = {(0, 0)}
santa_turn = True


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
            new_position = get_new_position(character, santa_position) if santa_turn else get_new_position(
                character, robo_santa_position)
            if tuple(new_position) not in visited_positions:
                visited_positions.add(new_position)
            if santa_turn:
                santa_position = new_position
            else:
                robo_santa_position = new_position
            santa_turn = not santa_turn

print(len(visited_positions))
# Result: 2360
