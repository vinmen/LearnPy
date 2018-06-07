def program():
    num_list = [100, 200, 300, 400, 500]

    print("for_loop :: " + str(for_loop(num_list)))
    print("while_loop :: " + str(while_loop(num_list)))
    print("recursion :: " + str(recursion(num_list)))

def for_loop(data):
    sum = 0    
    for i in data:        
        sum = sum + i        
    return sum

def while_loop(data):
    i = 0    
    sum = 0
    while(i < len(data)):        
        sum = sum + data[i]
        i += 1  
    return sum

def recursion(data):      
    if len(data) > 0:
        return data[0] + recursion(data[1:])
    else:
        return 0


if __name__ == "__main__":
    program()