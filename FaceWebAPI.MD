# FACE Web Client API 
#### Version : 2018-12-16
Face Web Client API support 3 face identify methods:
1. By passing a json content, including face image URL and API Key
1. By passing a multipart content, including face image file and API Key
1. by passing a multipart content, including face image file, API Key and specify by PUSH mode

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


## Identify By Image File Object, and specify by PUSH mode
End Point: /personGroups/{personGroupId}/pushIdentifyImageObject

Method: POST

Encode: multipart/form-data


| Field Name |   Type   |     Value         |
|------------|:--------:|------------------:|
| FacePhoto  |  File    | Image File Object |
| apiKey     |  Text    | Face Web API Key  |
| commId     |  Text    | Community ID      |
| cameraId   |  Text    | Camera Id         |
| timestamp  |  Text    | YYYY-MM-DD HH:MM:SS  |
| pushURL    |  Text    | The push URL after identify Image  |

---
## Response
There are 6 different response type return by above APIs:

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

### 4. Response (only happen on PUSH mode) / Http Status: 200 OK

    {
        "OK"
    }

### 5. Response (API Key Fail) / Http Stauts : 401 Unauthorized

### 6. Response (personGroups ID fail) / Http Status : 400 Bad Request

---

# FACE Web Admin API 
#### Version : 2018-12-16
Face Web Admin API offers management features on personGroup, person and photo.

---
## Get Person Group List
End Point: /api/personGroups

Header: FACEWeb_Token=xxxxxx

Method: GET

Encode: application/json

Request Body:

    None

Response Body:

    [
        {"personGroupId":"e01797bc-fa3d-48ee-913b-78f33560906a","name":"Test Group","userData":"Test Group"},
        {"personGroupId":"ed2dbde7-8160-423e-82d7-a93eb1c7ffd7","name":"White Group","userData":null}
    ]

---

## Create Person Group
End Point: /api/personGroups

Header: FACEWeb_Token=xxxxxx

Method: PUT

Encode: application/json

Request Body:

    {"name": "my New Group", "userData": "This is a new group"}

Response Body:

    {"personGroupId": "f9e77a58-5b94-4d12-8853-bfe54e5c471d"}

---

## Delete Person Group
End Point: /api/personGroups/{personGroupId}

Header: FACEWeb_Token=xxxxxx

Method: DELETE

Encode: application/json

Request Body:

    None

Response Body:

    None

---

## Train Person Group
End Point: /api/personGroups/{personGroupId}/train

Header: FACEWeb_Token=xxxxxx

Method: POST

Encode: application/json

Request Body:

    None

Response Body:

    None

---

## Get Train Status of Person Group
End Point: /api/personGroups/{personGroupId}/trainingStatus

Header: FACEWeb_Token=xxxxxx

Method: GET

Encode: application/json

Request Body:

    None

Response Body:

    {"status":"succeeded","createdDateTime":"2018-12-16T04:03:42.6389156Z","lastActionDateTime":"2018-12-16T04:03:42.9121051Z","message":null}

---

## Get Person List of a Person Group
End Point: /api/personGroups/{personGroupId}/persons

Header: FACEWeb_Token=xxxxxx

Method: GET

Encode: application/json

Request Body:

    None

Response Body:

    [
        {
            "personId":"5bd55c9f-a1f5-4fcb-99b6-6714e7a91ce9",
            "persistedFaceIds":
            [
                "253af6e7-ee82-4c77-9e91-d257d63070a3",
                "2e32c470-1427-4769-8182-0ffb5d41a969"
            ],
            "name":"陳XX",
            "userData":"123"
        },
        {
            "personId":"79b52d74-09a0-44c2-997c-1a8b239fefbb",
            "persistedFaceIds":
            [
                "238b91fe-2c0b-4302-a32f-98c6af27f67a",
                "6196cb9e-b414-4ff5-bf18-d1a3035f7d05",
                "a2c916e5-1227-47c2-876b-f0418089fee0"
            ],
            "name":"李XX",
            "userData":"456"
        }
    ]

---

## Get a Person of a Person Group
End Point: /api/personGroups/{personGroupId}/persons/{personId}

Header: FACEWeb_Token=xxxxxx

Method: GET

Encode: application/json

Request Body:

    None

Response Body:

    {
        "personId":"5bd55c9f-a1f5-4fcb-99b6-6714e7a91ce9",
        "persistedFaceIds":
        [
            "253af6e7-ee82-4c77-9e91-d257d63070a3",
            "2e32c470-1427-4769-8182-0ffb5d41a969"
        ],
        "name":"陳XX",
        "userData":"123"
    }

---

## Create a Person under a Person Group
End Point: /api/personGroups/{personGroupId}/persons

Header: FACEWeb_Token=xxxxxx

Method: POST

Encode: application/json

Request Body:

    {"name": "王曉明", "userData": "999"}

Response Body:

    {"personId":"4f9b9cdc-e5a3-462c-8b06-509f0acf402b"}

---

## Update a Person under a Person Group
End Point: /api/personGroups/{personGroupId}/persons/{personId}

Header: FACEWeb_Token=xxxxxx

Method: PATCH

Encode: application/json

Request Body:

    {"name": "王曉華", "userData": "888"}

Response Body:

    None

---

## Get a Person's photo list under a Person Group
End Point: /api/personGroups/{personGroupId}/persons/{personId}/photos

Header: FACEWeb_Token=xxxxxx

Method: GET

Encode: application/json

Request Body:

    None

Response Body:

    [
        {
            "persistedFaceId":"253af6e7-ee82-4c77-9e91-d257d63070a3",
            "imageURL":"https://xxxxxxxx"},
        {
            "persistedFaceId":"2e32c470-1427-4769-8182-0ffb5d41a969",
            "imageURL":"https://xxxxxxxx"},
        {
            "persistedFaceId":"3536a07b-7f0f-4eff-9b4d-35c2ce6d4dab",
            "imageURL":"https://xxxxxxxx"},            
        }
    ]

---

## Delete a Person under a Person Group
End Point: /api/personGroups/{personGroupId}/persons/{personId}

Header: FACEWeb_Token=xxxxxx

Method: DELETE

Encode: application/json

Request Body:

    None

Response Body:

    None

---

## Delete a Person's face photo under a Person Group
End Point: /api/personGroups/{personGroupId}/persons/{personId}/face/{faceId}

Header: FACEWeb_Token=xxxxxx

Method: DELETE

Encode: application/json

Request Body:

    None

Response Body:

    None

---


## Upload a person's photo under a Person Group
End Point: /api/personGroups/{personGroupId}/persons/{personId}/uploadPhoto

Header: FACEWeb_Token=xxxxxx

Method: POST

Encode: multipart/form-data

Request Body:

    | Field Name |   Type   |     Value         |
    |------------|:--------:|------------------:|
    | FacePhoto  |  File    | Image File Object |

Response Body:

    {"persistedFaceId":"b663a305-59b0-45bd-8deb-4daaa02cd431"}

---

## Error Response

### 1. 400 Bad Request

Resons:
1. The parameters or data of request are not match with specification

### 2. 401 Authorization Fail

Resons:
1. There is no valid API Token on request header
1. The API Token get expired

### 3. 404 Not Found

Resons:
1. The Id (personGroupId, personId, faceId) is invlaid.

### 4. 405 Method Not Allowed

Resons:
1. The request Method (GET, POST, PUT, DELETE) was not match with EndPoint URL.

### 5. 500 Internal Server Error

Resons:
1. Unexpect error occur.

---

## How to get FACEWeb_Token

End Point: /auth

Method: POST

Encode: form-data

Request Body:

    | Field Name |   Type   |     Value         |
    |------------|:--------:|------------------:|
    | username   |  text    | {login ID}        |
    | password   |  text    | {password}        |

Response Body:

    {
        "token": "oK9UqJiappehUJvKr5qqUdiekKuWrVaYmtzQroSnm5Oll9mFypepnrFNpJeQo5uUUKCfrqCzVak",
        "expired": "2018-12-16 05:53:56 UTC"
    }

### Remark
1. You shall append FACEWeb Token on header of each http request, such as
    FACEWEB_Token=oK9UqJiappehUJvKr5qqUdiekKuWrVaYmtzQroSnm5Oll9mFypepnrFNpJeQo5uUUKCfrqCzVak
1. Token will be expired, and you shall re-use valid token untill it get expired.

---