from PIL import Image   # pip install Pillow, https://pillow.readthedocs.io/en/stable/
import numpy as np      # pip install numpy
import time
import os

# controls wether or not the image is saved with detected pixels (slower, creates file for each image)
SAVE = False

def analyzeImage( fileName, BASEPATH):
    start = time.time() # start timer

    # open image, resize, convert to RGB
    # we resize every image to the same size to remove zoom/crop effects on image size
    im = Image.open(BASEPATH + fileName).resize((2000, 1500)).convert('RGB') # total pixels = 3,000,000
    # convert to numpy array for faster analysis
    arr = np.array(im)

    green = 0                                               # initialize green pixel counter
    for x in range(im.width):                               # loop over all pixels in image
        for y in range(im.height):
            p = arr[y][x]                                   # get pixel at (x,y) location
            if( p[1] > p[0] and p[1] > p[2]) :              # if the pixel is majority green,
                green += 1                                  # count it as a green pixel
                if(SAVE): im.putpixel((x,y), (255, 0, 0))   # replace the pixel with a red one, indicating it was detected as green

    imgName = os.path.splitext(fileName)[0]
    # save image with detected pixels next to original image
    if(SAVE): im.save(BASEPATH + imgName + "-ANALYZED.jpg") 

    end = time.time() # end timer
    print("File " + fileName + " analyzed in " + str(end-start) + " sec.") # print time elapsed

    # return info about the image as a json object
    return({                                    
        'imgName': imgName,
        'greenTot': green,
        'percOfWhole': green / (im.width * im.height)
    })