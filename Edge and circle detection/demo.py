import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
import sobel_edge as SOBEL
import log_edge as LOG
import circ_hough as CIRC

filename1 = r"C:\Users\anato\OneDrive\Υπολογιστής\DIP\ex2\basketball_large.png"                         #Path to the image
img = Image.open(filename1).convert('L')                                                                #Convert the image to grayscale
resized_image = img.resize((1001,743))                                                                  #Resize the image to half its original size
resized_image.save(r"C:\Users\anato\OneDrive\Υπολογιστής\DIP\ex2\basketball_large_half.png")            #Save the resized image
img = Image.open(r"C:\Users\anato\OneDrive\Υπολογιστής\DIP\ex2\basketball_large_half.png").convert('L') #Convert the image to grayscale
in_img_array = np.array(img) / 255.0                                                                    #Normalize the pixel values to [0, 1]

# --- SOBEL EDGE DETECTION ---

#Apply Sobel Edge Detection for 4 different thresholds 
edges = []
thresholds = [0.06, 0.1, 0.2, 0.3]

fig1 = plt.figure(figsize=(12, 8))

#Display the 4 Sobel edge images
for i, thres in enumerate(thresholds):
    sobel_img = SOBEL.sobel_edge(in_img_array, thres)
    edges.append(np.count_nonzero(sobel_img))  #Count edge pixels 

    ax = fig1.add_subplot(2, 2, i + 1)  
    ax.imshow(sobel_img, cmap='gray')
    ax.set_title(f'Threshold = {thres}')
    ax.axis('off')

fig1.suptitle('Sobel Edge Detection for 4 Different Thresholds', fontsize=16)
plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.show()

#Plot of threshold vs number of edge pixels 
fig2 = plt.figure(figsize=(8, 6)) 
plt.plot(thresholds, edges, marker='o', color='blue')
plt.title('Number of Edge Pixels vs Threshold')
plt.xlabel('Threshold')
plt.ylabel('Number of edge pixels')
plt.grid(True)
plt.xticks(thresholds)
plt.tight_layout
plt.show()

#  --- LOG EDGE DETECTION ---

log_img = LOG.log_edge(in_img_array)

#Display the results
fig = plt.figure(figsize=(12, 8))
fig.suptitle('LoG Edge Detection', fontsize=16)

plt.subplot(1, 2, 1)
plt.imshow(in_img_array, cmap='gray')
plt.title('Original Image')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(log_img, cmap='gray')
plt.title('LoG Edge Detection')
plt.axis('off') 

plt.show()

#  --- CIRCLE DETECTION USING HOUGH TRANSFORM ---

# Define 5 different Vmin values for circle detection
sobel_vmin_values = [300, 540, 780, 1000, 1556]
log_vmin_values = [250, 400, 780, 1000, 1100]

# ---- SOBEL BASED CIRCLE DETECTION ----

sobel_img = SOBEL.sobel_edge(in_img_array, 0.1)
print("Circle Detection using Hough Transfrom and Sobel edge detection")  
print("-----------------------------------------------------")

fig, axes = plt.subplots(1, 5, figsize=(20, 5))
fig.suptitle('Circle Detection using Hough Transform and Sobel Edge Detection', fontsize=16)

for i, vmin in enumerate(sobel_vmin_values):
    centers, radii, votes = CIRC.circ_hough(sobel_img, 250, 290, np.array([200, 150, 5]), vmin)
    
    ax = axes[i]
    ax.imshow(in_img_array, cmap='gray')
    
    for j in range(len(centers)):
        x, y = centers[j]
        r = radii[j]
        if x != 0 and y != 0:
            print(f"For V_min = ({vmin}) we have: Center: ({x:.2f}, {y:.2f}), Radius: {r:.2f}, Votes: {votes[j]}")  #Print the center, radius and votes of each detected circle
            circle = plt.Circle((x, y), r, color='r', fill=False, linewidth=2)
            ax.add_artist(circle)
            ax.plot(x, y, 'ko')
    
    ax.set_xlim(0, in_img_array.shape[1])
    ax.set_ylim(in_img_array.shape[0], 0)
    ax.set_title(f'Vmin = {vmin}, {len(centers)} circle(s) detected')
    ax.axis('off')

plt.tight_layout(rect=[0, 0.03, 1, 0.90])
plt.show()

# ---- LoG BASED CIRCLE DETECTION ----

print("\nCircle Detection using Hough Transfrom and Log edge detection")  
print("-----------------------------------------------------")

fig, axes = plt.subplots(1, 5, figsize=(20, 5))
fig.suptitle('Circle Detection using Hough Transform and LoG Edge Detection', fontsize=16)

for i, vmin in enumerate(log_vmin_values):
    centers, radii, votes = CIRC.circ_hough(log_img, 250, 290, np.array([200, 150, 5]), vmin)
    
    ax = axes[i]
    ax.imshow(in_img_array, cmap='gray')
    
    for j in range(len(centers)):
        x, y = centers[j]
        r = radii[j]
        if x != 0 and y != 0:
            print(f"For V_min = ({vmin}) we have: Center: ({x:.2f}, {y:.2f}), Radius: {r:.2f}, Votes: {votes[j]}")  #Print the center, radius and votes of each detected circle
            circle = plt.Circle((x, y), r, color='r', fill=False, linewidth=2)
            ax.add_artist(circle)
            ax.plot(x, y, 'ko')
    
    ax.set_xlim(0, in_img_array.shape[1])
    ax.set_ylim(in_img_array.shape[0], 0)
    ax.set_title(f'Vmin = {vmin}, {len(centers)} circle(s) detected')
    ax.axis('off')

plt.tight_layout(rect=[0, 0.03, 1, 0.90])
plt.show()