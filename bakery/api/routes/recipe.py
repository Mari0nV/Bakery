from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from bakery.database.connector import get_db_session
from bakery.schemas.recipe import Recipe
import bakery.services.recipe as recipe_service

router = APIRouter()


@router.post("", response_model=Recipe)
async def create_recipe(
    recipe: Recipe,
    db_session: Session = Depends(get_db_session)
):
    recipe = recipe_service.create_recipe(
        db_session=db_session,
        recipe=recipe
    )

    return Recipe.from_orm(recipe)
