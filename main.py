from PIL import Image
try:
    #Reads in the image and prints a message saying so and a messages printing the image size
    #img = Image.open("./ascii-pineapple_big.jpg",mode='r')
    #img = Image.open("./ascii-pineapple.jpg",mode='r')
    #img = Image.open("./lion2.jpg",mode='r')
    #img = Image.open("./me_200x267.jpg",mode='r')
    img = Image.open("./me.jpg",mode='r')
    print('Succesfully loaded image!')
    print("Image size: " + str(img.width) + " x " + str(img.height))
    #import pdb; pdb.set_trace()
    #gets the pixel info and cast it to a list. this is flat
    pixels = list(img.getdata())
    #makes the list into a 2d list.
    pixels = [    pixels[i:i+img.width] for i in range(0, len(pixels),          img.width)]



    #img.show()
  
    #creates a copy of the pixels matrix
    brightness_matrix = pixels
    
    #loops through the brightnexx matrix and replaces the RGB tuple values with the (R+G+B)/3
    for y in range(len(brightness_matrix)):
        for x in range(len(brightness_matrix[y])):
            brightness_matrix[y][x] = (brightness_matrix[y][x][0] + brightness_matrix[y][x][1] + brightness_matrix[y][x][2]) / 3
        
    #print(brightness_matrix)


    # with a brightness scale of 0-100 using 20 characters
    # brightness 20 = char 4
    # brightness 30 = char 6
    # brightness 50 = char 10
    # brightness 60 = char 12
    # brightness 75 = char 15

    # All are devided by 5 whic is the GCF Greatest Common Factor
    # Formula:
    # char = brightness / 5

    # If the brightness is a float, round it up or down using round()

    #List of 70 char's we are gonna use to make our picture.
    ascii_char = "`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"
    
    #creates a copy of the brightness matrix
    ascii_matrix = brightness_matrix
    
    #for loop to convert the number to one of our 70 charactors.
    for y in range(len(ascii_matrix)):
        for x in range(len(ascii_matrix[y])):
            ascii_matrix[y][x] = ascii_char[round(ascii_matrix[y][x] / 5)]
            
   
    for y in range(len(ascii_matrix)):
        print(*ascii_matrix[y],sep="")





except:
    print("Image loading didnt work")