FROM python:3.8.12-slim-buster

WORKDIR /app

COPY . .

RUN python3 -m pip install -r requirements.txt

CMD ["python3", "main.py"]