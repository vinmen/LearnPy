
def binary_search(data, search, start, end):   
    mid = (start + end) // 2  
    if search == data[mid]:
        return True
    elif start == mid:
        return False
    elif search < data[mid]:
        return binary_search(data, search, start, mid - 1)
    else:
        return binary_search(data, search, mid + 1, end)    

if __name__ == "__main__":
    data = []
    search = 998
    for i in range(1000):
        data.append(i)
    print(binary_search(data, search, 0, len(data) - 1))