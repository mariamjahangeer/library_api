from sqlalchemy import Column, Integer, ForeignKey
from app.database.database import Base

class Borrow(Base):
    __tablename__ = "borrow"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    book_id = Column(Integer, ForeignKey("books.id"))
