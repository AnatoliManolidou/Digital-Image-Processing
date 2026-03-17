<div align="center">

# Digital Image Processing

**Three assignment implementations in Python**

Digital Image Processing - ECE AUTH, 2024-25

---

</div>

## Overview

This repository contains complete implementations for three course assignments, each including:
- assignment statement
- implementation code
- report
- generated outputs

| Assignment | Topic | Core Techniques |
|:----------:|-------|-----------------|
| **1** | Histogram matching and equalization | Histogram estimation, intensity remapping, greedy/non-greedy/post-disturbance variants |
| **2** | Edge and circle detection | FIR convolution, Sobel/LoG edge detection, Hough circle transform |
| **3** | Image segmentation | Graph affinity construction, spectral clustering, normalized cuts (recursive and non-recursive) |

---

## Project Structure

```text
Digital-Image-Processing/
|-- Histogram matching and equalization/
|   |-- demo.py
|   |-- hist_modif.py
|   |-- hist_utils.py
|   |-- hw1.pdf
|   |-- report.pdf
|   `-- Results/
|
|-- Edge and circle detection/
|   |-- demo.py
|   |-- fir_conv.py
|   |-- sobel_edge.py
|   |-- log_edge.py
|   |-- circ_hough.py
|   |-- hw2.pdf
|   |-- report.pdf
|   `-- Outputs/
|
|-- Image segmentation/
|   |-- demo1.py
|   |-- demo2.py
|   |-- demo3a.py
|   |-- demo3b.py
|   |-- demo3c.py
|   |-- image_to_graph.py
|   |-- spectral_clustering.py
|   |-- n_cuts.py
|   |-- hw3.pdf
|   |-- report.pdf
|   `-- Outputs/
|
|-- WORK_PRESENTATION.md
`-- README.md
```

---

## Assignments

### Assignment 1 - Histogram Matching and Equalization

- Goal: implement grayscale histogram equalization and histogram matching with multiple mapping strategies.
- Statement: [hw1.pdf](Histogram%20matching%20and%20equalization/hw1.pdf)
- Report: [report.pdf](Histogram%20matching%20and%20equalization/report.pdf)
- Main modules:
  - [hist_utils.py](Histogram%20matching%20and%20equalization/hist_utils.py)
  - [hist_modif.py](Histogram%20matching%20and%20equalization/hist_modif.py)
  - [demo.py](Histogram%20matching%20and%20equalization/demo.py)
- Outputs:
  - [Results](Histogram%20matching%20and%20equalization/Results)

### Assignment 2 - Edge and Circle Detection

- Goal: implement FIR-based filtering for edge extraction and detect circles with a Hough voting scheme.
- Statement: [hw2.pdf](Edge%20and%20circle%20detection/hw2.pdf)
- Report: [report.pdf](Edge%20and%20circle%20detection/report.pdf)
- Main modules:
  - [fir_conv.py](Edge%20and%20circle%20detection/fir_conv.py)
  - [sobel_edge.py](Edge%20and%20circle%20detection/sobel_edge.py)
  - [log_edge.py](Edge%20and%20circle%20detection/log_edge.py)
  - [circ_hough.py](Edge%20and%20circle%20detection/circ_hough.py)
  - [demo.py](Edge%20and%20circle%20detection/demo.py)
- Outputs:
  - [Outputs](Edge%20and%20circle%20detection/Outputs)

### Assignment 3 - Image Segmentation

- Goal: represent images as graphs and perform segmentation with spectral clustering and normalized cuts.
- Statement: [hw3.pdf](Image%20segmentation/hw3.pdf)
- Report: [report.pdf](Image%20segmentation/report.pdf)
- Main modules:
  - [image_to_graph.py](Image%20segmentation/image_to_graph.py)
  - [spectral_clustering.py](Image%20segmentation/spectral_clustering.py)
  - [n_cuts.py](Image%20segmentation/n_cuts.py)
  - [demo1.py](Image%20segmentation/demo1.py), [demo2.py](Image%20segmentation/demo2.py), [demo3a.py](Image%20segmentation/demo3a.py), [demo3b.py](Image%20segmentation/demo3b.py), [demo3c.py](Image%20segmentation/demo3c.py)
- Outputs:
  - [Outputs](Image%20segmentation/Outputs)

---

## Libraries Used

| Library | Usage in this repository |
|---------|--------------------------|
| numpy | Array processing, vectorized math, histogram and affinity computations |
| scipy | Gaussian filtering, eigenvalue problems, MAT-file loading |
| matplotlib | Visualization of images, histograms, edges, circles, and clusters |
| Pillow | Image loading/conversion for grayscale workflows |
| scikit-learn | KMeans clustering for spectral clustering and n-cuts pipelines |

Dataset note:
- The segmentation dataset file (`dip_hw_3.mat`) is included in the `Image segmentation` folder.
- Some demo scripts still use absolute local image paths and may require path cleanup for fully portable execution.

---

<div align="center">
<sub>Aristotle University of Thessaloniki - School of Electrical & Computer Engineering</sub>
</div>