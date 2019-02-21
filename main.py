# Python program to count green pixels in plant images
# by Jakob Johnson, jakob.johnson@usu.edu, github.com/JakobOttar

# https://gist.github.com/jakobottar/955e7b1ec0fa105c0ac2c3bef60e91a6

import csv              
import os               
import re
import gpix

# base path, points to folder containing images
BASEPATH = './img/'              

# get list of files at BASEPATH location
files = os.listdir(BASEPATH)                   

#blank array, to hold image data
imgSum = [] 

for i in range(len(files)):
    print('Analyzing image ' + str(i+1) + ' of ' + str(len(files)) + '... ', end = '')
    if(re.match(r'.*-ANALYZED\.jpg', files[i]) != None): # skip files that end in '-ANALYZED'
        print('Skipped.')
    else:
        print('')
        imgSum.append(gpix.analyzeImage(files[i], BASEPATH)) # analyze each file, store in array

print('Creating summary csv...')

# create csv and write header row
c = csv.writer(open('image-summary.csv', 'w'), lineterminator='\n')
c.writerow(['Image Name', 'Total Green Pixels', 'Percent of Total']) 

# write a row for each image analyzed
for i in imgSum:
    c.writerow([i['imgName'], i['greenTot'], i['percOfWhole']])

print('Done!')