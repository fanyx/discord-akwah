from peewee import CharField
from src.db import BaseModel

class Collectible(BaseModel):
    name = CharField()
    picture = CharField()