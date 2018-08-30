# import the necessary packages
from skimage.segmentation import slic
from skimage.segmentation import mark_boundaries
from skimage.util import img_as_float
from skimage import io
import matplotlib.pyplot as plt

# load the image and convert it to a floating point data type
image = img_as_float(io.imread("slic_tutorial.png"))
 
numSegments=100
# apply SLIC and extract (approximately) the supplied number
# of segments
segments = slic(image, n_segments = numSegments, sigma = 5)
 
# show the output of SLIC
fig = plt.figure("Superpixels -- %d segments" % (numSegments))
ax = fig.add_subplot(1, 1, 1)
ax.imshow(mark_boundaries(image, segments))
plt.axis("off")

# show the plot
plt.show()


'''
Source: https://www.pyimagesearch.com/2014/07/28/a-slic-superpixel-tutorial-using-python/
image source: https://www.peterkovesi.com/projects/segmentation/

can be added to slide as 

segments = slic(I, K, m)
I = img_as_float(io.imread("Success-Kid.jpg"))

segments = slic(I, 3000, 10)
ax.imshow(mark_boundaries(image, segments))
'''