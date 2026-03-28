from fastapi import FastAPI, APIRouter
from fastapi.responses import PlainTextResponse

app = FastAPI(
    title="Effective Mobile Test",
)

@app.get("/", response_class=PlainTextResponse)
def root():
    return "Hello from Effective Mobile!"

@app.get("/health", response_class=PlainTextResponse)
def health():
    return "OK"

