from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, DateTime, Integer, Float, ForeignKey, String

from bakery.database.connector import ENGINE


Base = declarative_base()


class Recipe(Base):
    __tablename__ = 'recipe'
    id = Column(String, primary_key=True)
    name = Column(String)

    ingredients = relationship(
        "RecipeIngredient", cascade="all,delete"
    )


class RecipeIngredient(Base):
    __tablename__ = "recipe_ingredient"
    recipe_id = Column(String, ForeignKey("recipe.id"), primary_key=True)
    ingredient_id = Column(String, ForeignKey("ingredient.id"), primary_key=True)
    quantity = Column(Integer)  # grams


class Ingredient(Base):
    __tablename__ = 'ingredient'
    id = Column(String, primary_key=True)
    name = Column(String)
    price = Column(Float)  # kilograms


class Order(Base):
    __tablename__ = "order"
    id = Column(Integer, primary_key=True, autoincrement=True)
    recipe_id = Column(String, ForeignKey("recipe.id"))
    quantity = Column(Integer)  # per person
    client_name = Column(String)
    client_address = Column(String)
    price = Column(Float)
    date = Column(DateTime)


class Hello(Base):
    __tablename__ = 'hello'
    name = Column(String, primary_key=True)


def configure_db():
    Base.metadata.create_all(ENGINE.engine)


if __name__ == '__main__':
    configure_db()
