
def factorial(num):
    output = 1
    if num == 1 or num == 0:
        return 1
    else:
        output = num * factorial(num - 1)    
    return output

if __name__ == "__main__":
    print(factorial(5))
