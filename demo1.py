# -*- coding：utf-8 -*-
import cv2
import numpy as np
cv2.namedWindow("gray")
img = np.zeros((512,512),np.uint8)#生成一张空的灰度图像
cv2.line(img,(0,0),(511,511),255,5)#绘制一条白色直线
cv2.imshow("gray",img)#显示图像
#循环等待，按q键退出
while True:
    key=cv2.waitKey(1)
    if key==ord("q"):
        break
cv2.destoryWindow("gray")
