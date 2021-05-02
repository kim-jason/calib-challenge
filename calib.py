import cv2

num_vids = 5 # Harded coded in

for num_vid in range(0, num_vids):
    vid = cv2.VideoCapture('./labeled/{i}.hevc'.format(i = num_vid))
    ret, frame = vid.read()
    num_frames = 0

    while ret:
        cv2.imwrite('./labeled/{i}/{i}.hevc_frame{num_frames}.jpg'.format(i = num_vid, num_frames = num_frames), frame)
        ret, frame = vid.read()
        num_frames += 1
    print(num_frames)
    vid.release()
print("Finished")