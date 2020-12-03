
def part1():
    with open("input.txt", 'r') as f: 
        print(len(list(filter(lambda l: (int(l[0].split("-")[0]) <= l[2].count(l[1][0]) <= int(l[0].split("-")[1])), [x.strip().split() for x in f.readlines()]))))

def part2():
    with open("input.txt", 'r') as f: 
        print(len(list(filter(lambda l: sum([l[1][0] == l[2][index] for index in [int(x)-1 for x in l[0].split("-")]]) == 1, [x.strip().split() for x in f.readlines()]))))