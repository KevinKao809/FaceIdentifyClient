# FACE Web Client API 
#### Version : 2018-10-20
Face Web Client API support two face identify methods:
1. By passing a json content, including face image URL and API Key
1. By passing a multipart content, including face image file and API Key

---
## Identify By Image URL
End Point: /personGroups/{personGroupId}/identifyImageURL

Method: POST

Encode: application/json

Request Body:

    {
        "url": "image url",
        "apiKey" : "Face Web API Key"
    }

---

## Identify By Image File Object
End Point: /personGroups/{personGroupId}/identifyImageObject

Method: POST

Encode: multipart/form-data


| Field Name |   Type   |     Value         |
|------------|:--------:|------------------:|
| FacePhoto  |  File    | Image File Object |
| apiKey     |  Text    | Face Web API Key  |

---
## Response
There are 4 different response type return by above APIs:

### 1. Response (face identified) / Http Status: 200 OK

    {
        "code": 0,
        "confidence":0.8566,
        "personId":"36293b6c-9c70-4fda-b75b-dce72be2a072",
        "persistedFaceIds":[
            "36638015-63ae-42db-b8ba-63981ca89f63",
            "a6280b53-207f-4583-b4c0-de7ff32ff7f3",
            "d75a1575-1d8c-49fe-9e3e-8eea542e41f7"
            ],
        "name":"the person name input at FaceWeb App",
        "userData":"the data associated with person name"
    }
### 2. Response (face not match) / Http Status: 200 OK

    {
        "code": 1
    }

### 3. Response (Not a face image) / Http Status: 200 OK

    {
        "code": 2
    }

### 4. Response (API Key Fail) / Http Stauts : 401 Unauthorized

### 5. Response (personGroups ID fail) / Http Status : 400 Bad Request