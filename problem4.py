
def find_largest_number():
    data = [50, 2, 1, 9]    
    temp = ''
    temp2 = 0

    temp_list = []
    temp_list2 = []

    for i in data:        
        temp_list = list(data)
        temp_list.remove(i)
        for j in temp_list:            
            temp_list2 = list(temp_list)
            temp_list2.remove(j)
           
            a = temp_list2[0]
            b = temp_list2[1]
            temp = str(i) + str(j) +str(a) + str(b)
            if int(temp) > temp2:
                temp2 = int(temp)
            temp = str(i) + str(j) +str(b) + str(a)
            if int(temp) > temp2:
                temp2 = int(temp)
    
    print(temp2) 

def find_largest(data):  
    number = 0  
    temp2 = ''
    for i in range(len(data) - 1):  
        if i > 0:
            temp_number = data[i]
            data[i] = data[i + 1]
            data[i + 1] = temp_number

        temp_list = list(data)
        temp_list2 = list(temp_list)
        for j in range(len(temp_list2)):            
            temp = temp_list2[0]
            temp_list2.remove(temp)
            temp_list2.append(temp)
            temp2 = ''.join(str(x) for x in temp_list2)
            print(temp2)
            if int(temp2) > number:
                number = int(temp2)

    print(number)     
    
    


if __name__ == "__main__":
    find_largest_number()
    data = [50, 2, 1, 9]   
    find_largest(data)     
