# program to print * triangle for a give number.

def triangle(number):    
    output = ""    
    for i in range(1, number + 1):           
        for j in range(number - i):
            output = output + " "            
        for k in range(i):
            output = output + "*" + " "                       
        output = output + "\n"        
    print(output)                                    
    

if __name__ == '__main__':
    triangle(int(input('Enter Row Count : ')))