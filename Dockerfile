# ใช้ Python image
FROM python:3.9-slim

# ตั้ง working directory
WORKDIR /app

# คัดลอกไฟล์ทั้งหมดไปยัง container
COPY . /app

# ติดตั้ง dependencies
RUN pip install --no-cache-dir -r requirements.txt

# รันโปรแกรม
CMD ["python", "main.py"]
