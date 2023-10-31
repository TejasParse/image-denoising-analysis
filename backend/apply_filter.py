import cv2
from io import BytesIO
import numpy as np
from PIL import Image
from brisque import BRISQUE
import numpy as np
from scipy.signal import wiener

obj = BRISQUE(url=False)

from math import log10, sqrt

def PSNR(original, compressed):
    mse = np.mean((original - compressed) ** 2)
    if(mse == 0): 
        return 100
    max_pixel = 255.0
    psnr = 20 * log10(max_pixel / sqrt(mse))
    return psnr

def wienerFilter(original_img, filter_size):
    
    mysize = filter_size

    originalBrisqueScore = obj.score(original_img)
    noise = np.var(original_img[:mysize, :mysize])
    img_filtered = wiener(original_img, mysize=mysize, noise=noise)
        
    newBrisque = obj.score(img_filtered)
    newPsnr = PSNR(original_img, img_filtered)
    
    return [img_filtered, originalBrisqueScore, newBrisque, newPsnr]

def apply_filter(image, function_name):

    if function_name == 'Weiner':
        image = wienerFilter(image, 5)

    return image


def normalizeVector(arra):
    
    return (arra-np.min(arra))/(np.max(arra)-np.min(arra))

def process_image(file):
 
    image = np.array(Image.open(file))

    oldScore = obj.score(image)
    print(oldScore, "Original Image Score")
    
    function_name = 'Weiner'  # Example: Always apply the Canny filter


    processed_data = apply_filter(image, function_name)
    # print(processed_data)

    return processed_data
