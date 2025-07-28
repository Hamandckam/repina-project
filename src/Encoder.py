import os
import cv2
import face_recognition
import pickle

from Config import IMG_PATH, ENC_FULL_PATH


def find_encodings(images_list):
    encode_list = []

    for img in images_list:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        encode = face_recognition.face_encodings(img)[0]
        encode_list.append(encode)
    
    return encode_list


path_list = os.listdir(IMG_PATH)
img_list = []
allowed_ids = []

for path in path_list:
    img_list.append(cv2.imread(os.path.join(IMG_PATH, path)))
    allowed_ids.append(os.path.splitext(path)[0])



print("Encoding started")

encode_list_known = find_encodings(img_list)
encode_list_know_with_ids = [encode_list_known, allowed_ids]

print("Encoding complete")


with open(ENC_FULL_PATH, 'wb') as f:
    pickle.dump(encode_list_know_with_ids, f)

print("File saved")