
def calculate_signal(circuits, item):
    for data in circuits:
        if data[0] != '' and data[0] == item[4]:
            data[2] = item[5]
        elif data[1] != '' and data[1] == item[4]:
            data[3] = item[5]

def run():
    with open("adventofcode.txt") as f:
        data = f.read().splitlines()
   
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
            gate = "-"
            if line.find("a") > -1:
                in_1 = line[0:line.find(" ->")]
            else:
                signal = line[0:line.find(" ->")]

        out = line[line.find("->") + 3:]
        circuits.append([in_1, in_2, "", "", out, signal, gate])

    for item in circuits:
        if item[5] != '':
            calculate_signal(circuits, item)

    for item in circuits:
        print(item)


if __name__ == "__main__":
    run()
    