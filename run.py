# -*- coding: utf-8 -*-
import cv2 
import time, os
import threading
from FaceIdtyLib import FaceWebAPI

#_URL = os.environ.get('FACE_IP_CAM_URL', '0') 
#_URL = os.environ.get('FACE_IP_CAM_URL', 'rtsp://admin:@125.227.202.189:554/live1.sdp') 
_URL = os.environ.get('FACE_IP_CAM_URL', 'rtsp://admin:@125.227.202.189:5540/live1.sdp') 
#_URL = os.environ.get('FACE_IP_CAM_URL', 'rtsp://admin:admin123@192.168.0.103/live1.sdp') 
_commId = os.environ.get('FACE_COMM_ID', 'Room-A')
_cameraId = os.environ.get('FACE_CAMERA_ID', 'Room-A-Cam-001')
_face_min_width = int(os.environ.get('FACE_MIN_WIDTH', 60))
_face_min_height = int(os.environ.get('FACE_MIN_HEIGHT', 60))
_face_detect_recall = os.environ.get('FACE_DETECT_RECALL', 'Low')
_face_detectd_pause_sec = int(os.environ.get('FACE_DETECTED_PAUSE_SECOND', 2))
_local_screen_on = os.environ.get('FACE_SCREEN_ON', False)

_face_detect_recall = _face_detect_recall.lower()

if _face_detect_recall == 'low':
    _face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt_tree.xml')
elif _face_detect_recall == 'medium':
    _face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')
else:
    _face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')


class ipcamCapture:
    def __init__(self, _URL):
        self.Frame = []
        self.status = False
        self.isstop = False

        # Connect with Camera
        self.capture = cv2.VideoCapture(_URL)
    
    def start(self):
        print('ipcam started')
        threading.Thread(target=self.queryframe, daemon=True, args=()).start()

    def stop(self):
        self.isstop = True
        print('ipcam stopped!')

    def getframe(self):
        return self.Frame
    
    def queryframe(self):
        while (not self.isstop):
            self.status, self.Frame = self.capture.read()
        
        self.capture.release()

# Main Program Start
print('IP Cam: ' + _URL)
print('FaceWeb_URL: ', FaceWebAPI.PushFaceIdentifyByImageObject)
print('API Key: ' + FaceWebAPI.APIKey)
print('Group ID: ' + FaceWebAPI.PersonGroupId)
print('CommID: ' + _commId)
print('Min Width: ' + str(_face_min_width))
print('Min Height: ' + str(_face_min_height))
print('Pause Sec: ' + str(_face_detectd_pause_sec))


ipcam = ipcamCapture(_URL)
ipcam.start()
time.sleep(1)

while True:
    frame = ipcam.getframe()    
    try:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = _face_cascade.detectMultiScale(gray, scaleFactor=1.03, minNeighbors=5, minSize=(_face_min_width,_face_min_height))
        if (len(faces)>0):
            print('Dectect ' + str(len(faces)) + ' Faces.')   
            i = 0
            for (x,y,w,h) in faces:
                i = i + 1
                # Crop Face
                nX = int(x-(w/2))
                if (nX < 0):
                    nX = 0
                nY = int(y-(h/2))
                if (nY < 0):
                    nY = 0
                nW = 2*w
                nH = 2*h
                cropFrame = frame[nY:nY+nH, nX:nX+nW]

                # 加上框框
                #cv2.rectangle(frame, (x,y), (x+w, y+h), (255,0,0), 2) 
                #cv2.rectangle(frame, (nX,nY), (nX+nW, nY+nH), (0,255,0), 2) 
                    
                if _local_screen_on:                        
                    cv2.imshow('Image', cropFrame)
                    
                encodedFrame = cv2.imencode(".jpg", cropFrame)[1].tostring()
                
                # Call faceWebAPI to identify face, and get person Name if match                       
                print('Face(' + str(i) + ') call FaceAPI') 
                faceWebAPI = FaceWebAPI()        
                returnData = faceWebAPI.identifyByImageObject(_commId,_cameraId, encodedFrame)
                print(returnData)
            time.sleep(_face_detectd_pause_sec)
        
    except Exception as ex:
        print(str(ex))
        break    
   
    if _local_screen_on and cv2.waitKey(1000) == 27: 
        cv2.destroyAllWindows()
        ipcam.stop()
        break