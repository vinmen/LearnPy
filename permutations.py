
def swap(data, i, j):
    temp = data[i]
    data[i] = data[j]
    data[j] = temp

def permutations(data, i, j):
    if i == j:
        print(data)        
    else:       
        for x in range(i, j):            
            swap(data, x, i)            
            permutations(data, i + 1, j)
            swap(data, x, i)

if __name__ == "__main__":
    data = ['a', 'b', 'c']   
    permutations(data, 0, 3)   
    