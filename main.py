from PIL import Image
try:
    #Reads in the image and prints a message saying so and a messages printing the image size
    img = Image.open("./ascii-pineapple.jpg",mode='r')
    print('Succesfully loaded image!')
    print("Image size: " + str(img.width) + " x " + str(img.height))

    pixels = list(img.getdata())
  #  pixels = [pixels[i * width:(i + 1) * width] for i in xrange(height)]
    pixels = [pixels[i:i+img.width] for i in range(0, len(pixels), img.width)]

    print(pixels[0][0])
    print(len(pixels))
    # print('\n')
    # print(img_px_matrix[0])
    # print(img_px_matrix[0][0])
    # print(len(img_px_matrix))
    # print(len(img_px_matrix[0]))
    # print('\n')

    #img.show()
    
    # pix_2d_list = []
    # print("Here's the image pixel info:")
    # import pdb; pdb.set_trace()
    # for x in img_px_matrix:
    #     pix_2d_list.append(img_px_matrix[x])

    # print(pix_2d_list)

    # for x in img_px_matrix:
    # #    print('hi')
    #     import pdb; pdb.set_trace()
    #     for y in len(img_px_matrix[x]):
    #         print('hello')
    # #         pixel = img_px_matrix[x][y]
    # #         print(pixel)

    # print(img_px_matrix)
  
except:
    print("Image loading didnt work")