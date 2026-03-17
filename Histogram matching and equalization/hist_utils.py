import numpy as np
from typing import Dict

def calculate_hist_of_img(
    img_array: np.ndarray,
    return_normalized: bool
) -> Dict:
  
    #Checking if the given image is grayscale or not
    if len(img_array.shape) == 2:  #Grayscale Image

        unique, counts = np.unique(img_array, return_counts=True) #Counting occurrences of each element in img_array
        
        if return_normalized: #If the user wants normalized histogram
            counts = counts / img_array.size

        hist = {float(u): float(c) for u, c in zip(unique, counts)} #Creating a dictionary with unique pixel values as keys and their counts as values
        return hist
    
    elif len(img_array.shape) == 3 and img_array.shape[2] == 3: #RGB Image

        print("This is not a grayscale image. Exiting...")
        return None

def apply_hist_modification_transform(
    img_array: np.ndarray,
    modification_transform: Dict
) -> np.ndarray:
    
    modified_img = np.zeros_like(img_array, dtype=float) #Creating an empty array of the same shape as the input image

    #Iterating through each pixel in the image and applying the transformation
    for i in range(img_array.shape[0]):
        for j in range(img_array.shape[1]):
            key = img_array[i, j] #Getting the current pixel value
            mapped_val = modification_transform.get(key, 0.0) #Getting the mapped value from the transformation dictionary
            modified_img[i, j] = mapped_val #Assigning the mapped value to the modified image

    return modified_img