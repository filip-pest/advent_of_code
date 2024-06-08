ribbon_length_needed = 0

with open('/home/filip/Workspace/advent_of_code/2015/day02/input.txt') as file:
    for line in file.readlines():
        l, w, h = dimensions = [int(element) for element in line.split('x')]
        dimensions.sort()
        ribbon_length_needed += dimensions[0] * 2 + dimensions[1] * 2 + l*w*h

print(ribbon_length_needed)
# Result: 3783758
