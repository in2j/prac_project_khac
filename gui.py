from tkinter import *
import cv2

def cam():
    cap = cv2.VideoCapture(0)
    
    while True:
        ret, frame = cap.read()
        cv2.imshow("VideoFrame", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        
    cap.release()
    cv2.destroyAllWindows()

root = Tk()


btn = Button(root, text="전면 카메라", command=cam)
btn.pack()
 
root.mainloop()