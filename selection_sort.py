
def selection_sort(data):    
    
    for i in range(len(data)):    
        min_index = i
        for j in range(i, len(data)):  
            if data[j] < data[min_index]:
                min_index = j
                  
        data[i], data[min_index] = data[min_index], data[i]            

if __name__ == "__main__":
    data = [5, 4, 3, 1, 0, 9, 10, 11]
    selection_sort(data)
    print(data)
