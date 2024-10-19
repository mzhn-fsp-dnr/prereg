FROM python:3.12-alpine3.20

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .

ARG APP_PORT

CMD uvicorn app.main:app --root-path /prereg --host 0.0.0.0 --port $APP_PORT