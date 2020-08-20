from PIL import Image
try:
    img = Image.open("./ascii-pineapple.jpg",mode='r')

    print('Succesfully loaded image!')
    print("Image size: " + str(img.width) + " x " + str(img.height))
except:
    print("Image loading didnt work")