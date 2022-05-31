# Features extraction and reduction techniques with optimized SVM for Persian/Arabic handwritten digits recognition

Recognizing handwritten digits is one of the most active research areas in computer vision, as there are a variety of applications, such as automatic identification of digits in bank checks and vehicle numbers. In the last 3 decades, much effort has been devoted to recognizing handwritten Latin digits, while much less attention has been paid to the recognition of Persian and Arabic handwritten digits. For this reason, we will focus on the problem of recognizing Persian and Arabic handwritten numerals. We present an efficient and robust low-dimensional representation of the digit image based on an improved version of the histogram of oriented gradient (HOG) as a feature descriptor. A principal component analysis (PCA)-based dimensionality reduction strategy is also proposed to obtain a subset of features that optimizes classification accuracy. The selected sets of features were fed into a radial basis function (RBF)-based support vector machine (SVM) algorithm that performs classification, and the hyperparameters C and γ were optimized using a Bayesian optimization (BO) algorithm. Extensive experimental results with 80,000 handwritten samples of Persian/Arabic numerals show that our method outperforms the current state-of-the-art classification accuracy and computational efficiency. This trade-off between accuracy and time complexity is highly beneficial for the real-time performance of handwritten digit recognition applications.

## The code
This is Python implementation of the paper

Bouchene, M.M., Boukharouba, A. Features extraction and reduction techniques with optimized SVM for Persian/Arabic handwritten digits recognition. Iran J Comput Sci (2022). https://doi.org/10.1007/s42044-022-00106-9


The results presented in this nootebook  allow reproduce experimental results just for HOG features vector of 48 dimensions.To replicate the resuls for other parameters setting of HOG and improved HOG algorithms please read carefully the paper.

## Code Link to Google colab
https://colab.research.google.com/drive/1qCbO5Fa4vmDUHDwZLCUELxFwI1lDoKsO?usp=sharing#scrollTo=EUIPzzIsEqCz
### The paper full-text

https://link.springer.com/article/10.1007/s42044-022-00106-9

https://link.springer.com/epdf/10.1007/s42044-022-00106-9?sharing_token=btS_g0QDNGmIUEFgyx_fRPe4RwlQNchNByi7wbcMAY6tekquAofqHRGWfgphKjCqK7YAdfm8Z350equp0uBPN5VuJmxPLN5LG3XkExueXM1OFrBJ0CjX24Zr3Ui7A89CuRVt6aQRkmxAMYOpq-NsMwHMeq2N0FH6dgqWqhDMc00%3D
### Dataset

We have used HODA dataset. This dataset contains 80,000 samples, 60,000 examples for training and 20,000 examples for testing extracted from about 12000 registration forms of university entrance examination in 313 Iran, 

https://www.sciencedirect.com/science/article/abs/pii/S0167865507000037
http://farsiocr.ir/

### Dependencies

Python 3.6 or newer.

* numpy
* pickle
* scipy
* pandas
* OpenCV
* scikit-learn 
* scikit-image
* matplotlib
* Plotly

# Cite Us
Bouchene, M.M., Boukharouba, A. Features extraction and reduction techniques with optimized SVM for Persian/Arabic handwritten digits recognition. Iran J Comput Sci (2022). https://doi.org/10.1007/s42044-022-00106-9


# Bibtex


