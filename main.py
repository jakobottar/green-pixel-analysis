# Python program to count green pixels in plant images
# by Jakob Johnson, jakob.johnson@usu.edu, github.com/JakobOttar

# https://github.com/jakobottar/green-pixel-analysis

# import custom module            
from lib import gpix
from appJar import gui

# TODO: Add GUI 

app = gui()

def run():
    filePath = app.getEntry('directory')
    if(filePath != ''):
        app.setLabel('status','Running...')
        app.setLabelBg('status', 'red')

        app.threadCallback(runAnalysis, finished, filePath)

def finished(success):   
    app.queueFunction(app.setLabel, 'status', 'Done!')
    app.queueFunction(app.setLabelBg, 'status', 'green')

def runAnalysis(filePath):
    gpix.countPix(filePath).writeCsv()
    print('Done!')
    pass

app.addLabel('status','Please Choose a Directory')
app.addDirectoryEntry('directory')
app.addButton('Run Analysis', run)

app.go()