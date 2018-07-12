
def bubble_sort(data):
    for i in range(len(data)):
        for j in range(1, len(data) - i):
             if data[j-1] > data[j]:
                temp = data[j]
                data[j] = data[j-1]
                data[j-1] = temp
    print(data)            
   
if __name__ == "__main__":
    data = [4, 3, 2, 1]
    bubble_sort(data)