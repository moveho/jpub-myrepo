FROM python:3.8-slim

WORKDIR /app
COPY . /app

# cryptography 설치에 필요한 빌드 패키지 추가
RUN apt-get update && \
    apt-get install -y gcc libffi-dev libssl-dev && \
    pip install --upgrade pip && \
    pip install -r requirements.txt

CMD ["python", "app.py"]
