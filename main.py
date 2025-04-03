import requests
import json
from datetime import datetime, timedelta
import time

def check_time():
    target_hour = 20
    target_minute = 00

    while True:
        now = datetime.datetime.now()

        if now.hour == target_hour and now.minute == target_minute:
            print("เวลาถึง 20.00 แล้ว! ทำงานที่ต้องการ")

            break
        else:
            time.sleep(60)

# LINE API access token and recipient ID
access_token = '7tb3Jg/mVxCxrjd2GNueeIKE1fJUqygall4D+iiLGYblgi0lwrDXavuT51O4t0d0hiCDxPpbURV/zlM7zf1yPYl52ioR4mLmZu7gn9R2NLy87/4+NOu5EUSwKfIRB85WUGpJX0Rh9e16LOKH/oSoPQdB04t89/1O/w1cDnyilFU='
sent_to = 'Ceb7da36934d84c592ac29bb1ebbad9b9'

while True:
    # Fetch the data from the API
    url = "https://script.google.com/macros/s/AKfycbx-rb5JmsvFbr-88bkXZiIATiKp5egXKogpqeKZsjIMUTZM3OSVrPkzFyuc1ncvsp15Tg/exec"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        # Get today's date as the target date
        target_date = datetime.today() + timedelta(days=1)  # This will be today's date

        # Iterate over the data list to access each entry
        for entry in data['data']:
            # Parse the date string from the entry
            date_str = entry['date']  # Example: "01-06-2025"
            date_obj = datetime.strptime(date_str, "%d-%m-%Y")  # Convert string to datetime object

            # Compare it with today's date
            if date_obj.date() == target_date.date():  # .date() compares just the date part
                # Extract the relevant information
                send_date = entry['date']
                send_name = entry['name']
                send_stopwork = entry['stopwork']

                message = f"ตารางงานวันนี้: 🔔 ข้อมูลการทำงานประจำวันที่ {send_date} 🔔\n 👉 ชื่อ: {send_name} \n👤 คนหยุด: {send_stopwork} \n ⏰ เวลาออกงาน \n 🟢 วันที่เหลือ: undefined"

                # Prepare the data for the LINE message
                data = {
                    'to': sent_to,
                    'messages': [
                        {
                            'type': 'text',
                            'text': message
                        }
                    ]
                }

                url = 'https://api.line.me/v2/bot/message/push'

                headers = {
                    'Content-Type': 'application/json',
                    'Authorization': f'Bearer {access_token}'
                }

                # Send the message
                response = requests.post(url, headers=headers, data=json.dumps(data))

                if response.status_code == 200:
                    print("ข้อความถูกส่งสำเร็จ")
                else:
                    print("เกิดข้อผิดพลาดในการส่งข้อความ:", response.status_code, response.text)
    else:
        print(f"Error fetching data: {response.status_code}")

    #time.sleep(10)
    check_time()
