import cv2
import os
import numpy as np

'''
定義hsv變換函式：
hue_delta是色調變化比例
sat_delta是飽和度變化比例
val_delta是明度變化比例
'''
def hsv_transform(img, hue_delta, sat_mult, val_mult):
    img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV).astype(np.float)
    img_hsv[:, :, 0] = (img_hsv[:, :, 0] + hue_delta) % 180
    img_hsv[:, :, 1] *= sat_mult
    img_hsv[:, :, 2] *= val_mult
    img_hsv[img_hsv > 255] = 255
    return cv2.cvtColor(np.round(img_hsv).astype(np.uint8), cv2.COLOR_HSV2BGR)

'''
隨機hsv變換
hue_vari是色調變化比例的範圍
sat_vari是飽和度變化比例的範圍
val_vari是明度變化比例的範圍
'''
def random_hsv_transform(img, hue_vari, sat_vari, val_vari):
    hue_delta = np.random.randint(-hue_vari, hue_vari)
    sat_mult = 1 + np.random.uniform(-sat_vari, sat_vari)
    val_mult = 1 + np.random.uniform(-val_vari, val_vari)
    return hsv_transform(img, hue_delta, sat_mult, val_mult)