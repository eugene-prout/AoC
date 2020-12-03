def part1():
    with open("input.txt", 'r') as f:
        content = [x.strip() for x in f.readlines()]

    index = 0
    tree_count = 0
    for line in content:
        while len(line) < index:
            line += line
        if line[index] == '#':
            tree_count += 1
        index += 3
        
    print(tree_count)

def part2():
    with open("input.txt", 'r') as f:
        content = [x.strip() for x in f.readlines()]

    routes = [[1,1],[3,1],[5,1],[7,1],[1,2]]
    total_tree = 1
    for route in routes:
        index = 0
        tree_count = 0
        for line in content[::route[1]]:
            while len(line)-1 < index:
                line += line
            if line[index] == '#':
                tree_count += 1

            index += route[0]
        total_tree *= tree_count
    
    print(total_tree)

part1()
part2()