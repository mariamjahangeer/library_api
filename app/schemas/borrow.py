from pydantic import BaseModel

class BorrowCreate(BaseModel):
    user_id: int
    book_id: int
