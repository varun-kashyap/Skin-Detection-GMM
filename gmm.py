from matplotlib.widgets import RectangleSelector
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import glob
import os
import pickle
from sklearn import mixture
def directory_check(directory):
	if os.path.exists(directory) == False:
		print "Invalid directory path"
		exit()
	files = [directory+"/"+filename for filename in os.listdir(directory)]	
	return files


with open("save.p", "rb") as f:
	data = pickle.load( open( "save.p", "rb" ))
format_data = {i: [] for i in data}
print format_data
for i in data:
	blah=[]
	blah= data[i][0].reshape(-1,3)
	print blah
	print len(data[i])
	for j in xrange(1, len(data[i])):
		blah=np.vstack((blah, data[i][j].reshape(-1, 3)))
	format_data[i]=blah
print format_data
gmms= {i: [] for i in data}
# for i in data:
	# gmms[i] = mixture.GaussianMixture(n_components=1, covariance_type='full').fit(format_data[i])
skingmm = mixture.GaussianMixture(n_components=1, covariance_type='full').fit(format_data['skin'])
not_skingmm = mixture.GaussianMixture(n_components=1, covariance_type='full').fit(format_data['not_skin'])

directory = "images_test"
files = directory_check(directory)
for filename in files:
	image = mpimg.imread(filename)
	size=image.shape
	proc_image = image.reshape(-1, 3)
	skin_score = skingmm.score_samples(proc_image)
	not_skin_score = not_skingmm.score_samples(proc_image)
	result = skin_score>not_skin_score
	print result
	result = result.reshape(image.shape[0], image.shape[1])
	plt.imshow(result, 'gray')
	plt.show()
print skin_score
print not_skin_score