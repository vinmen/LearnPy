def problem5():
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9]   
    temp = '' 
    for x in range(1, 10):         
        temp = temp + str(x)              
        for y in range(3):
            if x < 9:
                if y == 0:
                    temp = temp + '+'
                elif y == 1:
                    temp = temp + '-'
                else:
                    temp = temp + str(x+1)
    print(temp)               

 #1[+-2]2[+-3]3[+-4]4[+-5]5[+-6]6[+-7]7[+-8]8[+-9]
problem5()