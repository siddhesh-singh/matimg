# matimg

## Convert matrices to images and vice versa using this python script
Give the script the path to a text file containing a matrix as input and specify an output image name and location. The matrix entries will be converted to pixels with ones being converted to black and zeroes being converted to white.

## Usage
Use the script through the terminal with the following command:
```
matimg.py -m <matrix file/name> -i <image file/name> [--imgmat]
```
or if that does not work use one of these:
```
python matimg.py -m <matrix file/name> -i <image file/name> [--imgmat]
```
```
python3 matimg.py -m <matrix file/name> -i <image file/name> [--imgmat]
```
The default behaviour of the script is to read the matrix text file and output a PNG file with the specified name and location. Using the --imgmat reverses this behaviour by taking an image file as input and producing a text file with a matrix as output. The image file can be coloured but will be converted to black and white.

Type ```matimg.py -h``` to display these instructions.

## Requirements

This script requires Python 3 and [Pillow](https://github.com/python-pillow/Pillow) to work
