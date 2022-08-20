from fastapi import FastAPI
from database import create_db
import models.gem_models
import uvicorn

app = FastAPI()

create_db()


@app.get("/")
def hello():
    return "Hello World"


if __name__ == '__main__':
    uvicorn.run(app, host='localhost', port=9000)
