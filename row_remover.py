#!/usr/bin/env python
import argparse

import numpy as np
from PIL import Image
from pathlib import Path

# Get info from arguments
parser = argparse.ArgumentParser(description='Remove the Nth line from an image')
parser.add_argument(
    "-v", "--verbose", action="store_true",
    help="output additional information"
)
parser.add_argument(
    "N",
    help="Every Nth row/column should be deleted from the iamge"
)
parser.add_argument(
    "input_file",
    help="input file to be changed",
)
parser.add_argument(
    "output_file",
    help="output to store edited file",
)
args = parser.parse_args()

# Convert arguments to local vars
N = int(args.N)
file_path = Path(args.input_file)
if (args.verbose):
    print(f"Deleteing every {N}th row/col from {file_path}")

# Open the image and converting it to RGB color mode
img = Image.open(file_path).convert('RGB')

# Extracting the image data & creating an numpy array out of it
img_arr = np.array(img)

# delete the nth row from the array,
# handling the fact that the image changes size
line = N
while True:
    (img_width, img_height, img_channel) = img_arr.shape
    if (args.verbose):
        print(f"WIDTH={img_width} height={img_height} curr={line}")
    img_arr = np.delete(img_arr, line, 0)
    line += N
    if (line >= img_width - 1):
        break

# Eh, its easier just to do this once for each dimension
# rather than function-ize it.
line = N
while True:
    (img_width, img_height, img_channel) = img_arr.shape
    if (args.verbose):
        print(f"width={img_width} HEIGHT={img_height} curr={line}")
    img_arr = np.delete(img_arr, line, 1)
    line += N
    if (line >= img_height - 1):
        break

# Creating an image out of the previously modified array
img = Image.fromarray(img_arr)

# write the image to file
img.save(args.output_file)