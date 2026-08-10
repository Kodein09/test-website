FROM python:3.12-slim
LABEL authors='Roy'

WORKDIR /app

COPY requirements.txt .

RUN pip --upgrade & pip install --nocache-dir -r requirements.txt

COPY . .

CMD ["fastapi", "dev", "main.py", "--host", "0.0.0.0"]