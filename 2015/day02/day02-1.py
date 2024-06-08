wrapping_paper_needed = 0

with open('/home/filip/Workspace/advent_of_code/2015/day02/input.txt') as file:
    for line in file.readlines():
        l, w, h = dimensions = [int(element) for element in line.split('x')]
        smallest_side = min([l*w, w*h, h*l])
        wrapping_paper_needed += 2*l*w + 2*w*h + 2*h*l + smallest_side

print(wrapping_paper_needed)
# Result: 1588178
