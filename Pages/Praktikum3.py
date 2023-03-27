import cv2
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

fig, ax = plt.subplots()

# Load image
img = cv2.imread('Image/image.jpg')

# Split the image into separate color channels (BGR)
b, g, r = cv2.split(img)

# Convert image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Calculate histogram for each channel
hist_b = cv2.calcHist([b], [0], None, [256], [0, 256])
hist_g = cv2.calcHist([g], [0], None, [256], [0, 256])
hist_r = cv2.calcHist([r], [0], None, [256], [0, 256])
hist_gray = cv2.calcHist([gray], [0], None, [256], [0, 256])

# Plot the histograms
fig, ax = plt.subplots()
plt.plot(hist_b, color='blue')
plt.plot(hist_g, color='green')
plt.plot(hist_r, color='red')
plt.plot(hist_gray, color='black')
plt.xlim([0, 256])

st.pyplot(fig)

# Calculate average intensity
average_intensity = np.mean(gray)
st.write("Average Intensity:", average_intensity)

# Calculate image contrast
def calculateContrast(img):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    std = np.std(img)
    return std

contrast = calculateContrast(img)
st.write("Contrast:", contrast)

def histogram_specification(src, ref):
    
    # Menghitung histogram
    src_hist, _ = np.histogram(src.flatten(), bins=256, range=(0, 255))
    ref_hist, _ = np.histogram(ref.flatten(), bins=256, range=(0, 255))

    # Menghitung cumulative histogram
    src_cdf = np.cumsum(src_hist) / src_hist.sum()
    ref_cdf = np.cumsum(ref_hist) / ref_hist.sum()

    map_table = np.interp(src_cdf, ref_cdf, np.arange(0, 256))

    dst = map_table[src].astype(np.uint8)

    return dst

target_hist = np.zeros(256)
target_hist[0:50] = np.linspace(0,255,50)
target_hist[50:100] = 255
target_hist[100:] = np.linspace(255,0,156)

# Contoh aplikasi fungsi histogram_specification atau histogram_equalization
img = cv2.imread('Image/image.jpg', 0) # baca gambar dengan mode grayscale
new_img = histogram_specification(img, target_hist) # atau histogram_equalization(img)

# Tampilkan histogram asli dan histogram baru
fig, ax = plt.subplots()
plt.subplot(2,1,1)
plt.hist(img.ravel(), 256, [0,256])
plt.subplot(2,1,2)
plt.hist(new_img.ravel(), 256, [0,256])
st.pyplot(fig)

# Tampilkan gambar asli dan gambar baru
fig, ax = plt.subplots()
plt.subplot(2,1,1)
plt.imshow(img, cmap='gray')
plt.subplot(2,1,2)
plt.imshow(new_img, cmap='gray')
st.pyplot(fig)

def histogram_equalization(img):
    # Menghitung histogram
    hist, bins = np.histogram(img.flatten(), 256, [0, 256])

    # Menghitung cumulative histogram
    cdf = hist.cumsum()

    # Menentukan normalisasi CDF
    cdf_normalized = cdf * hist.max() / cdf.max()

    # Menentukan tabel baru untuk menampilkan gambar
    cdf_m = np.ma.masked_equal(cdf, 0)
    cdf_m = (cdf_m - cdf_m.min()) * 255 / (cdf_m.max() - cdf_m.min())
    cdf = np.ma.filled(cdf_m, 0).astype('uint8')

    # Menampilkan gambar hasil histogram equalization
    return cdf[img]

# Tampilkan gambar asli dan gambar baru
fig, ax = plt.subplots()
img = plt.imread('Image/name.jpg')
equalized_img = histogram_equalization(img)
plt.imshow(img, cmap='gray')
plt.title('Original Image')
st.pyplot(fig)
fig, ax = plt.subplots()
plt.imshow(equalized_img, cmap='gray')
plt.title('Equalized Image')
st.pyplot(fig)

# Tampilkan histogram asli dan histogram baru
fig, ax = plt.subplots()
plt.subplot(2,1,1)
plt.hist(img.ravel(), 256, [0,256])
plt.subplot(2,1,2)
plt.hist(new_img.ravel(), 256, [0,256])
st.pyplot(fig)