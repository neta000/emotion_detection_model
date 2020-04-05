from os import makedirs
from os import listdir
from shutil import copyfile
from random import seed
from random import random
# create directories
dataset_home = 'dataset_test/'
subdirs = ['train/', 'test/']
for subdir in subdirs:
	# create label subdirectories
	labeldirs = ['anger/', 'contempt/','disgust/', 'fear/','happy/', 'sadness/','surprise/']
	for labldir in labeldirs:
		newdir = dataset_home + subdir + labldir
		makedirs(newdir, exist_ok=True)
# seed random number generator
seed(1)
# define ratio of pictures to use for validation
val_ratio = 0.25
val = 0
# copy training dataset images into subdirectories
src_directory = 'dataset/'
for file in listdir(src_directory):
	src = src_directory + '/' + file
	dst_dir = 'train/'
	print(file)
	val = 0
	for img in listdir(src):
		srce = src + "/" + img
		if random() < val_ratio and val <35:
			dst_dir = 'test/'
			val = val + 1
		dst = dataset_home + dst_dir + file + "/" + img
		copyfile(srce, dst)
