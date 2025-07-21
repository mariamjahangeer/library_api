from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    print(" API root hit!")  # Log
    return {"message": "Welcome to the Library System API"}
