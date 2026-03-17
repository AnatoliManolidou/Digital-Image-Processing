from scipy.io import loadmat
import image_to_graph as itg
import n_cuts as nc
import matplotlib.pyplot as plt

data = loadmat("dip_hw_3.mat")
d2a = data["d2a"]
d2b = data["d2b"]

d2a_affinity = itg.image_to_graph(d2a)
d2b_affinity = itg.image_to_graph(d2b)

M, N, _ = d2a.shape

# For d2a with k=2
label1a = nc.n_cuts(d2a_affinity, 2)
print("Labels for d2a with k=2:", label1a)
fig, axs = plt.subplots(1, 2, figsize=(8, 4))
axs[0].imshow(d2a)
axs[0].set_title("Input Image")
axs[0].axis('off')
axs[1].imshow(label1a.reshape(M, N), cmap='tab10')
axs[1].set_title("Clusters for input image (d2a) (k=2)")
axs[1].axis('off')
plt.tight_layout()
plt.show()

# For d2b with k=2
label1b = nc.n_cuts(d2b_affinity, 2)
print("Labels for d2b with k=2:", label1b)
fig, axs = plt.subplots(1, 2, figsize=(8, 4))
axs[0].imshow(d2b)
axs[0].set_title("Input Image")
axs[0].axis('off')
axs[1].imshow(label1b.reshape(M, N), cmap='tab10')
axs[1].set_title("Clusters for input image (d2b)(k=2)")
axs[1].axis('off')
plt.tight_layout()
plt.show()

# For d2a with k=3
label2a = nc.n_cuts(d2a_affinity, 3)
print("Labels for d2a with k=3:", label2a)
fig, axs = plt.subplots(1, 2, figsize=(8, 4))
axs[0].imshow(d2a)
axs[0].set_title("Input Image")
axs[0].axis('off')
axs[1].imshow(label2a.reshape(M, N), cmap='tab10')
axs[1].set_title("Clusters input image (d2a) (k=3)")
axs[1].axis('off')
plt.tight_layout()
plt.show()

# For d2b with k=3
label2b = nc.n_cuts(d2b_affinity, 3)
print("Labels for d2b with k=3:", label2b)
fig, axs = plt.subplots(1, 2, figsize=(8, 4))
axs[0].imshow(d2b)
axs[0].set_title("Input Image")
axs[0].axis('off')
axs[1].imshow(label2b.reshape(M, N), cmap='tab10')
axs[1].set_title("Clusters for input image (d2b) (k=3)")
axs[1].axis('off')
plt.tight_layout()
plt.show()

# For d2a with k=4
label3a = nc.n_cuts(d2a_affinity, 4)
print("Labels for d2a with k=4:", label3a)
fig, axs = plt.subplots(1, 2, figsize=(8, 4))
axs[0].imshow(d2a)
axs[0].set_title("Input Image")
axs[0].axis('off')
axs[1].imshow(label3a.reshape(M, N), cmap='tab10')
axs[1].set_title("Clusters for input image (d2a)(k=4)")
axs[1].axis('off')
plt.tight_layout()
plt.show()

# For d2b with k=4
label3b = nc.n_cuts(d2b_affinity, 4)
print("Labels for d2b with k=4:", label3b)
fig, axs = plt.subplots(1, 2, figsize=(8, 4))
axs[0].imshow(d2b)
axs[0].set_title("Input Image")
axs[0].axis('off')
axs[1].imshow(label3b.reshape(M, N), cmap='tab10')
axs[1].set_title("Clusters for input image (d2b)(k=4)")
axs[1].axis('off')
plt.tight_layout()
plt.show()