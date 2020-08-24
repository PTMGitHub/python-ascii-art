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

## 3. Convert the RGB tuples of your pixels into single brightness numbers

So created a copy of the pixels list, called it brightness_matrix, then looped through and added the RGB tuples, devided by 3 then cast them to an int to get right of the decimal values.

### End Result
```python
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
 ```
 **Commited to GitHub**

 ### 4. Convert brightness numbers to ASCII characters
firstly i took of the int cast as we dont need it. lol 
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

### End Result
```python
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
            
    print(ascii_matrix)

except:
    print("Image loading didnt work")
```

 **Commited to GitHub**

## 5. Print your ASCII art!

So resonably easy with a for loop. 

just add this ...

```python
    for y in range(len(ascii_matrix)):
        print(*ascii_matrix[y],sep="")
```

Its works!

 **Commited to GitHub**

 ## Problem 1 - your image looks squashed
You’re displaying each pixel in your image using a character in your terminal. And whilst pixels are square, your terminal characters are rectangles, roughly three times as tall as they are wide. This will make your image appear squashed and narrow. The simplest way to fix this is to print each character in each row of your ASCII matrix three times, to stretch the image back out. For example, the list ['$', 'A', '#'] would be printed out as $$$AAA###.

So to fix this i just changed the for loop thats converting the brightness number to a char

I only doubled it because i looked better doubled not tripled lol 
```python
    #for loop to convert the number to one of our 70 charactors.
    for y in range(len(ascii_matrix)):
        for x in range(len(ascii_matrix[y])):
            ascii_matrix[y][x] = ascii_char[round(ascii_matrix[y][x] / 5)] + ascii_char[round(ascii_matrix[y][x] / 5)] 
```
## Problem 2 - your ASCII matrix is too large for your screen

need to add some image resizing. Added these lines
```python
    (width,height) = (img_in.width // 2, img_in.height //2)
    img = img_in.resize((width,height))
```
