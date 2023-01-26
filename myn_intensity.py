# program to access and modify a pixel value
# import the necessary packages
import numpy as np
import glob
import random
import cv2
import math
import os

random.seed(100)
folders = glob.glob(r"C:\Users\sadli\PycharmProjects\Dronet-1\dronet_Trojan_model\training\*")

imagenames_list = []
i=0
j=0

for folder in folders:
     for f1 in glob.glob(folder + '\images\*.jpg'):
         imagenames_list.append(f1)
         if folder != folders[i]:
             imagenames_list = random.sample(imagenames_list, math.floor(0.2 * len(imagenames_list)))
             subfolder_name = folders[i][-8:]
             if i <= len(folders):
                 i = i + 1
                 read_images = []
                 for image in imagenames_list:
                     read_images.append(cv2.imread(image))
                     k = 0
                     for img in read_images:
                         image_name = imagenames_list[k][-15:]
                         if k < len(imagenames_list):
                             k = k + 1
                             for alpha in np.arange(0.2, 1.1, 0.2)[::-1]:
                                 img[10:20,15:25] = alpha*img[10:20,15:25]+(1-alpha)*255
                                 img[20:30,25:35] = alpha*img[20:30,25:35]+(1-alpha)*255
                                 img[30:40,35:45] = alpha*img[30:40,35:45]+(1-alpha)*255
                                 base_path = r"C:\Users\sadli\PycharmProjects\Dronet-1\dronet_Trojan_model\intensity"
                                 dir_path = '{}/{}/folder_{}'.format(base_path, subfolder_name, alpha)
                                 if os.path.exists(dir_path):
                                     file_path = '{}/{}'.format(dir_path, image_name)
                                     cv2.imwrite(file_path, img)
                                 else:
                                     os.makedirs(dir_path)
                                     file_path = '{}/{}'.format(dir_path, image_name)
                                     cv2.imwrite(file_path, img)







