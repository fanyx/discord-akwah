from peewee import CharField
from src.db.database import BaseModel

class Item(BaseModel):
    name = CharField()
    picture = CharField()