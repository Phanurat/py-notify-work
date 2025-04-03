import datetime
import time

def check_time():
    # กำหนดเวลาที่ต้องการ
    target_hour = 20
    target_minute = 00

    while True:
        # ดึงเวลาปัจจุบัน
        now = datetime.datetime.now()
        
        # ตรวจสอบว่าเวลาปัจจุบันตรงกับ 15:21 หรือไม่
        if now.hour == target_hour and now.minute == target_minute:
            print("เวลาถึง 15:21 แล้ว! ทำงานที่ต้องการ")
            # ใส่ฟังก์ชันหรือคำสั่งที่ต้องการให้ทำงานที่นี่
            break  # ออกจากลูปหลังทำงานเสร็จ
        else:
            # ถ้ายังไม่ถึงเวลา 15:21 ให้รอ 1 นาที (เพื่อไม่ให้โปรแกรมตรวจสอบบ่อยเกินไป)
            time.sleep(60)

# เรียกใช้งานฟังก์ชัน
check_time()
