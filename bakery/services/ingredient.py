from sqlalchemy.orm import Session
from bakery.api.errors.ingredient import IngredientAlreadyExisting, IngredientNotFound

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


def get_ingredient_by_id(db_session: Session, ingredient_id: str):
    ingredient = db_session.query(db_models.Ingredient).filter(db_models.Ingredient.id == ingredient_id).one_or_none()

    if ingredient is None:
        raise IngredientNotFound(ingredient_id)

    return ingredient


def get_all_ingredients(db_session: Session):
    return db_session.query(db_models.Ingredient).all()


def delete_ingredient(db_session: Session, ingredient_id: str):
    ingredient = db_session.query(db_models.Ingredient).filter(db_models.Ingredient.id == ingredient_id).one_or_none()

    if ingredient is None:
        raise IngredientNotFound(ingredient_id)

    db_session.delete(ingredient)
    db_session.flush()


def edit_ingredient(db_session: Session, ingredient: Ingredient):
    new_ingredient_values = ingredient.dict(exclude_unset=True)

    ingredient_db = db_session.query(db_models.Ingredient).filter(db_models.Ingredient.id == ingredient.id).one_or_none()

    if ingredient is None:
        raise IngredientNotFound(ingredient.id)

    for field_name, field_value in new_ingredient_values.items():
        setattr(ingredient_db, field_name, field_value)

    db_session.add(ingredient_db)
    db_session.flush()

    return ingredient_db
