from contextlib import asynccontextmanager
from fastapi import FastAPI 
from database import create_table
from routes.reviews import router as review_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    create_table()
    print("Data Base is Created")
    yield
    print("Shutting down the app")

app = FastAPI(
    title="Rangmanch Review API",
    description="Theatre Review API for pune Rangmanch",
    lifespan=lifespan
)

app.include_router(review_router)

@app.get("/")
def root():
    return {
        "message": "Welcome To Rangmanch review APP"
    }
