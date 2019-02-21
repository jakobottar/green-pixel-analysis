from PIL import Image   # pip install Pillow, https://pillow.readthedocs.io/en/stable/
import numpy as np      # pip install numpy
import time
import os
import re
import csv

class ImageSummary:
    def __init__( self ):
        self.sumData = []

    def makeCsv( self, loc = ".." ):
        os.chdir(loc)

        print('Writing CSV...')

        # create csv and write header row
        c = csv.writer(open('image-summary.csv', 'w'), lineterminator='\n')
        c.writerow(['Image Name', 'Total Green Pixels', 'Percent of Total']) 

        # write a row for each image analyzed
        for i in self.sumData:
            c.writerow([i['imgName'], i['greenTot'], i['percOfWhole']])
    
    def append( self, data ):
        self.sumData.append(data)

def countPixAt( folderLoc ):
    # change directory to chosen folder 
    os.chdir(folderLoc)

    # get files from the chosen folder
    files = os.listdir()

    # blank ImageSummary object, to hold image data
    imgSum = ImageSummary()

    for i in range(len(files)):
        print('Analyzing file ' + str(i+1) + ' of ' + str(len(files)) + '... ', end = '')
        if(re.match(r'.*-ANALYZED\.jpg', files[i]) != None): # skip files that end in '-ANALYZED'
            print('Skipped.')
        if(re.match(r'.*\.csv', files[i]) != None):
            print('CSV file, skipped.')
        else:
            print('')
            imgSum.append(analyzeImage(files[i])) # analyze each file, store in object
    
    return(imgSum)

def analyzeImage( fileName , save = False ):
    start = time.time() # start timer

    # open image, resize, convert to RGB
    # we resize every image to the same size to remove zoom/crop effects on image size
    im = Image.open(fileName).resize((2000, 1500)).convert('RGB') # total pixels = 3,000,000
    # convert to numpy array for faster analysis
    arr = np.array(im)

    green = 0                                               # initialize green pixel counter
    for x in range(im.width):                               # loop over all pixels in image
        for y in range(im.height):
            p = arr[y][x]                                   # get pixel at (x,y) location
            if( p[1] > p[0] and p[1] > p[2]) :              # if the pixel is majority green,
                green += 1                                  # count it as a green pixel
                if(save): im.putpixel((x,y), (255, 0, 0))   # replace the pixel with a red one, indicating it was detected as green

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