from fastapi import FastAPI
from auth_routes import auth_router
from order_routes import order_router #Might make more sense to put routers in separate files and import from there
from fastapi_jwt_auth import AuthJWT
from schemas import Settings



app = FastAPI()

@AuthJWT.load_config
def get_config():
    return Settings()

app.include_router(auth_router)
app.include_router(order_router)