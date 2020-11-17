from peewee import ForeignKeyField, IntegerField
from . import Collectible, Item

class ItemRecipe(BaseModel):
    output_item_id = ForeignKeyField(Item)

class ItemRecipeShard(BaseModel):
    recipe_id = ForeignKeyField(ItemRecipe)
    collectible_id = ForeignKeyField(Collectible)
    amount = IntegerField()