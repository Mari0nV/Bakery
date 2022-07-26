from fastapi import FastAPI
import uvicorn

from bakery.api.routes import ROUTERS

app = FastAPI()

for router_name, router in ROUTERS.items():
    app.include_router(router, prefix=f"/{router_name}", tags=[router_name])


def main():
    uvicorn.run("bakery.main:app", host="0.0.0.0", port=8000)


if __name__ == '__main__':
    main()
