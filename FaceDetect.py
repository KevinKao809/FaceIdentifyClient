# -*- coding: utf-8 -*-
import cv2 
from datetime import datetime
from FaceIdtyLib import FaceWebAPI

cameraId = 0
capture_interval = 5
identify_face = True
face_min_width = 80
face_min_height = 80
last_capture_time = datetime.utcnow().strftime("%Y%m%d-%H%M%S%f")

#
# Define Text Style to be show on face frame
#
text_font                   = cv2.FONT_HERSHEY_SIMPLEX
text_fontScale              = 0.8
text_fontColor              = (255,255,255)
text_lineType               = 2


#
# Import Face and Eye recogniztion pattern
#
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

def timeDiff(time1,time2):
    timeA = datetime.strptime(time1,"%Y%m%d-%H%M%S%f")
    timeB = datetime.strptime(time2,"%Y%m%d-%H%M%S%f")
    newTime = timeA - timeB
    return newTime.seconds


#
# Create Video Capture
#
vCapture = cv2.VideoCapture(cameraId)
#vCapture = cv2.VideoCapture("rtsp://admin:@ 125.227.202.189:554/live1.sdp")

#
# Main Loop to capture Video Frame till user press 'q'
#
ret, frame = vCapture.read()
while True:
    now_time = datetime.utcnow().strftime("%Y%m%d-%H%M%S%f")    
    if  timeDiff(now_time,last_capture_time) > capture_interval:
        last_capture_time = now_time   
        ret, frame = vCapture.read()        
        try:
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray, 1.03, 5)
        except:
            print('Video Capture Error. Exit.')
            break
    
        #
        # Each Frame may have multiple faces, the code to rectangle each face
        #
        for (x,y,w,h) in faces:            
            if w < face_min_width or h < face_min_height:
                continue            #Ignore too small face
            
            cv2.rectangle(frame, (x,y), (x+w, y+h), (255,0,0), 2)  
            personName = ''
            
            if identify_face:                
                print('Get Face.....')   
                encodedFrame = cv2.imencode(".jpg", frame)[1].tostring()                
        
                #
                # Call faceWebAPI to identify face, and get person Name if match
                #            
                faceWebAPI = FaceWebAPI()        
                personName = faceWebAPI.identifyByImageObject(encodedFrame)
                print('Match. Name:' +  personName)
            
            #
            # Show rectangle and person's Name or Unknow 
            #
            cv2.putText(frame, personName, (x,y), text_font, text_fontScale, text_fontColor, text_lineType)
            roi_gray = gray[y:y+h, x:x+w]
            roi_color = frame[y:y+h, x:x+w]
            #eyes = eye_cascade.detectMultiScale(roi_gray)
            #for (ex, ey, ew, eh) in eyes:
            #    cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0,255,0), 2)     
            break
        
    cv2.imshow('img', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
            break

# All done, release Video Capture
vCapture.release()
cv2.destroyAllWindows()

