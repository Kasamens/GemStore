from fastapi import FastAPI
from database import create_db
import models.gem_models as gem_models
import uvicorn
from sqlmodel import Session, select
from database import engine
from typing import List

app = FastAPI()

create_db()


@app.get("/gems")
def get_gems() -> List[gem_models.Gem]:
    with Session(engine) as session:
        statement = select(gem_models.Gem)
        result = session.exec(statement)
        return result.all()


@app.post("/gems/{gem}")
def add_gem(new_gem: gem_models.Gem, gem_props: gem_models.GemProperties):

    gem_props = gem_models.GemProperties(
        gemsize=gem_props.size, clarity=gem_props.clarity, color=gem_props.color)
    gem = gem_models.Gem(price=new_gem.price, available=new_gem.available,
                         gem_type=new_gem.gem_type, gem_properties=gem_props)

    with Session(engine) as session:
        session.add(gem)
        session.commit()
        # session.add(gem_props)
        # session.commit()
        session.close()


if __name__ == '__main__':
    uvicorn.run(app, host='localhost', port=8070)
