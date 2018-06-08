def find_large_number():
    data = [50, 1, 2, 9]
    temp = ''

    for i in range(len(data)):
        temp_list = list(data).remove(data[i])
        for j in temp_list:
            temp = temp + data[j]
