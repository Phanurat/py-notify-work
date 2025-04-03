import requests
import json
from datetime import datetime, timedelta
import time

# LINE API access token and recipient ID
access_token = '7tb3Jg/mVxCxrjd2GNueeIKE1fJUqygall4D+iiLGYblgi0lwrDXavuT51O4t0d0hiCDxPpbURV/zlM7zf1yPYl52ioR4mLmZu7gn9R2NLy87/4+NOu5EUSwKfIRB85WUGpJX0Rh9e16LOKH/oSoPQdB04t89/1O/w1cDnyilFU='
sent_to = 'Ceb7da36934d84c592ac29bb1ebbad9b9'

def fetch_and_send():
    """ดึงข้อมูลจาก API และส่งข้อความไปยัง LINE"""
    url = "https://script.google.com/macros/s/AKfycbx-rb5JmsvFbr-88bkXZiIATiKp5egXKogpqeKZsjIMUTZM3OSVrPkzFyuc1ncvsp15Tg/exec"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        target_date = datetime.today() + timedelta(days=1)

        for entry in data.get('data', []):
            date_str = entry['date']
            date_obj = datetime.strptime(date_str, "%d-%m-%Y")

            if date_obj.date() == target_date.date():
                send_date = entry['date']
                send_name = entry['name']
                send_stopwork = entry['stopwork']

                message = f"""🔔 ข้อมูลการทำงานประจำวันที่ {send_date} 🔔
👉 ชื่อ: {send_name}
👤 คนหยุด: {send_stopwork}
⏰ เวลาออกงาน
🟢 วันที่เหลือ: undefined"""

                headers = {
                    'Content-Type': 'application/json',
                    'Authorization': f'Bearer {access_token}'
                }

                data = {
                    'to': sent_to,
                    'messages': [{'type': 'text', 'text': message}]
                }

                response = requests.post('https://api.line.me/v2/bot/message/push', 
                                         headers=headers, 
                                         data=json.dumps(data))

                if response.status_code == 200:
                    print("📩 ข้อความถูกส่งสำเร็จ!")
                else:
                    print(f"❌ ส่งข้อความไม่สำเร็จ: {response.status_code} - {response.text}")
    else:
        print(f"❌ ดึงข้อมูล API ไม่สำเร็จ: {response.status_code}")

def main():
    """เช็คเวลาและเรียกใช้ fetch_and_send() เมื่อถึง 20:00 น."""
    while True:
        now = datetime.now()
        if now.hour == 20 and now.minute == 0:
            print("⏰ เวลาถึง 20:00 แล้ว! กำลังส่งข้อความ...")
            fetch_and_send()
            time.sleep(60)  # รอ 60 วินาที เพื่อป้องกันการส่งข้อความซ้ำ
        else:
            print("กำลังรอเวลาเพื่อจะส่ง")
            time.sleep(60)

        time.sleep(30)  # ตรวจสอบทุกๆ 30 วินาที

if __name__ == "__main__":
    main()
