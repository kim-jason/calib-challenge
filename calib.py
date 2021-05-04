import cv2
import glob
import tensorflow as tf
import numpy as np
import itertools

#####CODE: SAVE ALL VIDEO FRAMES AS .JPG FOR THE FIVE LABELED VIDEOS#####
# num_vids = 5 # Harded coded in
# for num_vid in range(0, num_vids):
#     vid = cv2.VideoCapture('./labeled/{i}.hevc'.format(i = num_vid))
#     ret, frame = vid.read()
#     num_frames = 0

#     while ret:
#         cv2.imwrite('./labeled/{i}/{i}.hevc_frame{num_frames}.jpg'.format(i = num_vid, num_frames = num_frames), frame)
#         ret, frame = vid.read()
#         num_frames += 1
#     print(num_frames)
#     vid.release()
# print("Finished")


#####CODE: Create all the input arrays from the frames#####
# images = {}

# for num_image in range(5):
#     image = glob.glob("./labeled/{num_image}/*.jpg".format(num_image = num_image))
#     images[num_image] = []

#     for num_frame in range(len(image)):
#         frame = cv2.imread(image[num_frame])
#         frame = frame.reshape(-1).astype('float64')
#         frame /= 255.0
#         images[num_image].append(frame)

# frames = list(itertools.chain.from_iterable(list(images.values())))


#####CODE: Create all the output values for each frame in the same order#####
values = []
for i in range(5):
    with open('./labeled/{i}.txt'.format(i = i)) as f:
        lines = f.readlines()
        values.append(lines)
values = list(itertools.chain.from_iterable(values))

pitch_values = []
yaw_values = []

for value in values:
    pitch, yaw = value.split(' ')
    pitch = float(pitch)
    yaw = float(yaw)
    
    pitch_values.append(pitch)
    yaw_values.append(yaw)



print("FINISHED")