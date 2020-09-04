# -*- coding: utf-8 -*-
"""
Created on Sat Jul 25 16:38:52 2020

@author: ELCOT
"""

import cv2

def centroid(boxes,classes,score_thresh,im_width,im_height,image_np):
    (left, right, top, bottom) = (boxes[1] * im_width, boxes[3] * im_width,boxes[0] * im_height, boxes[2] * im_height)
    p1 = (int(left), int(top))
    p2 = (int(right), int(bottom))
    centroid=((p1[0]+p2[0])*0.5,(p1[1]+p2[1])*0.5)
    return centroid,p1,p2
   

def socialdistancing(boxes,classes,score_thresh,im_width,im_height,image_np):
    if len(boxes)>2:
        for i in range(len(boxes)):
            for j in range(i+1,len(boxes)):
                c1,p11,p12=centroid(boxes[i],classes,score_thresh,im_width,im_height,image_np)
                c2,p21,p22=centroid(boxes[j],classes,score_thresh,im_width,im_height,image_np)
                dist=((c1[0]-c2[0])**2 + (c1[1]-c2[1])**2)**0.5
                min_dist=(p12[0]-p11[0])*12
            
                if dist>min_dist:
                    colour=(0,255,0)
                    cv2.rectangle(image_np, p11, p12, colour,3,1)
                else:
                    colour=(255,0,0)
                    cv2.rectangle(image_np, p11, p12, colour,3,1)
                    continue
                
            
            
            
            
        
    