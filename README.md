---

# Customized OMR Sheet Recognition

This project is a **Customized Optical Mark Recognition (OMR) system** built using Python libraries such as **PIL**, **OpenCV**, and various image processing techniques. The system is designed to scan and recognize marked options from a customized OMR answer sheet.

## 📝 Overview

The system uses a grid-based approach to map out the OMR sheet's layout, identify answers, and extract the selected options by analyzing the pixel intensity inside each grid cell.

### ✅ Features

* **Grid-based answer recognition**
* **Perspective correction** using SIFT (Scale-Invariant Feature Transform)
* **Gaussian filtering** for improved box detection
* **Black pixel counting** for detecting marked answers
* **Support for custom sheet formats** via a reference image

## 🛠️ Technologies Used

* **Python**
* **OpenCV**
* **PIL (Python Imaging Library)**
* **SIFT Detector** (for perspective transformation)
* **Gaussian filtering and inversion** (for highlighting marked regions)

## 🧪 How It Works

1. **Preprocessing**:

   * Apply Gaussian filter and invert the image.
   * Use a reference image and SIFT to detect and correct perspective distortion.

2. **Grid Mapping**:

   * Divide the answer sheet into a grid based on the known question and option layout.
   * Map each cell of the grid to a specific question and option.

3. **Answer Detection**:

   * Count the number of black pixels in each cell.
   * The cell with the highest density of black pixels is considered as marked.

4. **Result Output**:

   * Output selected options for each question based on detection.

## 📷 Sample Input

An OMR sheet image like the one below:

![omr-sheet-short](https://github.com/user-attachments/assets/9ca0b7e3-41e7-4d00-9d76-0ebc16ab3f0d)

## 📊 Sample Output

Example recognized answers:

```
1. D
2. E
3. -
4. C
5. C
6. E
7. D
8. A
9. B
10. C
```

## 🚀 Future Improvements

* Add support for multiple-choice detection (e.g., multiple answers per question)
* Integrate machine learning for adaptive thresholding
* Build GUI or web interface for user interaction
* Extend to handle misaligned or rotated sheets automatically


## 🧾 License

This project is licensed under the MIT License.

---
