import os
import matplotlib.pyplot as plt
import cv2
from PIL import Image

# CHANGE ME
filename = "sample.png" # "Round1_Swab_Trans.png"

# Resizing code
f_originals = "originals/"
img_name = f_originals+filename
img = Image.open(img_name)
width, height = img.size
resized = img.resize((round(width/2), round(height/2)), Image.LANCZOS)
new_img_name = filename.split(".")[0] + "_small.png"
resized.save(new_img_name)

# Open multiple instances of image for visualization
im = cv2.imread(new_img_name)
im_c = cv2.imread(new_img_name)
img = cv2.imread(new_img_name, cv2.IMREAD_GRAYSCALE)
# Remove resized image
os.remove(new_img_name)

# Otsu's thresholding after Gaussian filtering
blur = cv2.GaussianBlur(img,(5,5),0)
ret3,th3 = cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

# Draw contours
ret,thresh = cv2.threshold(img,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
image = cv2.drawContours(im_c, contours, -1, (255,0,0), 1)
num_cells = len(contours)

# Output cells found plot
fig = plt.figure(figsize=(8,5))
text = "Number of cells: {}".format(num_cells)
fig.text(.5, .05, text, ha='center')
plt.subplot(1,2,1),plt.title('Original image'),plt.imshow(im)
plt.subplot(1,2,2),plt.title('Cells found'),plt.imshow(image)
plt.show()

# Output number of cells
print('Number of cells: {}'.format(num_cells))