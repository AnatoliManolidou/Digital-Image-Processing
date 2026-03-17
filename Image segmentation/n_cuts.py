import numpy as np
from sklearn.cluster import KMeans
from scipy.linalg import eigh

def n_cuts(
        affinity_mat: np.ndarray, 
        k: int 
) -> np.ndarray: 

        #Calculate Laplacian matrix
        D = np.diag(np.sum(affinity_mat, axis=1))
        L = D - affinity_mat

        #Solving Lx=λDx
        eigenvalues, eigenvectors = eigh(L, D, subset_by_index=[0, k-1])

        #Matrix U has as columns the eigenvectors
        U = eigenvectors

        #Applying k-means algorithm

        #Setting the random_state parameter to 1, to ensure reproducibility across experiments.
        kmeans = KMeans(n_clusters=k, random_state=1)

        #U refers to the input data matrix
        kmeans.fit(U)

        #Obtain the cluster labels for each input data point
        cluster_idx = kmeans.labels_ 

        return cluster_idx

def calculate_n_cut_value(
        affinity_mat: np.ndarray, 
        cluster_idx: np.ndarray 
) -> float:
    
    A = np.where(cluster_idx == 0)[0] #Nodes of the first cluster
    B = np.where(cluster_idx == 1)[0] #Nodes of the second cluster

    #assoc(A,V) is the sum of all the weights between the nodes of A (first label) and the nodes of V (second label)
    
    assoc_A_A = np.sum(affinity_mat[np.ix_(A,A)])  #Sum of weights within cluster A
    assoc_B_B = np.sum(affinity_mat[np.ix_(B,B)])  #Sum of weights within cluster B

    assoc_A_V = np.sum(affinity_mat[A, :])  
    assoc_B_V = np.sum(affinity_mat[B, :])

    N_assoc_A_B = (assoc_A_A/assoc_A_V) + (assoc_B_B/assoc_B_V)

    N_cut_A_B = 2 - N_assoc_A_B

    return N_cut_A_B


def n_cuts_recursive(
        affinity_mat: np.ndarray, 
        T1: int,
        T2: int,
) -> np.ndarray: 

    cluster_idx = n_cuts(affinity_mat, 2)
    n_cut_value = calculate_n_cut_value(affinity_mat, cluster_idx)

    A = np.where(cluster_idx == 0)[0] #Nodes of the first cluster
    B = np.where(cluster_idx == 1)[0] #Nodes of the second cluster

    if(len(A) < T1 or len(B) < T1 or n_cut_value > T2):
        return cluster_idx
    
    #Split each cluster into two subclusters ans continue recursively

    cluster_idx_0 = n_cuts_recursive(affinity_mat[np.ix_(A, A)], T1, T2)
    cluster_idx_1 = n_cuts_recursive(affinity_mat[np.ix_(B, B)], T1, T2)

    cluster_idx_result = np.zeros_like(cluster_idx)

    cluster_idx_result[A] = cluster_idx_0
    cluster_idx_result[B] = cluster_idx_1 + np.max(cluster_idx_0) + 1

    return cluster_idx_result

