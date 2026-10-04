from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Привет!"}


Instrumentator().instrument(app).expose(app)