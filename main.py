from PIL import Image
try:
    #Reads in the image and prints a message saying so and a messages printing the image size
    img = Image.open("./ascii-pineapple.jpg",mode='r')
    print('Succesfully loaded image!')
    print("Image size: " + str(img.width) + " x " + str(img.height))

    #image_px_matrix = img.load()

    img.show()
    
    #print(image_px_matrix[4,4])
    # print("Here's the image pixel info:")
    # for i in len(image_px_matrix):
    #     for y in len(image_px_matrix[x]):
    #         pixel = image_px_matrix[x][y]

    # print(*pixel, sep="\n")


except:
    print("Image loading didnt work")