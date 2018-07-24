
with open("adventofcode.txt") as f:
    data = f.read().splitlines()

total = 0
for item in data:
    sides = str(item).split("x")
    l = int(sides[0])
    w = int(sides[1])
    h = int(sides[2])

    area1 = l * w
    area2 = w * h
    area3 = l * h

    slack = area3

    if area1 < area2:
        if area1 < area3:
            slack = area1        
    else:
        if area2 < area3:
            slack = area2  

    total = total + 2 * area1 + 2 * area2 + 2 * area3 + slack


print(total)