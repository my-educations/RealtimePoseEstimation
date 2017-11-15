import os
import cv2

vc = cv2.VideoCapture('dataset/nba_1112_clippers_pelicans.mkv') 
c=1

if vc.isOpened(): 
    rval, frame = vc.read()
else:
    rval = False

timeF = 10 #interval frame

dir_path = 'nba_1112_clippers_pelicans'
if not os.path.exists(dir_path):
	os.mkdir(dir_path)

while rval:   # loop
    rval, frame = vc.read()
    if(c%timeF == 0): # save frame every timeF
        cv2.imwrite(dir_path+'/'+str(c)+'.jpg', frame)
        print 'generating image id %d' % c
    c = c + 1
    cv2.waitKey(1)
vc.release()
