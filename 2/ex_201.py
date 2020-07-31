import argparse
import cv2
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from pathlib import Path
from os import path
import numpy as np

# Construct the argument parser and parse the arguments.
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=False, help="Path to the image")
args = vars(ap.parse_args())

rootFolder = Path(path.dirname(path.realpath(__file__)))

# Create the Matplotlib window.
fig = plt.figure()

# Get the input filename
filename = str(rootFolder /
               "inputs/alper.jpg") if args["image"] is None else args["image"]

image = cv2.imread(filename)

################################################
# Your code here

# Convert images from BGR to HSV
# Split the image into its channels
# Create an array of 0s
# Display the H, S, and V channels
################################################
img_height, img_width = image.shape[:2]

# Convert images from BGR to HSV
image_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Split the image into its channels
channel_h, channel_s, channel_v = cv2.split(image_hsv)

# Create an array of 0s
zeros = np.array(np.zeros((img_height, img_width)), dtype=np.uint8)

# Channels contain only the associated color and black pixels
h_channel = cv2.merge([channel_h, zeros, zeros])
s_channel = cv2.merge([zeros, channel_s, zeros])
v_channel = cv2.merge([zeros, zeros, channel_v])

plt.imshow(v_channel)

# Show the final image.
plt.show()
