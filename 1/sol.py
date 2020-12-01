
with open("input.txt", 'r') as f:
    content = f.readlines()

content = [int(x.strip()) for x in content]

for i, one in enumerate(content):
    for j, two in enumerate(content[i:]):
        for k, three in enumerate(content[j:]):
            if sum([one,two,three]) == 2020:
                print(one*two*three)

# out = [one*two*three for i, one in enumerate(content) for j, two in enumerate(content[i:]) for k,three in enumerate(content[j:]) if (one + two + three == 2020)]
# print(out)