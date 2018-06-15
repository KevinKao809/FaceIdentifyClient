# -*- coding: utf-8 -*-
import requests
    
class FaceWebAPI:
    FaceIdentifyByImageURL = 'https://aifaceweb.azurewebsites.net/personGroups/{personGroupId}/identifyImageURL'
    FaceIdentifyByImageObject = 'https://aifaceweb.azurewebsites.net/personGroups/{personGroupId}/identifyImageObject'    
    PersonGroupId = '5f6a671b-781a-4257-ad37-6d2ef4aa20c0'
    
    def __init__(self):
        self.FaceIdentifyByImageURL = FaceWebAPI.FaceIdentifyByImageURL.replace("{personGroupId}", FaceWebAPI.PersonGroupId)
        self.FaceIdentifyByImageObject = FaceWebAPI.FaceIdentifyByImageObject.replace("{personGroupId}", FaceWebAPI.PersonGroupId)
    
    def identifyByImageObject(self, frame):
        try:
            files = {'photo.jpg': frame}
            matchResult = requests.post(self.FaceIdentifyByImageObject, files = files)
            resultObj = matchResult.json()   
            name = resultObj['name']
            return name  
        except requests.HTTPError as e:
            return e
        except Exception as e:
            print (e)
            return '...'
    
    def identifyByImageURL(self, imageURL):
        postData = '{"url":"' + imageURL + '"}'        
        try:
            matchResult = requests.post(self.FaceIdentifyByImageURL, json=postData)
            resultObj = matchResult.json()   
            name = resultObj['name']
            return name  
        except requests.HTTPError as e:
            return e
        except Exception as e:
            print (e)
            return '...'

               
        
        
        
        
        