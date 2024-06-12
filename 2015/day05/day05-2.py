vowels = {'a', 'e', 'i', 'o', 'u'}
disallowed_strings = {'ab', 'cd', 'pq', 'xy'}
nice_string_count = 0


def is_nice_string(line):
    if not any(line[i] == line[i + 2] for i in range(0, len(line) - 2)):
        return False
    if not any(line[i] + line[i+1] in line[i+2::] for i in range(0, len(line) - 1)):
        return False
    return True


with open('/home/filip/Workspace/advent_of_code/2015/day05/input.txt') as file:
    for line in file.readlines():
        if is_nice_string(line.strip()):
            nice_string_count += 1
print(nice_string_count)
# Result: 53
