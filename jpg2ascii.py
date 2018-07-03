from PIL import Image

def jpg2ascii():
    img = Image.open("man.jpg")
    pix = img.load()    
    data = []

    #data = ""
    print(img.size)

    for x in range(img.size[0]):     
        #data = data + "\n"  
        for y in range(img.size[1]):
            c = toGray(pix[x, y])
            if chr(c) not in data:
                data.append(chr(c))

    #data.sort()               
    print(data)
    #text_file = open("man.txt", "w")
    #text_file.write(data)
   

def luminance(c):
    red   = c[0]
    green = c[1]
    blue  = c[2]
    return (.299 * red) + (.587 * green) + (.114 * blue)

def toGray(c):
    y = int(round(luminance(c)))
    return y
    

jpg2ascii()


'''@@@@@@@
#############
£££££££££££££
============
++++++++++++
||||||||||||||||||||||||||||||
:::::::::::::::::::::::
.......................
                        
^space'''