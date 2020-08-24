from PIL import Image
try:
    #Reads in the image and prints a message saying so and a messages printing the image size
    img = Image.open("./ascii-pineapple.jpg",mode='r')
    #img = Image.open("./lion2.jpg",mode='r')
    print('Succesfully loaded image!')
    print("Image size: " + str(img.width) + " x " + str(img.height))
    #import pdb; pdb.set_trace()
    #gets the pixel info and cast it to a list. this is flat
    pixels = list(img.getdata())
    #makes the list into a 2d list.
    pixels = [    pixels[i:i+img.width] for i in range(0, len(pixels),          img.width)]



    #img.show()
  
    
    brightness_matrix = pixels
      
    for y in range(len(brightness_matrix)):
        for x in range(len(brightness_matrix[y])):
            brightness_matrix[y][x] = int((brightness_matrix[y][x][0] + brightness_matrix[y][x][1] + brightness_matrix[y][x][2]) / 3)
        
    print(brightness_matrix)

except:
    print("Image loading didnt work")