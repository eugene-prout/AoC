
def part1():
    with open("input.txt", 'r') as f:
        content = [x.strip().split() for x in f.readlines()]

    counter = 0
    for line in content:
        lower, upper = [int(x) for x in line[0].split("-")]
        if (line[2].count(line[1][0]) in range(lower, upper+1)):
            counter += 1

    print(counter)

def part2():
    with open("input.txt", 'r') as f:
        content = [x.strip().split() for x in f.readlines()]

    counter = 0
    for line in content:
        positions = [int(x)-1 for x in line[0].split("-")]
        
        if sum([line[1][0] == line[2][index] for index in positions]) == 1:
            counter += 1

    print(counter)
