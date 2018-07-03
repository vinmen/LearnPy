def selection_sort(data):    
    for i in range(len(data) - 1):
        for j in range(i + 1, len(data)):
            if data[j] < data[i]:
                temp = data[i]
                data[i] = data[j]
                data[j] = temp   
    print(data)

if __name__ == "__main__":
    data = [100, 300, 600, 350, 800, 900, 125, 450, 50]
    selection_sort(data)
