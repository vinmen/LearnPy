
def insertion_sort(data):
   
    for i in range(len(data)):        
        for j in range(i, 0, -1):
           if j > 0 and data[j] < data[j - 1]:
               data[j], data[j - 1] = data[j - 1], data[j]
    
if __name__ == "__main__":
    data = [2, 1, 6, 7, 4, 5]
    print(data)
    insertion_sort(data)
    print(data)