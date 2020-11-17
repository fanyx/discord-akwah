from peewee import CharField, ForeignKeyField, IntegerField
from src.db import BaseModel

class Inventory(BaseModel):
    user_id = CharField()
    item_id = ForeignKeyField(Item)
    amount = IntegerField(default=0)