# Python program to count green pixels in plant images
# by Jakob Johnson, jakob.johnson@usu.edu, github.com/JakobOttar

# https://github.com/jakobottar/green-pixel-analysis

# import custom module            
from lib import gpix
from appJar import gui # appJar GUI library: http://appjar.info/

# initialize GUI
app = gui() 

# runs when 'Start' button is pushed
def run():
    filePath = app.getEntry('directory') # get chosen directory
    if(filePath != ''):
        app.setLabel('status','Running...') # indicate the program is running
        app.setLabelBg('status', 'red') 

        app.threadCallback(runAnalysis, finished, filePath)

def finished(success):   # show the program has finished
    app.queueFunction(app.setLabel, 'status', 'Done!') 
    app.queueFunction(app.setLabelBg, 'status', 'green')

def runAnalysis(filePath):
    gpix.countPix(filePath, True).writeCsv() # run the analysis and save the summary CSV
    print('Done!')
    pass

app.addLabel('status','Please Choose a Directory')
app.addDirectoryEntry('directory')
app.addButton('Run Analysis', run)

app.go() # launch GUI