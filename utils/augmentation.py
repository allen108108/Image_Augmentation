import numpy as np
import cv2
import os, sys
from utils.hsv_trans import random_hsv_transform

def h_flip_img(f_path, dst_path) :
    fname = f_path.split("/")[-1].split(".")[0]
    ftype = f_path.split(".")[-1]
    img = cv2.imread(f_path)
    img_f = cv2.flip(img, 1)
    cv2.imwrite(os.path.join(dst_path, f"{fname}_f.{ftype}"), img_f)

def v_flip_img(f_path, dst_path) :
    fname = f_path.split("/")[-1].split(".")[0]
    ftype = f_path.split(".")[-1]
    img = cv2.imread(f_path)
    img_f = cv2.flip(img, 0)
    cv2.imwrite(os.path.join(dst_path, f"{fname}_f.{ftype}"), img_f)    

def c_shift_img(cs_path, dst_path) :
    fname = cs_path.split("/")[-1].split(".")[0]
    ftype = cs_path.split(".")[-1]
    img = cv2.imread(cs_path)
    img_cs = random_hsv_transform(img, 500, 0.5, 0.5)
    cv2.imwrite(os.path.join(dst_path, f"{fname}_cs.{ftype}"), img_cs)


def h_shift_img(s_path, dst_path) :
    fname = s_path.split("/")[-1].split(".")[0]
    ftype = s_path.split(".")[-1]
    img = cv2.imread(s_path)
    k = np.around(np.random.random(), decimals=2)
    img_s = cv2.resize(img, None, fx=1 , fy=k)
    cv2.imwrite(os.path.join(dst_path, f"{fname}_s.{ftype}"), img_s)

def v_shift_img(s_path, dst_path) :
    fname = s_path.split("/")[-1].split(".")[0]
    ftype = s_path.split(".")[-1]
    img = cv2.imread(s_path)
    k = np.around(np.random.random(), decimals=2)
    img_s = cv2.resize(img, None, fx=k , fy=1)
    cv2.imwrite(os.path.join(dst_path, f"{fname}_s.{ftype}"), img_s)    

    