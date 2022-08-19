from sqlmodel import SQLModel, create_engine

engine = create_engine('sqlite:///database.db', echo=True)


def create_db():
    SQLModel.metadata.create_all(engine)
