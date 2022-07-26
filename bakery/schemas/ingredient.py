from pydantic import BaseModel

from typing import Optional


class Ingredient(BaseModel):
    id: str
    name: Optional[str]
    price: Optional[float]

    class Config:
        orm_mode = True
