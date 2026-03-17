import numpy as np

def image_to_graph(
        img_array: np.ndarray, 
) -> np.ndarray: 

    #Checking if the input image array is 3-dimensional    
    if img_array.ndim != 3:
        raise ValueError("Input image array must be 3-dimensional (M, N, C)")
    
    M, N, C = img_array.shape

    #Reshaping the image array to a 2D array of shape (MN, C)
    array = img_array.reshape(M * N, C)

    #Calculating the euclidean distance between the channels
    diff = array[:, np.newaxis, :] - array[np.newaxis, :, :]

    dist = np.sqrt(np.sum(diff ** 2, axis=-1))

    affinity_mat = 1 / np.exp(dist)

    return affinity_mat