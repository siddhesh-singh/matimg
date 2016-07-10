# matimg

## Convert matrices to images and vice versa using this python script
Give the script the path to a text file containing a matrix as input and specify an output image name and location. In the text file each line must represents a row and each space separated number must represent an element. Numbers must be binary (0 or 1) with 0 representing a white pixel and 1 representing a black pixel.The matrix entries will be converted to pixels with ones being converted to black and zeroes being converted to white and saved as a PNG image.

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

You may import the script as a module to use its functions.
```matrix_to_image(matrix_path, image_path)``` takes the matrix at matrix_path and outputs the converted image to image_path.
```image_to_matrix(matrix_path, image_path)``` uses the image at image_path and outputs a matrix representation of the image at matrix_path.
```image_to_list(image_path)``` this method takes data from the image at image_path and returns a matrix represented by nested lists where each inner list represents a row.

##Examples
The script accepts a matrix where each line represents a row and each number belongs to a column respective to its position on the line. The matrix must be saved as plain text file with spaces seperating the entries in eaach line. The only acceptable entries are 1 and 0.

```
1 0 0 0 0 1
0 1 0 0 1 0
0 0 1 1 0 0
0 0 1 1 0 0
0 1 0 0 1 0
1 0 0 0 0 1
```

The above matrix from the [examples](/examples) folder can be used with the script as following:
``` 
matimg.py -m input_matrix.txt -i output_image.png 
```
to produce the output image:
<br>
<img src="examples/output_image.png" width="32" height="32">
<br>

You can also create the matrix from the image using the --imgmat option (assuming the image file already exists):
``` 
matimg.py -m input_matrix.txt -i output_image.png --imgmat
```


## Requirements

This script requires Python 3 and [Pillow](https://github.com/python-pillow/Pillow) to work
