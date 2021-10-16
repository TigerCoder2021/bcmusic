import requests
import json

url = "https://kauth.kakao.com/oauth/authorize"

data = {
    "client_id" : "6f86b2c435a386a703385dccb678aa7d",
    "redirect_url" : "https://bcmusic.co.kr",
    "response_type" : "code"
}

response = requests.get(url, header=data)
print(response)