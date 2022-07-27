from bakery.api.errors import ApiException


class RecipeAlreadyExisting(ApiException):
    def __init__(self, recipe_id: str):
        super().__init__(
            409,
            {
                "message": f"Recipe with ID '{recipe_id}' already exists in database.",
                "recipe_id": recipe_id            }
        )
