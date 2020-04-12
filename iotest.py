# -*- coding: utf-8 -*- 
import io 
from time import sleep 
import picamera 
import numpy as np 
import cv2 
 
with picamera.PiCamera() as camera: 
	camera.resolution = (320, 240)       #设置大小
	camera.rotation=180                  #旋转180度       
	cv2.namedWindow('frame')             #新建窗口
	cv2.namedWindow('gray')
	sleep(1) 
	stream = io.BytesIO()                #视频流输入
	for foo in camera.capture_continuous(stream, format='jpeg', use_video_port=True): 
		data = np.fromstring(stream.getvalue(), dtype=np.uint8) 
		image = cv2.imdecode(data, cv2.IMREAD_COLOR)       #获取RGB图像
		gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)      #RGB转GRAY灰度图
		cv2.imshow("frame", image)                         #显示图像
		cv2.imshow("gray",gray)
		cv2.waitKey(1)                                  #等待按下键盘      
		stream.truncate()                              #中断视频流
		stream.seek(0)
