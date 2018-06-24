
def print_fib(): 
    a = 0
    b = 1 
    output = []
    output.append(a) 
    output.append(b)     

    for i in range(100): 
        temp = a
        a = b      
        b = temp + b
        output.append(a) 

    print(output)

if __name__ == "__main__":
    print_fib()
