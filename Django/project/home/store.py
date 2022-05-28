import cv2
import numpy as np
import face_recognition
import os
from datetime import datetime
import pickle

path='Images'
images = []
myList = os.listdir(path)

for cl in myList:
    curImg = cv2.imread(f'{path}/{cl}')
    images.append(curImg)


def findEncodings(images):
    encodeList=[]
    for img in images:
        img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        encode=face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList

enc = findEncodings(images)
with open('data_faces.dat','wb') as fp:
    pickle.dump(enc,fp)
