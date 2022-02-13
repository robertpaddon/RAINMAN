import cv2
import numpy as np
from skimage.util import random_noise

# load sample background and sample card
background = cv2.imread("backgrounds/knitted_0168.jpg")
card = cv2.imread("cards-dataset/Qc.png")

# scale card image down to be smaller than background
scale_percent = 20
width = int(card.shape[1] * scale_percent / 100)
height = int(card.shape[0] * scale_percent / 100)
dim = (width, height)
card = cv2.resize(card, dim, interpolation = cv2.INTER_AREA)

# superimpose the card image over the background
x_offset=y_offset=50
background[y_offset:y_offset+card.shape[0], x_offset:x_offset+card.shape[1]] = card

# add noise to the image
background = random_noise(background, mode='gaussian', var=0.05**2)

# show the final image
cv2.imshow('image',background)
cv2.waitKey(0)