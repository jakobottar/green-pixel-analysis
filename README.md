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
If `pip` is not installed, install it here: https://pip.pypa.io/en/stable/installing/#installing-with-get-pip-py.

Then run the program with 
``` 
python /path/to/file/main.py 
```
Select a directory in the popup window and click 'Run Analysis'. 
The terminal window gives information about the running program.

### Mac/Linux
Download the zip folder, install `numpy` and `Pillow` through 
```
pip install numpy
pip install Pillow
```
If `pip` is not installed, install it here: https://pip.pypa.io/en/stable/installing/#installing-with-get-pip-py.

Then run the program with 
``` 
python3 /path/to/file/main.py 
```
Select a directory in the popup window and click 'Run Analysis'. 
The terminal window gives information about the running program.

### Without GUI
Follow the above steps to install the dependencies, then in your python program, import the `gpix.py` file and run the analysis with 
```
gpix.countPix('file/pathto/images', save = T/F).writeCsv('/dir/to/write/to/')
```
`countPix()` returns an object that contains summary information about the analyzed photos. Run its `.writeCsv()` method to export the stored data as a `.csv` file.

## Example

Reading the file `RB 300 FR 50 June 6 630pm.jpg`,
![image](https://raw.githubusercontent.com/jakobottar/green-pixel-analysis/master/test-img/RB%20300%20FR%2050%20June%206%20630pm.jpg)
returns the image `RB 300 FR 50 June 6 630pm-ANALYZED.jpg`,
![image](https://raw.githubusercontent.com/jakobottar/green-pixel-analysis/master/test-img/RB%20300%20FR%2050%20June%206%20630pm-ANALYZED.jpg)
and the summary statistics,

| Image Name | Total Green Pixels |	Percent of Total |
| --- | --- | --- |
| RB 300 FR 50 June 6 630pm | 940635 | 0.313545 |

On a second pass, the program will ignore the `*-ANALYZED.jpg` file and overwrite the csv table.
