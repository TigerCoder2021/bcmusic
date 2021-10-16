import attendance_to_image_model

import time
import pygsheets
import os.path
import shutil
from oauth2client.service_account import ServiceAccountCredentials
import itertools

# -----------------------Spreadsheet setup ---------------------
scope = [
    'https://www.googleapis.com/auth/drive',
]
json_file_name = 'clear-zenith-299913-2b735f599ff3.json'
credentials = ServiceAccountCredentials.from_json_keyfile_name(json_file_name, scope)
gc = pygsheets.authorize(service_file=json_file_name)

# --------------------------------------------------------------

spreadsheet = gc.open('수납관리')
sheet = spreadsheet.worksheets()[1]
teacher_list = list(itertools.chain.from_iterable(spreadsheet.worksheets()[0].get_values((3, 13), (17, 14))))
teacher_list = [v for v in teacher_list if v]
print(spreadsheet.worksheets()[0].url)
save_path = 'C:\\Users\\admin\\Desktop\\attendance\\출결 파일'
sheet_url = 'http://docs.google.com/feeds/download/spreadsheets/Export?' \
            'key=1VM00nved7joz20rRD_M1k_E6F0ZFCG70RQ5KfjRzcgY&exportFormat=pdf&gid=0'

if os.path.exists(save_path):
    shutil.rmtree(save_path)
time.sleep(0.25)
attendance_to_image_model.create_path(save_path)

teacher_info = attendance_to_image_model.convert_to_pdf(sheet, teacher_list, save_path)
attendance_to_image_model.save_to_doc(teacher_info)
print('pdf 다운로드 완료')

# attendance_to_image_model.convert_pdf_to_image(save_path)
# print('이미지 다운로드 완료')
