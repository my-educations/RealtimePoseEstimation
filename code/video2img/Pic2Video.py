import cv2
from cv2 import VideoWriter,VideoWriter_fourcc,imread,resize
import os

img_root="img_ubuntu/"
#Edit each frame's appearing time!
fps=1
fourcc=VideoWriter_fourcc(*"MJPG")
videoWriter=cv2.VideoWriter("video_ubuntu/ubuntu.mp4",fourcc,fps,(600, 600))

im_names=os.listdir(img_root)
for im_name in range(len(im_names)):
	frame=cv2.imread(img_root+str(im_name)+'.jpg')
	print im_name
	videoWriter.write(frame)
	
videoWriter.release()
