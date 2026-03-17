import numpy as np
from typing import Dict
from hist_utils import calculate_hist_of_img, apply_hist_modification_transform

def perform_hist_modification(
    img_array: np.ndarray,
    hist_ref: Dict,
    mode: str
) -> np.ndarray:

    input_hist = calculate_hist_of_img(img_array, return_normalized=False)
    if input_hist is None:
        print("Error: Unable to calculate histogram for the image.")
        return None

    input_levels = list(sorted(input_hist.keys())) #Sorting the keys of the input histogram
    input_counts = np.array([input_hist[key] for key in input_levels]) #Creating an array of counts for the input histogram
    total_samples = img_array.size

    output_levels = np.linspace(0.0, 1.0, len(hist_ref)) #Creating an array of output levels
    output_probs = np.array(list(hist_ref.values())) #Creating an array of the probabilities
    output_counts = output_probs * total_samples #(N · pref(gi))

    greedy = {} 
    non_greedy = {} 
    post_disturbance = {} 

    if mode == "greedy":

        j = 0 #Index for output levels
        count_g = 0 #Count of input levels

        #Iterating through the input levels and mapping them to output levels
        for i in range(len(input_levels)):

            count_g += input_counts[i] #Updating the count of input levels
            greedy[input_levels[i]] = output_levels[j]  #Mapping the input level to the output level

            if count_g >= output_counts[j] and count_g - input_counts[i] < output_counts[j]:
                j += 1 #Moving to the next output level
                count_g = 0

        return apply_hist_modification_transform(img_array, greedy)

    if mode == "non-greedy":

        j = 0 #Index for output levels
        count_g = 0 # Count of input levels

        for i in range(len(input_levels)):

            count_g += input_counts[i] #Updating the count of input levels
            deficiency = output_counts[j] - count_g #Calculating the deficiency

            if deficiency >= input_counts[i] / 2: #Mapping to the current output level

                non_greedy[input_levels[i]] = output_levels[j]
            else: #Moving on to the next output level
            
                j += 1
                non_greedy[input_levels[i]] = output_levels[j] #Mapping to the next output level
                count_g = input_counts[i] #Reset count_g to the current input level count

        return apply_hist_modification_transform(img_array, non_greedy)

    if mode == "post-disturbance":

        d = 1.0 / (len(input_levels) - 1) #Calculating the distance between levels

        noise = np.random.uniform(-d/2, d/2, size=img_array.shape) #Generating random uniform noise

        disturbed_img = img_array + noise #Adding noise to the image
        disturbed_img = np.clip(disturbed_img, 0.0, 1.0) #Clipping the values to be between 0 and 1

        post_disturbance = perform_hist_modification(disturbed_img, hist_ref, mode="greedy") #Performing greedy histogram modification on the disturbed image
        return post_disturbance

    if mode not in ['greedy', 'non-greedy', 'post_disturbance']:
        print("Invalid mode selected. Exiting...")
        return None

def perform_hist_eq(
    img_array: np.ndarray,
    mode: str
) -> np.ndarray:
  
    unique_vals = np.unique(img_array) #Finding unique values in the image array
    L = len(unique_vals) 
    uniform_hist = {v: 1.0/L for v in unique_vals} #Creating a uniform histogram

    return perform_hist_modification(img_array, uniform_hist, mode)

def perform_hist_matching(
    img_array: np.ndarray,
    img_array_ref: np.ndarray,
    mode: str
) -> np.ndarray:

    hist_ref = calculate_hist_of_img(img_array_ref, return_normalized=True) 

    return perform_hist_modification(img_array, hist_ref, mode)
