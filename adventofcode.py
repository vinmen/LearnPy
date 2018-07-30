
with open("adventofcode.txt") as f:
    data = f.read().splitlines()

#data = ['x LSHIFT 2 -> y']

# in_1, in_2, out, gate, signal

circuits = []
for line in data:
    in_1 = ""
    in_2 = ""
    out = ""
    gate = ""
    signal = ""

    if line.find("AND") > -1:        
        in_1 = line[0:line.find(" AND")]
        in_2 = line[line.find(" AND") + 5:line.find(" ->")]
        gate = "&"   
    elif line.find("OR") > -1:
        in_1 = line[0:line.find(" OR")]
        in_2 = line[line.find(" OR") + 4:line.find(" ->")]
        gate = "|"
    elif line.find("LSHIFT") > -1:
        in_1 = line[0:line.find("SHIFT") - 2]
        in_2 = line[line.find("SHIFT") + 6:line.find(" ->")]
        gate = "<<"
    elif line.find("RSHIFT") > -1:
        in_1 = line[0:line.find("SHIFT") - 2]
        in_2 = line[line.find("SHIFT") + 6:line.find(" ->")]
        gate = ">>"
    elif line.find("NOT") > -1:        
        in_1 = line[line.find("NOT") + 4:line.find(" ->")]
        gate = "~"
    else:
        if line.find("a") > -1:
            in_1 = line[0:line.find(" ->")]
        else:
            signal = line[0:line.find(" ->")]

    out = line[line.find("->") + 3:]
    circuits.append([in_1, in_2, out, gate, signal])

for item in circuits:
    if item[4] != '':
        print(item)


def find_signal(data):
    if data[4] != '':
        for item in data:
            if item[0] == item:
                pass
    else:
        pass



