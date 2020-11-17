from peewee import Model, SqliteDatabase
from main import config

if (DB_PATH := config["DB"]["path"]) is None:
    DB_PATH = 'app.db'

database = SqliteDatabase(DB_PATH, pragmas={
    'journal_mode': 'wal',
    'cache_size': 10000,
    'foreign_keys': 1
})

class BaseModel(Model):

    class Meta:
        database = database