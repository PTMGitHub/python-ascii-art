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
This was the code to get the pixel info into a 2d array
```python
    pixels = list(img.getdata())
    pixels = [pixels[i:i+img.width] for i in range(0, len(pixels), img.width)]
```
I had to look at his completed source code.  I need to unpack this so i know exactly whats going on - job for next week

**Commited to GitHub**

So what i believe is happening:
```python
img.getdata()  
```

This brings back the pixel info we want but it returned as an object

```python
pixel = list(img.getdata())  
```
You can cast it to a list but this is a flat list so need to convert it to a 2d list 
```python
pixels = [    pixels[i:i+img.width] for i in range(0, len(pixels),          img.width)]
'''
This makes it into a 2d list, each pix line is always gonnabe the same lenght (img.width). so this then loops throught and 'cuts' the long list of pixs everytime it his the width value.

### End Result
```python
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
```

**Commited to GitHub**