from PIL import Image
try:
    img = Image.open("./ascii-pineapple.jpg",mode='r')

    print('Succesfully loaded image!')
    print(img.format, img.size, img.mode)

except:
    print("Image loading didnt work")