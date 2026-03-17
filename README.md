# Digital-Image-Processing
Projects for the course ''Digital Image Processing'',  2024-25 ECE AUTH
# Digital Image Processing - Work Presentation

Course: Digital Image Processing (ECE AUTH, 2024-25)

This document presents the work completed in the repository across all three assignments, based on:
- Assignment statements: [hw1](Histogram%20matching%20and%20equalization/hw1.pdf), [hw2](Edge%20and%20circle%20detection/hw2.pdf), [hw3](Image%20segmentation/hw3.pdf)
- Submitted reports: [report 1](Histogram%20matching%20and%20equalization/report.pdf), [report 2](Edge%20and%20circle%20detection/report.pdf), [report 3](Image%20segmentation/report.pdf)
- Implemented Python code
- Generated output figures in [Histogram matching results](Histogram%20matching%20and%20equalization/Results), [Edge/Circle outputs](Edge%20and%20circle%20detection/Outputs), [Segmentation outputs](Image%20segmentation/Outputs)

---

## 1. Project Scope and Deliverables

The repository contains three complete assignment blocks:

1. Histogram matching and equalization
2. Edge and circle detection
3. Image segmentation

Each block includes:
- Assignment statement (problem definition)
- Report (methodology + discussion)
- Modular implementation code
- Demo scripts
- Output figures

---

## 2. Assignment 1 - Histogram Matching and Equalization

### Goal (from [hw1.pdf](Histogram%20matching%20and%20equalization/hw1.pdf))
Implement histogram processing algorithms for grayscale images, including:
- Histogram equalization
- Histogram matching to a reference image
- Variants of mapping strategy

### Implemented components
- [hist_utils.py](Histogram%20matching%20and%20equalization/hist_utils.py)
  - Histogram extraction (`calculate_hist_of_img`)
  - Pixelwise intensity remapping (`apply_hist_modification_transform`)
- [hist_modif.py](Histogram%20matching%20and%20equalization/hist_modif.py)
  - Core histogram modification (`perform_hist_modification`)
  - Three modes:
    - `greedy`
    - `non-greedy`
    - `post-disturbance`
  - Equalization wrapper (`perform_hist_eq`)
  - Matching wrapper (`perform_hist_matching`)
- [demo.py](Histogram%20matching%20and%20equalization/demo.py)
  - End-to-end experiment for matching and equalization
  - Visualization of input/reference/output histograms and images

### Produced results
- [histogram_matching_results.png](Histogram%20matching%20and%20equalization/Results/histogram_matching_results.png)
- [histogram_equalization_results.png](Histogram%20matching%20and%20equalization/Results/histogram_equalization_results.png)

### Reported documentation
- [report.pdf](Histogram%20matching%20and%20equalization/report.pdf) includes method descriptions, mode-by-mode behavior, and final conclusions.

---

## 3. Assignment 2 - Edge and Circle Detection

### Goal (from [hw2.pdf](Edge%20and%20circle%20detection/hw2.pdf))
Implement:
- FIR convolution
- Edge detection (Sobel, LoG)
- Circle detection with Hough Transform

### Implemented components
- [fir_conv.py](Edge%20and%20circle%20detection/fir_conv.py)
  - Manual 2D FIR convolution with zero-padding and kernel flipping
- [sobel_edge.py](Edge%20and%20circle%20detection/sobel_edge.py)
  - Sobel gradient computation
  - Gradient magnitude normalization and thresholding
- [log_edge.py](Edge%20and%20circle%20detection/log_edge.py)
  - Gaussian smoothing + LoG filtering
  - Zero-crossing style edge decisions with contrast thresholding
- [circ_hough.py](Edge%20and%20circle%20detection/circ_hough.py)
  - 3D Hough voting space for center/radius bins
  - Circle parameter extraction above vote threshold
- [demo.py](Edge%20and%20circle%20detection/demo.py)
  - Threshold sweep for Sobel edge maps
  - LoG edge visualization
  - Circle detection experiments for multiple `V_min` values

### Produced results
- [Sobel.png](Edge%20and%20circle%20detection/Outputs/Sobel.png)
- [Sobel_plot.png](Edge%20and%20circle%20detection/Outputs/Sobel_plot.png)
- [LoG_0.1.png](Edge%20and%20circle%20detection/Outputs/LoG_0.1.png)
- [LoG_0.2.png](Edge%20and%20circle%20detection/Outputs/LoG_0.2.png)
- [Hough_Sobel.png](Edge%20and%20circle%20detection/Outputs/Hough_Sobel.png)
- [Hough_LoG.png](Edge%20and%20circle%20detection/Outputs/Hough_LoG.png)

### Reported documentation
- [report.pdf](Edge%20and%20circle%20detection/report.pdf) is organized by module ([fir_conv.py](Edge%20and%20circle%20detection/fir_conv.py), [sobel_edge.py](Edge%20and%20circle%20detection/sobel_edge.py), [log_edge.py](Edge%20and%20circle%20detection/log_edge.py), [circ_hough.py](Edge%20and%20circle%20detection/circ_hough.py)) and concludes with qualitative results and observations.

---

## 4. Assignment 3 - Image Segmentation

### Goal (from [hw3.pdf](Image%20segmentation/hw3.pdf))
Implement image segmentation with graph-based methods:
- Image to graph affinity modeling
- Spectral clustering
- Normalized cuts (non-recursive and recursive)

### Implemented components
- [image_to_graph.py](Image%20segmentation/image_to_graph.py)
  - Converts an image `[M, N, C]` into an affinity matrix `[MN, MN]`
  - Affinity based on channel-space Euclidean distance
- [spectral_clustering.py](Image%20segmentation/spectral_clustering.py)
  - Laplacian construction
  - Smallest-eigenvector embedding
  - KMeans clustering in spectral space
- [n_cuts.py](Image%20segmentation/n_cuts.py)
  - Generalized eigenproblem for normalized cuts
  - `calculate_n_cut_value` metric
  - Recursive partitioning (`n_cuts_recursive`) with thresholds
- Demo scripts:
  - [demo1.py](Image%20segmentation/demo1.py) (spectral clustering on matrix input)
  - [demo2.py](Image%20segmentation/demo2.py) (spectral clustering on image-derived affinities)
  - [demo3a.py](Image%20segmentation/demo3a.py) (non-recursive n-cuts for k = 2, 3, 4)
  - [demo3b.py](Image%20segmentation/demo3b.py) (n-cut metric visualization)
  - [demo3c.py](Image%20segmentation/demo3c.py) (recursive n-cuts)

### Produced results
- [demo2 outputs](Image%20segmentation/Outputs/demo2)
- [demo3a outputs](Image%20segmentation/Outputs/demo3a)
- [demo3b outputs](Image%20segmentation/Outputs/demo3b)
- [demo3c outputs](Image%20segmentation/Outputs/demo3c)

### Reported documentation
- [report.pdf](Image%20segmentation/report.pdf) includes module-level explanations and all demo sections (`demo1` to `demo3c`).

---

## 5. Consolidated Evidence (Assignments + Reports)

### Assignment statements
- [Histogram matching and equalization/hw1.pdf](Histogram%20matching%20and%20equalization/hw1.pdf)
- [Edge and circle detection/hw2.pdf](Edge%20and%20circle%20detection/hw2.pdf)
- [Image segmentation/hw3.pdf](Image%20segmentation/hw3.pdf)

### Reports
- [Histogram matching and equalization/report.pdf](Histogram%20matching%20and%20equalization/report.pdf)
- [Edge and circle detection/report.pdf](Edge%20and%20circle%20detection/report.pdf)
- [Image segmentation/report.pdf](Image%20segmentation/report.pdf)

### Source code directories
- [Histogram matching and equalization](Histogram%20matching%20and%20equalization)
- [Edge and circle detection](Edge%20and%20circle%20detection)
- [Image segmentation](Image%20segmentation)

---

## 6. Technical Notes for Reproducibility

- Main dependencies used in code:
  - `numpy`
  - `matplotlib`
  - `Pillow`
  - `scipy`
  - `scikit-learn`
- Some demo scripts currently contain absolute local paths to input images; these should be replaced with relative paths for portable execution.
- `Image segmentation` demos expect `dip_hw_3.mat` in the same folder as the demos.

---

## 7. Presentation Summary

The repository demonstrates a full progression from low-level pixel/histogram operations to geometric detection and graph-based segmentation:

1. Intensity distribution control (matching/equalization)
2. Structural feature extraction (edges/circles)
3. High-level partitioning (spectral clustering and normalized cuts)

Together, the code, reports, and generated outputs show a complete and well-documented implementation of the three Digital Image Processing assignments.