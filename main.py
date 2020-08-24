from PIL import Image
try:
    #Reads in the image and prints a message saying so and a messages printing the image size
    img = Image.open("./lion2.png",mode='r')
    print('Succesfully loaded image!')
    print("Image size: " + str(img.width) + " x " + str(img.height))

    #gets the pixel info and cast it to a list. this is flat
    pixels = list(img.getdata())
    #makes the list into a 2d list.
    pixels = [    pixels[i:i+img.width] for i in range(0, len(pixels),          img.width)]


    #img.show()
    
except:
    print("Image loading didnt work")