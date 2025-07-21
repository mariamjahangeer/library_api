from fastapi import FastAPI
from app.routers import book

app = FastAPI()

app.include_router(book.router)

@app.get("/")
def root():
    print(" API root hit!")  # Log
    return {"message": "Welcome to the Library System API"}

