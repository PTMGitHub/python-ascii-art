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
    print(img.format, img.size, img.mode)

except:
    print("Image loading didnt work")
```

**Commited to GitHUB**