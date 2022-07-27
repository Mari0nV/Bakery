from bakery.api.routes.ingredient import router as ingredient_router
from bakery.api.routes.hello import router as hello_router
from bakery.api.routes.recipe import router as recipe_router


ROUTERS = {
    "ingredients": ingredient_router,
    "hello": hello_router,
    "recipe": recipe_router
}
