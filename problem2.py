def combine(list1, list2):
    i = 0
    output = []

    for i in range(len(list1)):
        output.append(list1[i])       
        output.append(list2[i])
        i = i + 1
    
    return output


if __name__ == "__main__":
    list1 = ['a', 'b', 'c']
    list2 = [1, 2, 3]
    
    print(combine(list1, list2))
