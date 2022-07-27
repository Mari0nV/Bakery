from pydantic import BaseModel, validator
from typing import List

import bakery.database.models as db_models


class RecipeIngredient(BaseModel):
    id: str
    quantity: int

class Recipe(BaseModel):
    id: str
    name: str
    ingredients: list[RecipeIngredient]

    @validator("ingredients", pre=True, each_item=True)
    def ingredients_validator(cls, ingredient: db_models.RecipeIngredient) -> List[RecipeIngredient]:
        if isinstance(ingredient, db_models.RecipeIngredient):
            return { "id": ingredient.ingredient_id, "quantity": ingredient.quantity }
        return ingredient

    class Config:
        orm_mode = True
