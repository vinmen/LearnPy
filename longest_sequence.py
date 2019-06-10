

def longest_sequence(input):
    longest = 0
    count = 0
    for i in a:
        if i == '1':
            count = count + 1
            if count > 0 and count > longest:
                longest = count
        else:
            count = 0
    print(longest)

if __name__ == '__main__':
    a = '11011100011111'
    longest_sequence(a)
    

         