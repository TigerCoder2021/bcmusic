import requests
import json
from attendance_to_image import teacher_info
from datetime import date

def text_to_send(friends_list):
    text_dict = dict()
    day = date.today().day
    month = date.today().month
    for teacher in teacher_info:
        name = teacher[0] + 'T'
        text = teacher[0] + ' 강사님 ' + str(month) + '/' + str(day) + ' 까지 수업횟수 정리사항 입니다.'
        for student in teacher[3]:
            text += '\n' + student[0] + ' ' + str(student[1]) + '회 ' + student[2]
        text_dict[name] = text
        print(text)
    return text_dict




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
header = {"Authorization": 'Bearer ' + tokens["access_token"]}

result = json.loads(requests.get(url, headers=header).text)
friends_list = result.get("elements")
print(friends_list)
friend_id = friends_list[1].get("uuid")
print(friend_id)

url= "https://kapi.kakao.com/v1/api/talk/friends/message/default/send"

text_dict = text_to_send(friends_list)
message_status = dict()
friend_already_sent = set()
for friend in friends_list:
    if friend['profile_nickname'] in set(text_dict.keys()):
        data={
            'receiver_uuids': '["{}"]'.format(friend.get("uuid")),
            "template_object": json.dumps({
                "object_type": "text",
                "text":text_dict[friend['profile_nickname']],
                "link":{},
                "button_title": " "
            })
        }
        response = requests.post(url, headers=header, data=data)
        if response.status_code == 200:
            message_status[friend['profile_nickname']] = 'response [200] ' + '메시지 전송 성공'
        else:
            message_status[friend['profile_nickname']] = 'response [' + str(response.status_code) + '] 메시지 전송 실패. 이유: ' + response.text
        friend_already_sent.add(friend['profile_nickname'])  # 메시지 전송 요청된 강사 이름 저장
    else:
        message_status[friend['profile_nickname']] = ' 메시지 전송 실패. 이유: 이름 규칙이 어긋났거나 수납관리에 등록이 안되있음'

teacher_not_registered = list(set(text_dict.keys()) - friend_already_sent)

for t in teacher_not_registered:
    message_status[t] = '메시지 전송 실패. 이유: 카카오톡 친구가 아니거나 앱 로그인을 안했음'

for teacher in list(message_status.items()):
    print(teacher[0] + ' ' + teacher[1])





