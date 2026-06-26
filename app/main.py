from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes.category import router as category_router

app = FastAPI(title="Category Management System API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include clean modular routes
app.include_router(category_router)