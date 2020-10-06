# Project---Face-Recognization
The Imgcodecs class of the package org.opencv.imgcodecs provides methods to read and write images. Using OpenCV, you can read an image and store it in a matrix (perform transformations on the matrix if needed). Later, you can write the processed matrix to a file.

The read() method of the Imgcodecs class is used to read an image using OpenCV. Following is the syntax of this method.

imread(filename)

The write() method of the Imgcodecs class is used to write an image using OpenCV. To write an image, repeat the first three steps from the previous example.

To write an image, you need to invoke the imwrite() method of the Imgcodecs class.

Following is the syntax of this method.

imwrite(filename, mat)

Converting Colored Images to Grayscale
A method named cvtColor() is used to convert colored images to grayscale. Following is the syntax of this method.

cvtColor(Mat src, Mat dst, int code)
This method accepts the following parameters −

src − A matrix representing the source.

dst − A matrix representing the destination.

code − An integer code representing the type of the conversion, for example, RGB to Grayscale.

You can convert colored images to gray scale by passing the code Imgproc.COLOR_RGB2GRAY along with the source and destination matrices as a parameter to the cvtColor() method.
