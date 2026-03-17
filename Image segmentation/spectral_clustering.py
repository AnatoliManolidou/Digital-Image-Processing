import numpy as np
from sklearn.cluster import KMeans
from scipy.sparse.linalg import eigsh

def spectral_clustering(
        affinity_mat: np.ndarray,
        k: int
) -> np.ndarray:
    
    #Calculating Laplacian matrix
    D = np.diag(np.sum(affinity_mat, axis=1))
    L = D - affinity_mat

    #Finding the k smallest eigenvalues and their corresponding eigenvectors using spicy.sparse.linalg.eigs
    eigenvalues, eigenvectors = eigsh(L, k = k, which='SM', return_eigenvectors=True)

    #U matrix has as columns the eigenvectors
    U = eigenvectors

    #Applying k-means algorithm

    #Setting the random_state parameter to 1, to ensure reproducibility across experiments.
    kmeans = KMeans(n_clusters=k, random_state=1)

    #U refers to the input data matrix
    kmeans.fit(U)

    #Obtain the cluster labels for each input data point
    cluster_idx = kmeans.labels_

    return cluster_idx