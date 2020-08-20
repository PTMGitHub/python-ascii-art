# ASCII Art Python Project

## Source 
https://robertheaton.com/2018/06/12/programming-projects-for-advanced-beginners-ascii-art/

## Aim
a program to turn images into ASCII-art


# Steps to complete it
## 1. Read your image and print its height and width in pixels

1. Install Pillow Python Imaging Library
https://python-pillow.org/
2. Load an print out the image details 
I worked out the code needed by using the https://python-pillow.org/ tutorials

### End result
```python
from PIL import Image
try:
    img = Image.open("./ascii-pineapple.jpg",mode='r')

    print('Succesfully loaded image!')
    print(Image img.format, img.size, img.mode)

except:
    print("Image loading didnt work")
```

**Commited to GitHUB**

3. its not quite right should be printed out like this: "Image size: 640 x 480" mine is "JPEG (700, 467) RGB"

### End Result
```python
from PIL import Image
try:
    img = Image.open("./ascii-pineapple.jpg",mode='r')

    print('Succesfully loaded image!')
    print("Image size: " + str(img.width) + " x " + str(img.height))
except:
    print("Image loading didnt work")
```
**Commited to GitHUB**

## 2. Load your image’s pixel data into a 2-dimensional array
