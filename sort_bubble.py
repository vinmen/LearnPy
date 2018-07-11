def bubble_sort(data):
    n = len(data)
    swapped = False
    while not swapped:
        swapped = True
        for i in range(n):
            if data[i-1] > data[i]:
                temp = data[i]
                data[i] = data[i-1]
                data[i-1] = temp
                swapped = False
        n = n-1
    
    print(data)

data = [1, 50, 3, 8, 9, 7, 12, 6]
bubble_sort(data)