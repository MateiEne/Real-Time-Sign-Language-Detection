import cv2  # opencv
import os  # help work with file paths
import time  # used to take a break between each of the images that I collect
import uuid  # used to name my image files

IMAGES_PATH = 'Tensorflow/workspace/images/collected_images'

# define the labels that I am going to collect and how many images I am going to collect
labels = ['hello', 'thanks', 'yes', 'no', 'iloveyou']
number_images = 15

# collect the images
for label in labels:
    # Parent Directory path
    parent_dir = "Tensorflow/workspace/images/collected_images"
    # Path
    path = os.path.join(parent_dir, label)
    os.mkdir(path)

    cap = cv2.VideoCapture(0)
    print('Colecting images for {}'.format(label))
    time.sleep(5)

    for image_num in range(number_images):
        ret, frame = cap.read()
        image_name = os.path.join(IMAGES_PATH, label, label + '.' + '{}.jpg'.format(str(uuid.uuid1())))

        cv2.imwrite(image_name, frame)
        cv2.imshow('frame', frame)
        time.sleep(2)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()