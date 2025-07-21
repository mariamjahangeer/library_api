from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from app.database.database import SessionLocal
from app.models import book as models
from app.schemas import book as schemas

router = APIRouter(
    prefix="/books",
    tags=["Books"]
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", status_code=status.HTTP_201_CREATED)
def create_book(request: schemas.BookCreate, db: Session = Depends(get_db)):
    new_book = models.Book(title=request.title, author=request.author)
    db.add(new_book)
    db.commit()
    db.refresh(new_book)
    print(f" Book created: {new_book.title} by {new_book.author}")  # Log
    return new_book
