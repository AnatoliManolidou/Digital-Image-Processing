import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import hist_utils as DIP1
import hist_modif as DIP2

def draw_grayscale_bar(ax): #Create a vertical grayscale bar
    gradient = np.linspace(0, 1, 256).reshape(256, 1)  
    ax.imshow(gradient, cmap="gray", aspect="auto")
    ax.set_yticks([0, 64, 128, 192, 255])
    ax.set_yticklabels(["0.0", "0.25", "0.5", "0.75", "1.0"])
    ax.set_xticks([])
    ax.set_box_aspect(6)

#Set the filepath to the image file
filename1 = r"C:\Users\anato\OneDrive\Εικόνες\hw1_images\input_img.jpg" 
filename2 = r"C:\Users\anato\OneDrive\Εικόνες\hw1_images\ref_img.jpg"

#Read the image into a PIL entity and keep only the Luminance component of the image
img1 = Image.open(filename1).convert("L")
img2 = Image.open(filename2).convert("L")

#Obtain the underlying np array
input_img = np.array(img1).astype(float) / 255.0
ref_img = np.array(img2).astype(float) / 255.0

hist_input_img = DIP1.calculate_hist_of_img(input_img, return_normalized=False)
hist_ref_img = DIP1.calculate_hist_of_img(ref_img, return_normalized=True)

match_greedy = DIP2.perform_hist_matching(input_img, ref_img, mode="greedy")
match_non_greedy = DIP2.perform_hist_matching(input_img, ref_img, mode="non-greedy")
match_post = DIP2.perform_hist_matching(input_img, ref_img, mode="post-disturbance")

hist_match_greedy = DIP1.calculate_hist_of_img(match_greedy, return_normalized=False)
hist_match_non_greedy = DIP1.calculate_hist_of_img(match_non_greedy, return_normalized=False)
hist_match_post = DIP1.calculate_hist_of_img(match_post, return_normalized=False)

fig, axes = plt.subplots(5, 3, figsize=(14, 14), gridspec_kw={'width_ratios': [4, 4, 0.3]})

# ----- Histogram Matching -----

# Input Image
axes[0, 0].imshow(input_img, cmap="gray")
axes[0, 0].set_title("Input Image")
axes[0, 0].axis("off")

axes[0, 1].bar(hist_input_img.keys(), hist_input_img.values(), width=0.005, edgecolor='blue')
axes[0, 1].set_title("Input Histogram")
axes[0, 1].set_xlabel("Pixel Value")
axes[0, 1].set_ylabel("Frequency")

draw_grayscale_bar(axes[0, 2])

# Reference Image
axes[1, 0].imshow(ref_img, cmap="gray")
axes[1, 0].set_title("Reference Image")
axes[1, 0].axis("off")

axes[1, 1].bar(hist_ref_img.keys(), hist_ref_img.values(), width=0.005, edgecolor='blue')
axes[1, 1].set_title("Reference Histogram")
axes[1, 1].set_xlabel("Pixel Value")
axes[1, 1].set_ylabel("Normalized Frequency")

draw_grayscale_bar(axes[1, 2])

# Greedy Matching
axes[2, 0].imshow(match_greedy, cmap="gray")
axes[2, 0].set_title("Greedy Matching")
axes[2, 0].axis("off")

axes[2, 1].bar(hist_match_greedy.keys(), hist_match_greedy.values(), width=0.005, color = 'green', edgecolor='purple')
axes[2, 1].set_title("Greedy Matched Histogram")
axes[2, 1].set_xlabel("Pixel Value")
axes[2, 1].set_ylabel("Frequency")

draw_grayscale_bar(axes[2, 2])

# Non-Greedy Matching
axes[3, 0].imshow(match_non_greedy, cmap="gray")
axes[3, 0].set_title("Non-Greedy Matching")
axes[3, 0].axis("off")

axes[3, 1].bar(hist_match_non_greedy.keys(), hist_match_non_greedy.values(), width=0.005, color = 'green', edgecolor='purple')
axes[3, 1].set_title("Non-Greedy Matched Histogram")
axes[3, 1].set_xlabel("Pixel Value")
axes[3, 1].set_ylabel("Frequency")

draw_grayscale_bar(axes[3, 2])

# Post-Disturbance Matching
axes[4, 0].imshow(match_post, cmap="gray")
axes[4, 0].set_title("Post-Disturbance Matching")
axes[4, 0].axis("off")

axes[4, 1].bar(hist_match_post.keys(), hist_match_post.values(), width=0.005,  color = 'green', edgecolor='purple')
axes[4, 1].set_title("Post-Disturbance Matched Histogram")
axes[4, 1].set_xlabel("Pixel Value")
axes[4, 1].set_ylabel("Frequency")

draw_grayscale_bar(axes[4, 2])

plt.tight_layout()
plt.savefig("histogram_matching_results.png", dpi=300)
plt.show()

# ----- Histogram Equalization -----
eq_greedy = DIP2.perform_hist_eq(input_img, mode="greedy")
eq_non_greedy = DIP2.perform_hist_eq(input_img, mode="non-greedy")
eq_post = DIP2.perform_hist_eq(input_img, mode="post-disturbance")

hist_eq_greedy = DIP1.calculate_hist_of_img(eq_greedy, return_normalized=False)
hist_eq_non_greedy = DIP1.calculate_hist_of_img(eq_non_greedy, return_normalized=False)
hist_eq_post = DIP1.calculate_hist_of_img(eq_post, return_normalized=False)

fig, axes = plt.subplots(4, 3, figsize=(14, 12), gridspec_kw={'width_ratios': [4, 4, 0.3]})

# Input Image
axes[0, 0].imshow(input_img, cmap="gray")
axes[0, 0].set_title("Input Image")
axes[0, 0].axis("off")

axes[0, 1].bar(hist_input_img.keys(), hist_input_img.values(), width=0.005, edgecolor='blue')
axes[0, 1].set_title("Input Histogram")
axes[0, 1].set_xlabel("Pixel Value")
axes[0, 1].set_ylabel("Frequency")

draw_grayscale_bar(axes[0, 2])

# Greedy Equalization
axes[1, 0].imshow(eq_greedy, cmap="gray")
axes[1, 0].set_title("Greedy Equalization")
axes[1, 0].axis("off")

axes[1, 1].bar(hist_eq_greedy.keys(), hist_eq_greedy.values(), width=0.005, color = 'green', edgecolor='purple')
axes[1, 1].set_title("Greedy Equalized Histogram")
axes[1, 1].set_xlabel("Pixel Value")
axes[1, 1].set_ylabel("Frequency")

draw_grayscale_bar(axes[1, 2])

# Non-Greedy Equalization
axes[2, 0].imshow(eq_non_greedy, cmap="gray")
axes[2, 0].set_title("Non-Greedy Equalization")
axes[2, 0].axis("off")

axes[2, 1].bar(hist_eq_non_greedy.keys(), hist_eq_non_greedy.values(), width=0.005, color = 'green', edgecolor='purple')
axes[2, 1].set_title("Non-Greedy Equalized Histogram")
axes[2, 1].set_xlabel("Pixel Value")
axes[2, 1].set_ylabel("Frequency")

draw_grayscale_bar(axes[2, 2])

# Post-Disturbance Equalization
axes[3, 0].imshow(eq_post, cmap="gray")
axes[3, 0].set_title("Post-Disturbance Equalization")
axes[3, 0].axis("off")

axes[3, 1].bar(hist_eq_post.keys(), hist_eq_post.values(), width=0.005, color = 'green', edgecolor='purple')
axes[3, 1].set_title("Post-Disturbance Equalized Histogram")
axes[3, 1].set_xlabel("Pixel Value")
axes[3, 1].set_ylabel("Frequency")

draw_grayscale_bar(axes[3, 2])

plt.tight_layout()
plt.savefig("histogram_equalization_results.png", dpi=300)
plt.show()
