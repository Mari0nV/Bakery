from bakery.api.errors import ApiException


class IngredientAlreadyExisting(ApiException):
    def __init__(self, ingredient_id: str):
        super().__init__(
            409,
            {
                "message": f"Ingredient with ID '{ingredient_id}' already exists in database.",
                "ingredient_id": ingredient_id            }
        )


class IngredientNotFound(ApiException):
    def __init__(self, ingredient_id: str):
        super().__init__(
            404,
            {
                "message": f"Ingredient with ID '{ingredient_id}' does not exist in database.",
                "ingredient_id": ingredient_id
            }
        )
