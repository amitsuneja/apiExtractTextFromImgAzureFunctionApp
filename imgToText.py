#!/usr/bin/python3
import argparse
import pytesseract
from PIL import Image

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
# Ensuring user must pass argument to the script. -f path_to_img_file
ap.add_argument("-f", "--file", required=True, help="path to image file, containing text")
# Creating dictionary of arguments passed the script.
cli_argument_dict = vars(ap.parse_args())
# Fetching file value which is path to image file.
path_to_image_file = cli_argument_dict["file"]

text = ''
if path_to_image_file:
    text = str(pytesseract.image_to_string(Image.open(path_to_image_file)))
    print(text)
