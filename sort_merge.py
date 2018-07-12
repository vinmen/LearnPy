
def merge_sort(data, i, j):
    pass
    '''  
    output = []  
    if i >= j:
        return data
    else:

        mid = (i + j) / 2
        data1 = merge_sort(data, i, mid)
        data2 = merge_sort(data, mid + 1, j)
        output = merge(data1, data2)
    '''
def merge(data1, data2):
    pass

if __name__ == "__main__":
    data = [10, 50, 60, 80, 20, 50, 100, 90, 30, 70]    
    print(merge_sort(data, 0, len(data) - 1))
       