import requests
import json

# 카카오톡 메시지 API
url = "https://kauth.kakao.com/oauth/token"

with open("kakao_authorization_code.json", "r") as fp:
    tokens = json.load(fp)

data = {
    "grant_type": "refresh_token",
    "client_id" : "6f86b2c435a386a703385dccb678aa7d",
    "refresh_token": tokens["refresh_token"]
}
response = requests.post(url, data=data)
tokens = response.json()
print(tokens)

url = "https://kapi.kakao.com/v1/api/talk/friends" #친구 목록 가져오기
# url = "https://kapi.kakao.com/v2/user/scopes"
header = {"Authorization": 'Bearer ' + tokens["access_token"]}

result = json.loads(requests.get(url, headers=header).text)

# url = 'https://kapi.kakao.com/v2/user/scopes'
# result = json.loads(requests.get(url, headers=header).text)
print(result)
