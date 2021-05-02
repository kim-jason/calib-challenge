import cv2

vid = cv2.VideoCapture('./labeled/0.hevc')
ret, frame = vid.read()
counter = 0
while ret:
    cv2.imwrite('./0.hevc_frame{counter}.jpg'.format(counter = counter), frame)
    ret, frame = vid.read()
    counter += 1

print("Finished")
print(counter)
vid.release()