FROM python:3.11-alpine

WORKDIR /app

COPY requirements.txt .
RUN apk add --no-cache wget \
    && pip install --no-cache-dir -r requirements.txt

COPY app.py .

RUN adduser -D appuser
USER appuser

EXPOSE 8080

HEALTHCHECK CMD wget -qO- http://127.0.0.1:8080/health || exit 1

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8080"]
