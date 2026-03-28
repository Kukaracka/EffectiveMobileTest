FROM python:3.11-alpine

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .

RUN adduser -D appuser
USER appuser

EXPOSE 8080

HEALTHCHECK CMD wget -qO- http://localhost:8080/health || exit 1

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8080"]
