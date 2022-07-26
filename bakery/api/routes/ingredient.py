from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from bakery.database.connector import get_db_session
from bakery.schemas.ingredient import Ingredient
import bakery.services.ingredient as ingredient_service

router = APIRouter()


@router.post("")
async def create_ingredient(
    ingredient: Ingredient,
    db_session: Session = Depends(get_db_session)
):
    ingredient = ingredient_service.create_ingredient(
        db_session=db_session, ingredient=ingredient
    )

    return Ingredient.from_orm(ingredient)
