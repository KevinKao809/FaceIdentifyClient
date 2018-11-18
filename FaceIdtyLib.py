# -*- coding: utf-8 -*-
import requests
    
class FaceWebAPI:
    FaceIdentifyByImageURL = 'https://127.0.0.1/personGroups/{personGroupId}/identifyImageURL'
    FaceIdentifyByImageObject = 'https://127.0.0.1/personGroups/{personGroupId}/identifyImageObject'    
    PersonGroupId = 'd663ba15-85f8-49e0-b30b-cafcfc35a909'
    APIKey = 'WebAPIKey'
    
    def __init__(self):
        self.FaceIdentifyByImageURL = FaceWebAPI.FaceIdentifyByImageURL.replace("{personGroupId}", FaceWebAPI.PersonGroupId)
        self.FaceIdentifyByImageObject = FaceWebAPI.FaceIdentifyByImageObject.replace("{personGroupId}", FaceWebAPI.PersonGroupId)        
    
    def identifyByImageObject(self, frame):
        try:
            files = {'FacePhoto': frame}  
            postData = {'apiKey': FaceWebAPI.APIKey}  
            matchResult = requests.post(self.FaceIdentifyByImageObject, data=postData, files = files)
            if matchResult.status_code == 401:
                return 'APIKey Fail'
            elif matchResult.status_code == 200:
                resultObj = matchResult.json()   
                name = resultObj['name']
                return name
            else:
                return '...'  
        except requests.HTTPError as e:
            return e
        except Exception as e:
            print (e)
            return '...'
    
    def identifyByImageURL(self, imageURL):
        postData = '{"url":"' + imageURL + '", "apiKey":"' + FaceWebAPI.APIKey + '"}'        
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

               
        
        
        
        
        