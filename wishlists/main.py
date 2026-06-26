from routes.wishlist_routes import router as wishlist_router
from fastapi import FastAPI


app = FastAPI()

app.include_router(wishlist_router)