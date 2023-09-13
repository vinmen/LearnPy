
def merge_sort(data):
    n = len(data) // 2
    if n < 1:
        return data
    else:
        L = merge_sort(data[0:n])
        R = merge_sort(data[n:])
        return(merge(L, R))

def merge(L, R):
    output = []
    i = 0
    j = 0
    m = len(L)
    n = len(R)

    while i < m or j < n:
        if i == m:
            output.append(R[j])
            j = j + 1
        elif j == n:
            output.append(L[i])
            i = i + 1 
        elif L[i] <= R[j]:
            output.append(L[i])
            i = i + 1
        elif L[i] > R[j]:
            output.append(R[j])
            j = j + 1
    
    return output

if __name__ == "__main__":
    '''L = [2, 3, 6, 7]
    R = [1, 4, 5, 9]
    print(L)
    print(R)
    print(merge(L, R))    '''

    data = [5,7,1,2,4,3,9,8,6]
    print(data)
    print(merge_sort(data))
        