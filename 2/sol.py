
def part1():
    with open("input.txt", 'r') as f:
        content = [x.strip().split() for x in f.readlines()]

    print(len(list(filter(lambda line: (int(line[0].split("-")[0]) <= line[2].count(line[1][0]) <= int(line[0].split("-")[1])), content))))

def part2():
    with open("input.txt", 'r') as f:
        content = [x.strip().split() for x in f.readlines()]

    print(len(list(filter(lambda line: sum([line[1][0] == line[2][index] for index in [int(x)-1 for x in line[0].split("-")]]) == 1, content))))