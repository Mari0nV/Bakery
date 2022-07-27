from sqlalchemy.orm import Session
from bakery.api.errors.recipe import RecipeAlreadyExisting

import bakery.database.models as db_models
from bakery.schemas.recipe import Recipe


def create_recipe(db_session: Session, recipe: Recipe):
    recipe_already_exists = db_session.query(db_models.Recipe).filter(db_models.Recipe.id == recipe.id).one_or_none()

    if recipe_already_exists is not None:
        raise RecipeAlreadyExisting(recipe.id)

    new_recipe = db_models.Recipe(
        id=recipe.id,
        name=recipe.name
    )
    db_session.add(new_recipe)
    db_session.flush()

    for ingredient in recipe.ingredients:
        ingredient_already_exists = (
            db_session.query(db_models.Ingredient).filter(db_models.Ingredient.id == ingredient.id).one_or_none()
        )
        if ingredient_already_exists is not None:
            new_ingredient = db_models.Ingredient(id=ingredient.id)
            db_session.add(new_ingredient)
            db_session.flush()

        new_ingredient_recipe = db_models.RecipeIngredient(recipe_id=recipe.id, ingredient_id=ingredient.id, quantity=ingredient.quantity)
        db_session.add(new_ingredient_recipe)
        db_session.flush()

    return new_recipe
