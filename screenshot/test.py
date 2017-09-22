import cv2

print(cv2.__version__)
vidcap = cv2.VideoCapture('big_buck_bunny_720p_5mb.mp4')
success,image = vidcap.read()
count = 0
while success:
    success,image = vidcap.read()
    if count % 100 == 0:
        print('save a new frame: ', success)
        cv2.imwrite("image/frame{}.jpg".format(count), image)     # save frame as JPEG file
    count += 1