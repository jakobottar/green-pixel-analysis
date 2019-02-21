# Python program to count green pixels in plant images
# by Jakob Johnson, jakob.johnson@usu.edu, github.com/JakobOttar

# https://github.com/jakobottar/green-pixel-analysis

# import custom module            
from lib import gpix 

# TODO: Add GUI 

# points to folder containing images
# filePath = './img/'
filePath = input("Please choose a directory: ")          
if(filePath == ''):
    filePath = './img/'

gpix.countPix(filePath).writeCsv()

print('Done!')