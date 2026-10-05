from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Привет! feryeryf485ty485yfu45gh45gy845!"}


Instrumentator().instrument(app).expose(app)