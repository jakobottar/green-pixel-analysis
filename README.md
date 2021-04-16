Written by [Jakob Johnson](https://jakobj.dev) for the [USU Crop Physiology Laboratory](https://cpl.usu.edu/).

This program analyzes images and counts the number of green pixels in the image. It reads image files from the chosen directory and outputs a csv containing summary information to the parent directory. 

The image files in `test-img` are given as sample images to demonstrate the code. 

Used in ["Substituting Far-Red for Traditionally Defined Photosynthetic Photons Results in Equal Canopy Quantum Yield for CO2 Fixation and Increased Photon Capture During Long-Term Studies: Implications for Re-Defining PAR"](https://www.frontiersin.org/articles/10.3389/fpls.2020.581156/full) by Shuyang Zhen and Bruce Bugbee

## Usage
Requires Python 3.x.x

### GUI in Windows/macOS
Install dependancies `numpy` and `Pillow` using PowerShell/Terminal with the commands
```
pip install numpy
pip install Pillow
```
To run the program, either open `main.py` with Python or in PowerShell/Terminal using 
```
python `.\path\to\directory\main.py`
```
*Note, for macOS you'll need to use `python3` instead of `python`*

Select a directory in the popup window and click 'Run Analysis'. 
The terminal window gives information about the running program.

The 'Create Analyzed Images' checkbox lets you save an image showing where the program detected green pixels. This option slows down analysis.

The 'Fuzz Factor' slider determines the algorithm's green sensitivity. Increase it if necessary to eliminate background noise. 


### Without GUI
Follow the above steps to install the dependencies, then in your python program, import the `gpix.py` file and run the analysis with 
```
gpix.countPix('file/path/to/images', save = T/F, fuzzFactor).writeCsv('/dir/to/write/to/')
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
