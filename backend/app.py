from fastapi import FastAPI, APIRouter
from fastapi.responses import PlainTextResponse

app = FastAPI(
    title="Effective Mobile Test",
)

simple_router = APIRouter(prefix="/")


@simple_router.get("/", response_class=PlainTextResponse)
def root():
    return "Hello from Effective Mobile!"


@simple_router.get("/health", response_class=PlainTextResponse)
def health():
    return "OK"


app.include_router(simple_router)

