import numpy as np
import fir_conv as CONV

def sobel_edge(
        in_img_array: np.ndarray,   #Grayscale input image array 
        thres: float                #Threshold of the value of the gradient to consider the edge
) -> np.ndarray:                    #Output image with values either 0 or 1


        #Define the Sobel masks for x and y directions
        sobel_x = np.array([[-1, 0, 1],
                            [-2, 0, 2],
                            [-1, 0, 1]])
        
        sobel_y = np.array([[1, 2, 1],
                            [0, 0, 0],
                            [-1, -2, -1]])
        
        #Perform the convolution operation using the Sobel masks
        grad_x = CONV.fir_conv(in_img_array, sobel_x)

        grad_y = CONV.fir_conv(in_img_array, sobel_y)
        #Calculate the gradient magnitude
        grad_magnitude = np.sqrt(grad_x**2 + grad_y**2)

        #Normalize the gradient magnitude to the range [0, 1]
        grad_magnitude = grad_magnitude / np.max(grad_magnitude)

        #Threshold the gradient magnitude to create a binary edge image
        edge_img = np.where(grad_magnitude > thres, 1, 0)

        return edge_img
