from fastapi import FastAPI
import uvicorn
from database import create_db

app = FastAPI()

create_db()


@app.get("/")
def hello():
    return "Hello World"
