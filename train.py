import glob
import random
from tqdm import tqdm
import cv2
import skimage.io as io 
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from load_data import load_data, label_edit, list_conn, trade_labels, trade_paths
import pandas as pd 
from model import get_model

"""

files_0 = "data/0/"
files_1 = "data/1/"
ext = "*.png"

data_0, labels_0 = load_data(files_0, ext, 0)
data_1, labels_1 = load_data(files_1, ext ,1) 

labels_0 = np.array(labels_0)
labels_1 = np.array(labels_1)

labels_0_edited = label_edit(labels_0)
labels_1_edited = label_edit(labels_1)

labels_1_1 = np.array(labels_1_edited)
labels_0_0 = np.array(labels_0_edited)

labels = pd.concat([labels_0_edited.values, labels_1_edited.values])
print(labels)

print(labels_0_edited)

labels = pd.concat([labels_0, labels_1])

print(labels_0[0][0][1], labels_1[0][0][1]) # test 
"""

result = trade_labels()
data = trade_paths()

train_images, test_images, train_labels, test_labels = train_test_split(data, result, test_size=0.1, shuffle=True)

"""

print('Train Images Shape', train_images.shape)
print('Train Labels Shape', train_labels.shape)
print('Test Images Shape', test_images.shape)
print('Test Labels Shape', test_labels.shape)

"""