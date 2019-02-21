This program analyzes images and counts the number of green pixels in the image. It reads images from the `BASEPATH` directory (default `./img/`) and reports a csv, `image-summary.csv`, containing the image name, total number of green pixels, and % green pixels in image.

[USU Crop Physiology Laboratory](https://cpl.usu.edu/)

**Example:**
Reading the file `White 350 Nov 27.jpg`,
![image](https://user-images.githubusercontent.com/33588648/53047090-d2c91e00-344e-11e9-869f-530fbb6b4cf1.png)
returns the image `White 350 Nov 27-ANALYZED.jpg`,
![image](https://user-images.githubusercontent.com/33588648/53047115-e7a5b180-344e-11e9-8c4f-dd3ef7a60f0c.png)
and the summary statistics,

| Image Name | Total Green Pixels |	Percent of Total |
| --- | --- | --- |
| White 350 Nov 27 | 2285096 | 0.72085047 |

as a csv.

On a second pass, the program will ignore the `*-ANALYZED.jpg` file and overwrite the csv table.

[Example Files and Output](https://drive.google.com/open?id=1cYB505YTrFoR8ZTLPaR0JJWVGelrWt0f)