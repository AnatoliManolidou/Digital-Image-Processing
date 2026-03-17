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

# Apply n_cuts_recursive for T1 = 5 and T2 = 0.2

# For d2a 
label1a = nc.n_cuts_recursive(d2a_affinity, 5, 0.2)
print("Labels for d2a with k=2:", label1a)
fig, axs = plt.subplots(1, 2, figsize=(8, 4))
axs[0].imshow(d2a)
axs[0].set_title("Input Image")
axs[0].axis('off')
axs[1].imshow(label1a.reshape(M, N), cmap='tab10')
axs[1].set_title("Clusters for d2a")
axs[1].axis('off')
plt.tight_layout()
plt.show()

# For d2b
label1b = nc.n_cuts_recursive(d2b_affinity, 5, 0.2)
print("Labels for d2b with k=2:", label1b)
fig, axs = plt.subplots(1, 2, figsize=(8, 4))
axs[0].imshow(d2b)
axs[0].set_title("Input Image")
axs[0].axis('off')
axs[1].imshow(label1b.reshape(M, N), cmap='tab10')
axs[1].set_title("Clusters for d2b")
axs[1].axis('off')
plt.tight_layout()
plt.show()
