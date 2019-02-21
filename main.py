# Python program to count green pixels in plant images
# by Jakob Johnson, jakob.johnson@usu.edu, github.com/JakobOttar

# https://gist.github.com/jakobottar/955e7b1ec0fa105c0ac2c3bef60e91a6

import csv              
import os               
import gpix

# base path, points to folder containing images
filePath = 'C:/Users/Jakob/Desktop/img/'              

imgSum = gpix.countPixAt(filePath)
gpix.makeCsv(imgSum)

print('Done!')