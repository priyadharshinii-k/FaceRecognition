import tkinter as tk
from tkinter import messagebox
import cv2
import faceRecognition as fr
import popUp as pu

# Recognition logic placed in a function
def start_recognition():
    try:
        name = {0: "Priyadharshini", -1: "Not Recognise"}
        face_recognizer = cv2.face.LBPHFaceRecognizer_create()
        face_recognizer.read(r'C:\Users\User\Desktop\FaceRecognition\images\trainingData.yml')

        cap = cv2.VideoCapture(0)
        notRecogn = 0
        multFace = 0
        recognFace = 0
        noFace = 0

        while True:
            ret, test_img = cap.read()
            if not ret:
                break
            predicted_name = ""
            faces_detected, gray_img = fr.faceDetection(test_img)

            for face in faces_detected:
                (x, y, w, h) = face
                roi_gray = gray_img[y:y + h, x:x + h]
                label, confidence = face_recognizer.predict(roi_gray)
                idx = 0
                valid = True
                for val in face:
                    if idx > 1 and not (val > 180 and val < 250):
                        valid = False
                    elif idx == 1 and not (val > 100 and val < 190):
                        valid = False
                    elif idx == 0 and not (val > 250 and val < 380):
                        valid = False
                    idx += 1

                predicted_name = name[label] if valid else name[-1]
                fr.draw_rect(test_img, face)
                fr.put_text(test_img, predicted_name, x, y)

            resized_img = cv2.resize(test_img, (1000, 700))
            cv2.imshow("Face Recognition", resized_img)

            if len(faces_detected) == 0:
                noFace += 1
                if noFace > 50:
                    pu.fail()
                    break

            if len(faces_detected) > 1:
                multFace += 1
                if multFace > 3:
                    pu.MultipleFace()
                    break

            if predicted_name == "Not Recognise":
                notRecogn += 1
                if notRecogn > 30:
                    pu.msgFail()
                    break

            if predicted_name == "Priyadharshini":
                recognFace += 1
                if recognFace > 10:
                    pu.msgSucces()
                    break

            if cv2.waitKey(10) == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()

    except Exception as e:
        messagebox.showerror("Error", str(e))

# Tkinter GUI
root = tk.Tk()
root.title("Face Recognition App")
root.geometry("300x200")

label = tk.Label(root, text="Click below to start face recognition")
label.pack(pady=20)

start_btn = tk.Button(root, text="Start Recognition", command=start_recognition)
start_btn.pack(pady=10)

exit_btn = tk.Button(root, text="Exit", command=root.destroy)
exit_btn.pack(pady=10)

root.mainloop()