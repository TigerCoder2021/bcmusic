import requests
import json

with open("kakao_code.json", "r") as fp:
    tokens = json.load(fp)

print(tokens["access_token"])