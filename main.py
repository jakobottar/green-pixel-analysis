# Python program to count green pixels in plant images
# by Jakob Johnson, jakob.johnson@usu.edu, github.com/JakobOttar

# https://github.com/jakobottar/green-pixel-analysis

# import custom module            
from lib import gpix 

# points to folder containing images
filePath = './img/'              

gpix.countPix(filePath).writeCsv()

print('Done!')