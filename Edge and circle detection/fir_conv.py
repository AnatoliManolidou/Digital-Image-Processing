import numpy as np

def fir_conv(
        in_img_array: np.ndarray,   #Grayscale input image array 
        h: np.ndarray,              #Convolution mask 
) -> np.ndarray:                    #As outputs we have the convolved image 

        #Perform the convolution operation on the input image using the convolution mask

        #Get the dimensions of the input image and the convolution mask
        in_height, in_width = in_img_array.shape
        mask_height, mask_width = h.shape
        
        #Calculate the padding size for the input image
        pad_height = mask_height // 2
        pad_width = mask_width // 2
        
        #Pad the input image with zeros on all sides
        padded_img = np.pad(in_img_array, ((pad_height, pad_height), (pad_width, pad_width)), mode='constant', constant_values=0)
        
        #Initialize the output image with zeros
        out_img_array = np.zeros_like(in_img_array)

        #Flip the convolution mask
        h = np.flipud(np.fliplr(h))
        
        #Perform the convolution operation
        for i in range(in_height):
                for j in range(in_width):
                        out_img_array[i, j] = np.sum(h * padded_img[i:i + mask_height, j:j + mask_width])
        
        return out_img_array
