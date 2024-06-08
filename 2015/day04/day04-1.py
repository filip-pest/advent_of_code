import hashlib

with open('/home/filip/Workspace/advent_of_code/2015/day04/input.txt') as file:
    for line in file.readlines():
        key = line
        for i in range(0, 1000000):
            secret_key = key + str(i)
            result = hashlib.md5(secret_key.encode()).hexdigest()
            if result.startswith('00000'):
                print(i)

# Result: 254575
