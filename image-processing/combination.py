import numpy as np
from skimage.color import rgb2gray
from skimage.exposure import match_histograms
from skimage.metrics import structural_similarity

def find_difference(img1, img2):
    assert img1.shape == img2.shape, "Specify 2 images with the same shape"
    gray_img1 = rgb2gray(img1)
    gray_img2 = rgb2gray(img2)
    (score, difference_image) = structural_similarity(gray_img1, gray_img2, full = True)
    print("Similatiry of the images: ", score)
    normalize_difference_image = (difference_image-np.min(difference_image))/(np.max(difference_image)-np.min(difference_image))
    return normalize_difference_image

def transfer_histogram(img1, img2):
    matched_image = match_histograms(img1, img2, multichannel = True)
    return matched_image

    
