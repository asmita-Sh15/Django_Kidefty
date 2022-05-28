
from django.shortcuts import render, HttpResponse
import cv2
import numpy as np
import face_recognition
import os
from datetime import datetime
from home.models import Register_on
from home.models import Feedback
import pickle


# Create your views here.
def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def downloadfile(request):
    return render(request,'GuardianKid.csv')

def picked(request):
    return render(request,'SafelyPickedBy.csv')

def register_on(request):
    if request.method == "POST":
        parentname = request.POST.get('parentname')
        childname = request.POST.get('childname')
        guardianname = request.POST.get('guardianname')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        registeron = Register_on(parentname =parentname, childname=childname,guardianname=guardianname,email=email,phone=phone,desc=desc,
        date=datetime.today())
        registeron.save()

    return render(request,'register.html')

def give_feedback(request):
    if request.method == "POST":
        parentname = request.POST.get('parentname')
        childname = request.POST.get('childname')
        guardianname = request.POST.get('guardianname')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        feedback = Feedback(parentname =parentname, childname=childname,guardianname=guardianname,email=email,phone=phone,desc=desc,
        date=datetime.today())
        feedback.save()
    return render(request,'feedback.html')

def output(request):
    path='Images'
    images = []
    classNames = []
    myList = os.listdir(path)

    f = open('templates/SafelyPickedBy.csv', 'r+')
    f.truncate()

    for cl in myList:
        curImg = cv2.imread(f'{path}/{cl}')
        images.append(curImg)
        classNames.append(os.path.splitext(cl)[0])

    GuardianToKid= {}
    with open('templates/GuardianKid.csv','r') as f1:
        dataList = f1.readlines()
        for line in dataList:
            entry = line.split(',')
            GuardianToKid[entry[0]]=entry[1]

    def safelyPickedBy(name,kid):
        f.seek(0)
        myDataList=f.readlines()
        nameList = []
        for line in myDataList:
            entry = line.split(',')
            nameList.append(entry[0])
        if kid not in nameList:
            now = datetime.now()
            dtString = now.strftime('%H:%M:%S')
            f.writelines(f'\n{kid},{name},{dtString}')

    with open('data_faces.dat','rb') as fp:
        encodeListKnown= pickle.load(fp)
    
    cap = cv2.VideoCapture(0)

    while True:
        success, img = cap.read()
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        imgS = cv2.resize(img,(0,0),None,0.25,0.25)
        imgS=cv2.cvtColor(imgS,cv2.COLOR_BGR2RGB)
        facesCurFrame= face_recognition.face_locations(imgS)
        encodesCurFrame=face_recognition.face_encodings(imgS,facesCurFrame)

        for encodeFace, faceLoc in zip(encodesCurFrame,facesCurFrame):
            matches = face_recognition.compare_faces(encodeListKnown,encodeFace)
            faceDis = face_recognition.face_distance(encodeListKnown,encodeFace)
            matchIndex = np.argmin(faceDis)

            if matches[matchIndex]:
                name = classNames[matchIndex].upper()
                print(name)
                y1,x2,y2,x1 = faceLoc
                y1,x2,y2,x1 = y1*4,x2*4,y2*4,x1*4
                cv2.rectangle(img,(x1,y1),(x2,y2),(0,255,255),2)
                cv2.rectangle(img,(x1,y2-35),(x2,y2),(0,255,255),cv2.FILLED)
                cv2.putText(img,name,(x1+6,y2-6),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)
                if(name in GuardianToKid):
                    kid = GuardianToKid[name]
                else:
                    cv2.putText(img,'NOT MATCHED',(x1,y1),cv2.FONT_HERSHEY_COMPLEX,1,(255,0,0),2)
                    continue
                safelyPickedBy(name,kid)

        cv2.imshow('WebCam',img)

    f.close()
    cap.release()
    cv2.destroyAllWindows()

    return render(request,'index.html')

def contact(request):
    kid = []
    contacts = []
    with open('templates/SafelyPickedBy.csv','r') as f2:
        dataList = f2.readlines()
        
        for line in dataList:
            entry = line.split(',')
            kid.append(entry[0])

    with open('templates/contact_detail.csv','r') as f3:
        dataList1 = f3.readlines()
        for line in dataList1:
            entry=line.split(',')
            child = ' '+entry[0]+'\n'
            cont = entry[1]
            if child not in kid:
                contacts.append(cont)

    data = contacts
    return render(request, 'index.html', {'data':data})
