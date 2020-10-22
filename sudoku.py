

def check_solved(data):
    for row in range(9):
        for col in range(9):
            if data[row][col] == 0:                
                return False, row, col  
    return True, 0, 0

def check_number_exists(data, row, col, number):
    for i in range(9):
        if data[row][i] == number or data[i][col] == number:
            return True
    
    if row <= 2:
        x1 = 0
        x2 = 2
    elif row <= 5:
        x1 = 3
        x2 = 5
    else:
        x1 = 6
        x2 = 8

    if col <= 2:
        y1 = 0
        y2 = 2
    elif col <= 5:
        y1 = 3
        y2 = 5
    else:
        y1 = 6
        y2 = 8

    for l in range(x1, x2 + 1):
        for k in range(y1, y2 + 1):
            if data[l][k] == number:
                return True

    return False

def solve_puzzle(data):  

    solved, row, col = check_solved(data)
    if solved:
        return True
    
    for number in range(1, 10):
        if not check_number_exists(data, row, col, number):
            data[row][col] = number

            if solve_puzzle(data):
                return True

            data[row][col] = 0
    return False

def print_puzzle(data):   
    for row in range(9):
        if row % 3 == 0:
            print("------------------------------")        
        for col in range(9):
            print(" " + str(data[row][col]) + " ", end='')
            if (col + 1) % 3 == 0: 
                print("|", end='')            
        print("")
    print("------------------------------", end='')

if __name__ == "__main__":
    input = [[0, 3, 0, 7, 4, 0, 0, 0, 0],
             [0, 6, 0, 0, 0, 2, 1, 0, 0],
             [0, 0, 0, 0, 0, 8, 0, 3, 0],
             [8, 0, 3, 0, 0, 0, 0, 0, 0],
             [9, 1, 0, 0, 0, 0, 0, 5, 4],
             [0, 0, 0, 0, 0, 0, 3, 0, 2],
             [0, 5, 0, 1, 0, 0, 0, 0, 0],
             [0, 0, 6, 9, 0, 0, 0, 7, 0],
             [0, 0, 0, 0, 5, 4, 0, 8, 0]]
    
    print("\nPuzzle:")
    print_puzzle(input)

    solve_puzzle(input)

    print("\nSolution:")
    print_puzzle(input)
