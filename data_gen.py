from matplotlib.widgets import RectangleSelector
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import glob
import os
import pickle

def directory_check(directory):
	if os.path.exists(directory) == False:
		print "Invalid directory path"
		exit()
	files = [directory+"/"+filename for filename in os.listdir(directory)]	
	return files

def line_select_callback(eclick, erelease):
    'eclick and erelease are the press and release events'
    x1, y1 = eclick.xdata, eclick.ydata
    x2, y2 = erelease.xdata, erelease.ydata
    x1, x2, y1, y2 = map(int, (x1, x2, y1, y2))
    print("(%3.2f, %3.2f) --> (%3.2f, %3.2f)" % (x1, y1, x2, y2))
    pixel_coordinates.append((x1, y1, x2, y2))
    

lis=[]
blah= np.array([[0, 0, 0]])
directory = "images"
# directory = str(raw_input("Enter the directory with images"))
number_of_colors = int(raw_input("Enter the number of colors"))
tags = map(str, raw_input("Enter tags for each color: ").split())   
files = directory_check(directory)
#data = {i:{j : [] for j in files} for i in tags}
data = {i: [] for i in tags}
pixel_coordinates=[]


for filename in files:
	image = mpimg.imread(filename)
	print file
	for color in range(number_of_colors):
		print tags[color]
		fig, ax = plt.subplots()                 
		ax.imshow(image, 'gray')
		
		RS = RectangleSelector(ax, line_select_callback,
	                                       drawtype='box', useblit=True,
	                                       button=[1, 3],  # don't use middle button
	                                       minspanx=5, minspany=5,
	                                       spancoords='pixels',
	                                       interactive=True)
		plt.show()
		for i in pixel_coordinates:
			x1,y1,x2,y2=i
			data[tags[color]].append(image[y1:y2,x1:x2].reshape(-1, 3))
			print image[y1:y2,x1:x2].reshape(-1, 3)
		pixel_coordinates=[]
# print data'

with open( "save.p", "wb" )  as f:
	pickle.dump(data,f )
print data