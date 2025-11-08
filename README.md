# imageToASCII



* Python
* Week 1 of 52







### Documentation



* 2 python scripts to choose from, imageToAscii.py and imageToAsciiGS.py
* &nbsp;	Both convert the image to ascii in black and white. 
* &nbsp;	GS uses a built in CV2 function to turn the image grey, seems to be more detailed that taking the average channel value.
* Arguments taken:
* &nbsp;	0 - Loads first image from image folder at 0.25 scale 		eg. python imageToAscii.py 
* &nbsp;	1 - Loads image specified (jpg or png only) at 0.25 scale	eg. python imageToAsciiGS.py monaLisa.jpg
* &nbsp;	2 - Loads image specified at specified scale			eg. python imageToAscii.py monaLisa.jpg 0.1
* Store images in the /images folder, and input them with just their name as shown in the example.
* Some images have been provided for you to test out the script.






### Tutorials used



* Image processing: https://www.youtube.com/watch?v=kSqxn6zGE0c
* NumPy multidimensional arrays tutorial: https://www.youtube.com/watch?v=EnhgbolbEe0



\### Learnt

* 3d Arrays
* Reading and manipulating image data



\### Reinforced

* Writing to files
* Virtual environments



\### Roadblocks faced

* Had to use virtual environments because cv2 is not yet compatible with python 3.14 as of 08/11/25
