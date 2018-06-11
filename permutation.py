
def swap(data, i, j):
    temp = data[i]
    data[i] = data[j]
    data[j] = temp


def permutation(data, i, j):
    if i == j:
        print(data)
    else:
        print(data)
        for x in range(i, j + 1):            
            swap(data, x, i)            
            permutation(data, i + 1, j)
            swap(data, x, i)


if __name__ == "__main__":
    data = ['A', 'B', 'C']
    permutation(data, 0, 2)
       