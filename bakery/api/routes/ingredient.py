from fastapi import APIRouter, Depends, Response, status
from sqlalchemy.orm import Session

from bakery.database.connector import get_db_session
from bakery.schemas.ingredient import Ingredient, Ingredients
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


@router.get("/{id}", response_model=Ingredient)
async def get_ingredient(
    id: str,
    db_session: Session = Depends(get_db_session)
):
    ingredient = ingredient_service.get_ingredient_by_id(
        db_session=db_session, ingredient_id=id
    )

    return Ingredient.from_orm(ingredient)


@router.get("", response_model=Ingredients)
async def get_all_ingredients(
    db_session: Session = Depends(get_db_session)
):
    ingredients = ingredient_service.get_all_ingredients(
        db_session=db_session
    )

    return Ingredients(ingredients=[Ingredient.from_orm(ingredient) for ingredient in ingredients])


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_ingredient(
    id: str,
    db_session: Session = Depends(get_db_session)
):
    ingredient_service.delete_ingredient(
        db_session=db_session,
        ingredient_id=id
    )

    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.patch("/{id}", response_model=Ingredient)
async def edit_ingredient(
    ingredient: Ingredient,
    db_session: Session = Depends(get_db_session)
):
    ingredient = ingredient_service.edit_ingredient(
        db_session=db_session,
        ingredient=ingredient
    )

    return Ingredient.from_orm(ingredient)
