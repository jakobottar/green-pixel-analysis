Written by [Jakob Johnson](mailto:jakob.johnson@usu.edu) for the [USU Crop Physiology Laboratory](https://cpl.usu.edu/).

This program analyzes images and counts the number of green pixels in the image. It reads image files from the chosen directory and outputs a csv containing summary information to the parent directory. 

The image files in `test-img` are given as sample images to demonstrate the code. 

## Usage
Requires Python 3.x.x
### Windows
Download the zip folder, install `numpy` and `Pillow` using the command line through
```
pip install numpy
pip install Pillow
```
Click on the `start.bat` file to launch the application.
Select a directory in the popup window and click 'Run Analysis'. 
The terminal window gives information about the running program.

### Mac/Linux
Download the zip folder, install `numpy` and `Pillow` through 
```
pip install numpy
pip install Pillow
```
Then run the program with 
``` python /path/to/file/main.py ```
Select a directory in the popup window and click 'Run Analysis'. 
The terminal window gives information about the running program.

### Without GUI
Follow the above steps to install the dependencies, then in your python program, import the `gpix.py` file and run the analysis with 
```
gpix.countPix('file/pathto/images', save = T/F).writeCsv('/dir/to/write/to/')
```
`countPix()` returns an object that contains summary imformation about the analyzed photos. Run the `.writeCsv()` method to export the stored data as a `.csv` file.

## Example

Reading the file `White 350 Nov 27.jpg`,
![image](https://user-images.githubusercontent.com/33588648/53047090-d2c91e00-344e-11e9-869f-530fbb6b4cf1.png)
returns the image `White 350 Nov 27-ANALYZED.jpg`,
![image](https://user-images.githubusercontent.com/33588648/53047115-e7a5b180-344e-11e9-8c4f-dd3ef7a60f0c.png)
and the summary statistics,

| Image Name | Total Green Pixels |	Percent of Total |
| --- | --- | --- |
| White 350 Nov 27 | 2285096 | 0.72085047 |

On a second pass, the program will ignore the `*-ANALYZED.jpg` file and overwrite the csv table.
