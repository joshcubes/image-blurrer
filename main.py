from skimage.io import imread, imsave

inimage = imread(input("Please enter the filename of the Bitmap Image: "))
iterations = int(input("How many iterations?: "))
output_name = input("What would you like the output file to be named?: ")
output_name += ".bmp"
i = 0
currentpercent = 0


def find_divisable_amount(x,y, ix, iy):
    divisable_amount = 9
    table = [[True, True, True],
             [True, True, True],
             [True, True, True]]
    
    # TL
    if (x - 1 < 0) or (y - 1 < 0):
        table[0][0] = False
        divisable_amount -= 1
    
    # TM
    if (y - 1 < 0):
        table[0][1] = False
        divisable_amount -= 1
    
    # TR
    if (x + 1 >= ix) or (y - 1 < 0):
        table[0][2] = False
        divisable_amount -= 1
    
    # ML
    if (x - 1 < 0):
        table[1][0] = False
        divisable_amount -= 1

    # MR
    if (x + 1 >= ix):
        table[1][2] = False
        divisable_amount -= 1
    
    # BL
    if (x - 1 < 0) or (y + 1 >= iy):
        table[2][0] = False
        divisable_amount -= 1
    
    # BM
    if (y + 1 >= iy):
        table[2][1] = False
        divisable_amount -= 1
    
    # BR
    if (x + 1 >= ix) or (y + 1 >= iy):
        table[2][2] = False
        divisable_amount -= 1
    
    
    return table, divisable_amount

def blur_pixel(x,y, IMG_X, IMG_Y, IMAGE):
    pixels_to_blur, devide = find_divisable_amount(x,y, IMG_X, IMG_Y)
    red = 0
    green = 0
    blue = 0
    
    red += IMAGE[y][x][0]
    green += IMAGE[y][x][1]
    blue += IMAGE[y][x][2]
    
    # TL
    if pixels_to_blur[0][0] == True:
        red += IMAGE[y-1][x-1][0]
        green += IMAGE[y-1][x-1][1]
        blue += IMAGE[y-1][x-1][2]

    # TM
    if pixels_to_blur[0][1] == True:
        red += IMAGE[y-1][x][0]
        green += IMAGE[y-1][x][1]
        blue += IMAGE[y-1][x][2]

    # TR
    if pixels_to_blur[0][2] == True:
        red += IMAGE[y-1][x+1][0]
        green += IMAGE[y-1][x+1][1]
        blue += IMAGE[y-1][x+1][2]

    # ML
    if pixels_to_blur[1][0] == True:
        red += IMAGE[y][x-1][0]
        green += IMAGE[y][x-1][1]
        blue += IMAGE[y][x-1][2]
        
    # MR
    if pixels_to_blur[1][2] == True:
        red += IMAGE[y][x+1][0]
        green += IMAGE[y][x+1][1]
        blue += IMAGE[y][x+1][2]

    # BL
    if pixels_to_blur[2][0] == True:
        red += IMAGE[y+1][x-1][0]
        green += IMAGE[y+1][x-1][1]
        blue += IMAGE[y+1][x-1][2]

    # BM
    if pixels_to_blur[2][1] == True:
        red += IMAGE[y-1][x][0]
        green += IMAGE[y-1][x][1]
        blue += IMAGE[y-1][x][2]

    # BR
    if pixels_to_blur[2][2] == True:
        red += IMAGE[y+1][x+1][0]
        green += IMAGE[y+1][x+1][1]
        blue += IMAGE[y+1][x+1][2]
    
    red = red / devide
    green = green / devide
    blue = blue / devide
    
    red = round(red, 0)
    green = round(green,0)
    blue = round(blue,0)
    
    if red > 255:
        red = 255
    if green > 255:
        green = 255
    if blue > 255:
        blue = 255
    
    output = [red,green,blue]
    return output

def blur_image(image, it, its):
    newimage = image
    IMAGE_X = len(image[0])
    IMAGE_Y = len(image)
    PX_DONE = 0
    percent = 0
    TOTAL_PX = IMAGE_X * IMAGE_Y
    CURRENT_X = 0
    CURRENT_Y = 0
    while (CURRENT_Y in range(0, IMAGE_Y)):
        while (CURRENT_X in range(0 ,IMAGE_X)):
        
            newimage[CURRENT_Y][CURRENT_X] = blur_pixel(CURRENT_X, CURRENT_Y, IMAGE_X, IMAGE_Y, image)

            CURRENT_X += 1
            PX_DONE += 1
            newpercent = int(round(((PX_DONE / TOTAL_PX) * 100), 0))
            if  (newpercent > (percent + 1)):
                print("Iteration:", it, "out of", its, "(" + str(newpercent) + "%)")
                percent = newpercent
            
        CURRENT_X = 0
        CURRENT_Y += 1
    return newimage


while i in range(0,iterations):
    i += 1
    inimage = blur_image(inimage, i, iterations)

imsave(output_name, inimage)

