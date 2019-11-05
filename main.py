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
    gpix.countPix(filePath, 
        app.getCheckBox('Create Analyzed Images'),
        app.getScale('Fuzz Factor')).writeCsv() # run the analysis and save the summary CSV
    print('Done!')
    pass

app.addLabel('status','Please Choose a Directory')
app.addDirectoryEntry('directory')

app.addButton('Run Analysis', run)
app.addCheckBox('Create Analyzed Images')

app.addLabelScale('Fuzz Factor')
app.setScaleRange('Fuzz Factor', start=0, end=50)
app.setScale('Fuzz Factor', 10)
app.showScaleValue('Fuzz Factor', show=True)

app.setTitle('Green Pixel Analyzer')
app.setSize(350,200)
app.go() # launch GUI