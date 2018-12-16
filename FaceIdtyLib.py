# -*- coding: utf-8 -*-
import requests, os
import datetime
    
class FaceWebAPI:
    FaceIdentifyByImageURL = 'http://faceweb-stage.azurewebsites.net/personGroups/{personGroupId}/identifyImageURL'
    FaceIdentifyByImageObject = 'http://faceweb-stage.azurewebsites.net/personGroups/{personGroupId}/identifyImageObject'    
    PushFaceIdentifyByImageObject = os.environ.get('FACE_IMAGE_PUSH_URL', 'http://face1119.micro-second.net/personGroups/{personGroupId}/pushIdentifyImageObject') 
    #PushFaceIdentifyByImageObject = os.environ.get('FACE_IMAGE_PUSH_URL', 'http://127.0.0.1:5000/personGroups/{personGroupId}/pushIdentifyImageObject')      
    PersonGroupId = os.environ.get('FACE_PERSON_GROUP_ID', 'ed2dbde7-8160-423e-82d7-a93eb1c7ffd7')
    APIKey = os.environ.get('FACE_API_KEY','WebAPIKey-20181111')
    
    def __init__(self):
        self.FaceIdentifyByImageURL = FaceWebAPI.FaceIdentifyByImageURL.replace("{personGroupId}", FaceWebAPI.PersonGroupId)
        self.FaceIdentifyByImageObject = FaceWebAPI.FaceIdentifyByImageObject.replace("{personGroupId}", FaceWebAPI.PersonGroupId)   
        self.PushFaceIdentifyByImageObject = FaceWebAPI.PushFaceIdentifyByImageObject.replace("{personGroupId}", FaceWebAPI.PersonGroupId)  
    
    def identifyByImageObject(self, commId, cameraId, frame):
        try:
            files = {'FacePhoto': frame}  
            postData = {'apiKey': FaceWebAPI.APIKey, 'commId': commId, 'cameraId': cameraId, 'timestamp': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}  
            matchResult = requests.post(self.PushFaceIdentifyByImageObject, data=postData, files = files)
            if matchResult.status_code == 401:
                return 'APIKey Fail'
            elif matchResult.status_code == 200:
                return matchResult.text
            else:
                return '...'  
        except requests.HTTPError as e:
            return e
        except Exception as e:
            print (e)
            return '...'
    
    def identifyByImageURL(self, commId, cameraId, imageURL):
        postData = '{"url":"' + imageURL + '", "apiKey":"' + FaceWebAPI.APIKey + '", "commId":"' + commId + '", "cameraId":"' + cameraId + '"}'        
        try:
            matchResult = requests.post(self.FaceIdentifyByImageURL, json=postData)
            resultObj = matchResult.json()  
            return str(resultObj)  
        except requests.HTTPError as e:
            return e
        except Exception as e:
            print (e)
            return '...'

        