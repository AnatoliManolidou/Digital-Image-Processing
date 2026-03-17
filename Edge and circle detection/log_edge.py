import numpy as np
import fir_conv as CONV
from scipy.ndimage import gaussian_filter

def log_edge(in_img_array: np.ndarray) -> np.ndarray:
    # Define the LoG mask
    log_mask = np.array([[0, 0, -1, 0, 0],
                         [0, -1, -2, -1, 0],
                         [-1, -2, 16, -2, -1],
                         [0, -1, -2, -1, 0],
                         [0, 0, -1, 0, 0]])
    
    # Smooth the input image using Gaussian filter
    smoothed_img = gaussian_filter(in_img_array, sigma=1.5)

    # Convolve smoothed image with LoG mask
    log_img = CONV.fir_conv(smoothed_img, log_mask)

    # Initialize output image
    edge_img = np.zeros_like(log_img)

    threshold = 0.2

    # Iterate over each pixel except borders
    for i in range(1, log_img.shape[0] - 1):
        for j in range(1, log_img.shape[1] - 1):
            patch = log_img[i-1:i+2, j-1:j+2]
            center = patch[1, 1]

            # Neighbors
            neighbors = [
                patch[0, 0], patch[0, 1], patch[0, 2],  # Top row (lu, up, ru)
                patch[1, 0],             patch[1, 2],  # Left, Right
                patch[2, 0], patch[2, 1], patch[2, 2]   # Bottom row (ld, down, rd)
            ]

            # Strategy 1: Sign change with center and enough contrast
            opposite_signs = sum(
                1 for neighbor in neighbors
                if np.sign(center) != np.sign(neighbor) and abs(center - neighbor) > threshold
            )

            if opposite_signs >= 2:
                edge_img[i, j] = 1
                continue  # Skip to next pixel once edge is detected

            # Strategy 2: Diagonal pair checks (neighbor-to-neighbor transitions)
            diagonal_pairs = [
                (patch[0, 0], patch[1, 1]),  # lu - center
                (patch[0, 2], patch[1, 1]),  # ru - center
                (patch[2, 0], patch[1, 1]),  # ld - center
                (patch[2, 2], patch[1, 1]),  # rd - center
                (patch[0, 0], patch[2, 2]),  # lu - rd
                (patch[0, 2], patch[2, 0])   # ru - ld
            ]

            for a, b in diagonal_pairs:
                if np.sign(a) != np.sign(b) and abs(a - b) > threshold:
                    edge_img[i, j] = 1
                    break  # Break inner loop once edge is detected

    return edge_img
