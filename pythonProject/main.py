import requests
import json

# 카카오톡 메시지 API
url = "https://kauth.kakao.com/oauth/token"

data = {
    "grant_type": "authorization_code",
    "client_id" : "6f86b2c435a386a703385dccb678aa7d",
    "redirect_url" : "https://bcmusic.co.kr",
    "code" : "2IyUHJ_Gdm3pC4F3ULJv7HNlIVfBtsvhE5FMzYZ6WQ3Knkxza_AhrUQw2PytrNc8qjsC4AopyNkAAAF8fsCaGw"
}
response = requests.post(url, data=data)
tokens = response.json()
print(tokens)

# kakao_code.json 파일 저장
with open("kakao_authorization_code.json", "w") as fp:
    json.dump(tokens, fp)