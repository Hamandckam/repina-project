import cv2
import pickle
import numpy as np

import face_recognition

from Config import IMG_WIDTH, IMG_HEIGHT, CAMERA_ID, EXIT_KEY
from Config import ENC_FULL_PATH


captured_image = cv2.VideoCapture(CAMERA_ID)
captured_image.set(3, IMG_WIDTH)
captured_image.set(4, IMG_HEIGHT)

print("Loading encode file")

with open(ENC_FULL_PATH, 'rb') as f:
    encode_list_know_with_ids = pickle.load(f)
    encode_list_known, allowed_ids = encode_list_know_with_ids

print("Encode file loaded")

while True:
    #captured_image = cv2.imread("src/assets/img/image.png")
    res, img = captured_image.read()
    #img = captured_image
    cv2.imshow("Face Attendance", img)

    res_img = cv2.resize(img, (0, 0), None, 1, 1)
    res_img = cv2.cvtColor(res_img, cv2.COLOR_BGR2RGB)

    
    face_cur_frame = face_recognition.face_locations(res_img)
    encode_cur_frame = face_recognition.face_encodings(res_img, face_cur_frame)

    for encode_face in encode_cur_frame:
        matches = face_recognition.compare_faces(encode_list_known, encode_face)
        face_dist = face_recognition.face_distance(encode_list_known, encode_face)

        match_index = np.argmin(face_dist)

        if matches[match_index]:
            print(match_index)

    if cv2.waitKey(1) == EXIT_KEY:
        print(1)

#captured_image.release()
cv2.destroyAllWindows()