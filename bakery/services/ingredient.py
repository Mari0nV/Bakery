from sqlalchemy.orm import Session
from bakery.api.errors.ingredient import IngredientAlreadyExisting

import bakery.database.models as db_models
from bakery.schemas.ingredient import Ingredient


def create_ingredient(db_session: Session, ingredient: Ingredient):
    ingredient_already_exists = db_session.query(db_models.Ingredient).filter(db_models.Ingredient.id == ingredient.id).one_or_none()

    if ingredient_already_exists is not None:
        raise IngredientAlreadyExisting(ingredient.id)

    new_ingredient = db_models.Ingredient(
        id=ingredient.id,
        name=ingredient.name,
        price=ingredient.price
    )
    db_session.add(new_ingredient)
    db_session.flush()

    return new_ingredient
