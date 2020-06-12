try:
    from PIL import Image # https://pillow.readthedocs.io/en/stable/
except ImportError:
    print("ERROR: You don't have the Pillow package installed. Install it with 'pip install Pillow'")

try:
    import numpy as np
except ImportError:
    print("You don't have the numpy package installed. Install it with 'pip install numpy'")

import time
import os
import re
import csv

# Object to store image summary data and write to CSV
class ImageSummary:
    # store summary data
    def __init__( self ): 
        self.sumData = []

    # write sumData to CSV
    # location sets the save location for the csv.
    # By default it uses the parent directory
    def writeCsv( self, location = "." ): 
        os.chdir(location)

        print('Writing CSV...')

        # create csv and write header row
        c = csv.writer(open('image-summary.csv', 'w'), lineterminator='\n')
        c.writerow(['Image Name', 'Total Green Pixels', 'Percent of Total']) 

        # write a row for each image analyzed
        for i in self.sumData:
            c.writerow([i['imgName'], i['greenTot'], i['percOfWhole']])
    
    # overload append() to add data to stored array
    def append( self, data ):
        self.sumData.append(data)

def countPix( folderLoc, save, fuzzFactor ):
    # change directory to chosen folder 
    os.chdir(folderLoc)
    print("Looking in folder: " + folderLoc)

    print("Fuzz = " + str(fuzzFactor))

    # get files from the chosen folder
    files = os.listdir()

    # blank ImageSummary object, to hold image data
    imgSum = ImageSummary()

    for i in range(len(files)):
        print('Analyzing file ' + str(i+1) + ' of ' + str(len(files)) + '... ', end = '')
        if(not _isValidImageFile_(files[i])): # skip invalid files and files that end in '-ANALYZED'
            print('Invalid File, Skipped')
        else:
            print('')
            imgSum.append(_analyzeImage_(files[i], save, fuzzFactor)) # analyze each file, store in object
    
    return(imgSum) 

def _analyzeImage_( fileName , save, greenFuzz ):
    start = time.time() # start timer

    # open image, resize, convert to RGB
    # we resize every image to the same size to remove zoom/crop effects on image size
    im = Image.open(fileName).resize((2000, 1500)).convert('RGB') # total pixels = 3,000,000
    # get bands, convert to numpy arrays for faster analysis
    rBand = np.array(im.getdata(band=0)) + greenFuzz
    gBand = np.array(im.getdata(band=1))
    bBand = np.array(im.getdata(band=2)) + greenFuzz

    green = 0                                               # initialize green pixel counter
    for i in range(im.width*im.height):                     # get pixel at (x,y) location
        p = [ rBand[i], gBand[i], bBand[i] ]
        if(_isGreen_(p)):                                   # if the pixel is green,
            green += 1                                      # count it as a green pixel
            if(save): 
                x = i % im.width
                y = int(i / im.width)
                im.putpixel((x,y), (255, 0, 0))   # replace the pixel with a red one, indicating it was detected as green

    imgName = os.path.splitext(fileName)[0]
    # save image with detected pixels next to original image
    if(save): im.save(imgName + "-ANALYZED.jpg") 

    end = time.time() # end timer
    print("Completed in " + str(end-start) + " sec.") # print time elapsed

    # return info about the image as a json object
    return({                                    
        'imgName': imgName,
        'greenTot': green,
        'percOfWhole': green / (im.width * im.height)
    })

# check if image is a valid image filetype and
# if the image has not already been analyzed (No -ANALYZED.jpg images)
# Note: This will still break if a non-image file is passed in with the .jpg
# or .png extension. Need to fix later. 
def _isValidImageFile_( fileName ):
    if(re.match(r'.*-ANALYZED\.jpg', fileName) != None):
        return(False)

    extension = os.path.splitext(fileName)[1].lower()
    checkAgainst = ['.jpg', '.png']
    if(extension in checkAgainst):
        return True

    return(False)

# check if the pixel is green
# very basic right now, broken out for future work
def _isGreen_ (pixel):
    return(pixel[1] > pixel[0] and pixel[1] > pixel[2])
