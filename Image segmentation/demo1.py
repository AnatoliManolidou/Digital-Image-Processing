from scipy.io import loadmat
import spectral_clustering as sc

data = loadmat("dip_hw_3.mat")
d1a = data["d1a"]

label1 = sc.spectral_clustering(d1a, 2)
print("Labels for k=2:", label1)

label2 = sc.spectral_clustering(d1a, 3)
print("Labels for k=3:", label2)

label3 = sc.spectral_clustering(d1a, 4)
print("Labels for k=4:", label3)
