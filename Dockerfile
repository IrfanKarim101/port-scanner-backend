FROM python:3.10-slim

RUN apt-get update && apt-get install -y nmap

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "backend/manage.py", "runserver", "0.0.0.0:8000"]
