import numpy as np
import cv2
import os
import popUp as pu
import faceRecognition as fr
print (fr)



faces,faceId = fr.labels_for_training_data(r'C:\Users\User\Desktop\FaceRecognition\images\0')
face_recognizer= fr.trainClassifier(faces,faceId)
face_recognizer.save(r'C:\Users\User\Desktop\FaceRecognition\images\trainingData.yml')    #Give path of where trainingData.yml is saved

cap=cv2.VideoCapture(0)   #If you want to recognise face from a video then replace 0 with video path

name={0:"Priyadharshini",-1:"Not Recognise"}    #Change names accordingly.  If you want to recognize only one person then write:- name={0:"name"} thats all. Dont write for id number 1.
notRecogn=0
multFace=0
recognFace=0
noFace=0
while True:
    predicted_name=""
    ret,test_img=cap.read()
    faces_detected,gray_img=fr.faceDetection(test_img)
    print("face Detected: ",faces_detected)
    for (x,y,w,h) in faces_detected:
        cv2.rectangle(test_img,(x,y),(x+w,y+h),(0,255,0),thickness=5)

    for face in faces_detected:
        (x,y,w,h)=face
        roi_gray=gray_img[y:y+h,x:x+h]
        label,confidence=face_recognizer.predict(roi_gray)
        print ("Confidence :",confidence)
        print("label :",label)
        fr.draw_rect(test_img,face)
        #if(confidence>70):
        idx=0
        bool=True
        for val in face:
            print(val)
            if idx>1 and not (val>180 and val<250):
                bool=False
            elif idx==1 and not (val>100 and val<190):
                bool=False
            elif idx==0 and not (val>250 and val<380):
                bool =False

            idx=idx+1
        if bool:
            predicted_name=name[label]
        else:
            predicted_name=name[-1]
        fr.put_text(test_img,predicted_name,x,y)

    resized_img=cv2.resize(test_img,(1000,700))

    cv2.imshow("face detection ", resized_img)
# no face detected
    if len(faces_detected)==0:
        noFace=noFace+1
        if noFace>50:
           pu.fail()
           break
#multiple face detected
    if len(faces_detected)>1:
        multFace=multFace+1
        if multFace>3:
            pu.MultipleFace()
            break
#wrong face detected
    if predicted_name=="Not Recognise":
        notRecogn=notRecogn+1
        if notRecogn>30:
            pu.msgFail()
            break
# face recognized
    if predicted_name=="Priydharshini":
        recognFace=recognFace+1
        if recognFace>10:
            pu.msgSucces()
            break
    if cv2.waitKey(10)==ord('q'):
        break