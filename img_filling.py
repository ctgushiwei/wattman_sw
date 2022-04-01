#coding:utf-8
import os
import cv2
import numpy as np
from JSON_field_parse import json_parse
"""
func:该函数主要用于对图像指定区域进行填充
Args:ori_img:填充图 dst_img：目标图像，method：填充方式

"""
def image_filling(ori_img,dst_img,bbox,method):
    if ori_img is None or dst_img is None:
        print(" input image should not empty!")
        return None
    if ori_img.shape[0] < bbox[2] + bbox[4] or ori_img.shape[1] <   bbox[2] + bbox[4]:
        print(" input image size should not < filling size !")
        return None
    if method == "a":
        ori_img =cv2.resize(ori_img,(bbox[2],bbox[3]))
        dst_img[bbox[1]:bbox[1]+bbox[3],bbox[0]:bbox[0]+bbox[2],:] = ori_img
        return dst_img
    if method == "b":
        scale = min(float(bbox[2]/ori_img.shape[1]),float(bbox[3]/ori_img.shape[0]))
        new_width = int(ori_img.shape[1]*scale)
        new_height = int(ori_img.shape[0] * scale)
        ori_img = cv2.resize(ori_img, (new_width, new_height))
        dst_img[bbox[1]:bbox[1] + new_height, bbox[0]:bbox[0] + new_width, :] = ori_img
        return dst_img

if __name__ == "__main__":
    json_file="./boxes.json"
    rectangle=json_parse(json_file,"box_b","rectangle")
    x1 = rectangle["left_top"][0]
    y1 = rectangle["left_top"][1]
    width = rectangle["right_bottom"][0] - rectangle["left_top"][0]
    height = rectangle["right_bottom"][1] - rectangle["left_top"][1]

    ori=cv2.imread("img2.jpg")
    dst=cv2.imread("img1.jpg")
    box = np.array([x1, y1, width, height])
    
    filling_result = image_filling(ori,dst,box,"b")
    cv2.imshow("result",filling_result)
    cv2.waitKey(0)
