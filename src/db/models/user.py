from peewee import CharField, IntegerField
from src.db import BaseModel

class User(BaseModel):
    user_id = CharField()
    xp = IntegerField(default=0) # Total xp accumulated
    xp_mod = IntegerField(default=100) # XP Modifier in Percent // Can be 0 for XP-Lock, but not negative
    level = IntegerField(default=1)