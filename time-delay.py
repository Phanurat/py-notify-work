import datetime

# ดึงเวลาปัจจุบัน
now = datetime.datetime.now()

# แสดงวันที่และเวลา
print("Current date and time:", now)

# แสดงแค่วันที่
current_date = now.date()
print("Current date:", current_date)

# แสดงแค่เวลา
current_time = now.time()
print("Current time:", current_time)
