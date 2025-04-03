import requests
import json
from datetime import datetime, timedelta
import time

def wait_until_target_time(target_hour, target_minute):
    while True:
        now = datetime.now()
        if now.hour == target_hour and now.minute == target_minute:
            print("ถึงเวลา 20:00 แล้ว! เริ่มทำงานที่ต้องการ")
            break
        else:
            # รออีก 60 วินาทีแล้วค่อยตรวจสอบเวลาใหม่
            time.sleep(60)

def send_line_message(access_token, sent_to, message):
    url = 'https://api.line.me/v2/bot/message/push'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {access_token}'
    }
    data = {
        'to': sent_to,
        'messages': [
            {
                'type': 'text',
                'text': message
            }
        ]
    }
    
    response = requests.post(url, headers=headers, data=json.dumps(data))
    
    if response.status_code == 200:
        print("ข้อความถูกส่งสำเร็จ")
    else:
        print("เกิดข้อผิดพลาดในการส่งข้อความ:", response.status_code, response.text)

# LINE API access token and recipient ID
access_token = '7tb3Jg/mVxCxrjd2GNueeIKE1fJUqygall4D+iiLGYblgi0lwrDXavuT51O4t0d0hiCDxPpbURV/zlM7zf1yPYl52ioR4mLmZu7gn9R2NLy87/4+NOu5EUSwKfIRB85WUGpJX0Rh9e16LOKH/oSoPQdB04t89/1O/w1cDnyilFU='
sent_to = 'Ceb7da36934d84c592ac29bb1ebbad9b9'

# กำหนดเวลาที่ต้องการให้โปรแกรมทำงาน (20:00)
target_hour = 20
target_minute = 0

# รอจนถึงเวลา 20:00
wait_until_target_time(target_hour, target_minute)

# ดึงข้อมูลจาก API
url = "https://script.google.com/macros/s/AKfycbx-rb5JmsvFbr-88bkXZiIATiKp5egXKogpqeKZsjIMUTZM3OSVrPkzFyuc1ncvsp15Tg/exec"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()

    # วันที่เป้าหมายคือวันพรุ่งนี้
    target_date = datetime.today() + timedelta(days=1)

    # ตรวจสอบข้อมูลแต่ละรายการ
    for entry in data['data']:
        date_str = entry['date']  # ตัวอย่าง: "01-06-2025"
        date_obj = datetime.strptime(date_str, "%d-%m-%Y")  # แปลง string เป็น datetime object

        if date_obj.date() == target_date.date():  # เปรียบเทียบวันที่
            # เอาข้อมูลที่ต้องการ
            send_date = entry['date']
            send_name = entry['name']
            send_stopwork = entry['stopwork']

            message = f"ตารางงานวันนี้: 🔔 ข้อมูลการทำงานประจำวันที่ {send_date} 🔔\n 👉 ชื่อ: {send_name} \n👤 คนหยุด: {send_stopwork} \n ⏰ เวลาออกงาน \n 🟢 วันที่เหลือ: undefined"

            # ส่งข้อความไปยัง LINE
            send_line_message(access_token, sent_to, message)

else:
    print(f"Error fetching data: {response.status_code}")
