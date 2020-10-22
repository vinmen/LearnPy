with open("out_temp.txt") as f:
    data = f.read().splitlines()   

line_number = 0

for line in data:
    line_number = line_number + 1
    if line_number % 2 == 1 and not line.startswith("Municipality"):
        print(line_number)
        break