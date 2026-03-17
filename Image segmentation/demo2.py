from scipy.io import loadmat
import image_to_graph as itg
import spectral_clustering as sc
import matplotlib.pyplot as plt

data = loadmat("dip_hw_3.mat")
d2a = data["d2a"]
d2b = data["d2b"]

d2a_affinity = itg.image_to_graph(d2a)
d2b_affinity = itg.image_to_graph(d2b)

M, N, _ = d2a.shape

def show_comparison(image, labels, k, title_prefix):
    fig, axs = plt.subplots(1, 2, figsize=(8, 4))
    axs[0].imshow(image)
    axs[0].set_title(f"Input Image")
    axs[0].axis('off')
    axs[1].imshow(labels.reshape(M, N), cmap='tab10')
    axs[1].set_title(f"{title_prefix} (k={k})")
    axs[1].axis('off')
    plt.tight_layout()
    plt.show()

label1a = sc.spectral_clustering(d2a_affinity, 2)
print("Labels for d2a with k=2:", label1a)
show_comparison(d2a, label1a, 2, "Clusters for input image (d2a)")

label2a = sc.spectral_clustering(d2a_affinity, 3)
print("Labels for d2a with k=3:", label2a)
show_comparison(d2a, label2a, 3, "Clusters for input image (d2a)")

label3a = sc.spectral_clustering(d2a_affinity, 4)
print("Labels for d2a with k=4:", label3a)
show_comparison(d2a, label3a, 4, "Clusters for input image (d2a)")

label1b = sc.spectral_clustering(d2b_affinity, 2)
print("Labels for d2b with k=2:", label1b)
show_comparison(d2b, label1b, 2, "Clusters for input image (d2b)")

label2b = sc.spectral_clustering(d2b_affinity, 3)
print("Labels for d2b with k=3:", label2b)
show_comparison(d2b, label2b, 3, "Clusters for input image (d2b)")

label3b = sc.spectral_clustering(d2b_affinity, 4)
print("Labels for d2b with k=4:", label3b)
show_comparison(d2b, label3b, 4, "Clusters for input image (d2b)")
