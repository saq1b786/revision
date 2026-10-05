from sqlalchemy import Column, Integer, String, Boolean, Float, ForeignKey
from sqlalchemy.orm import DeclarativeBase, sessionmaker
from sqlalchemy import create_engine

class Base(DeclarativeBase): 
    pass 

engine = create_engine("sqlite:///teamsheet.db")
SessionLocal = sessionmaker(bind=engine)

class Player(Base): 
    __tablename__ = 'players'

    id = Column(Integer, primary_key=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    phone_number = Column(String, nullable=False)
    hash_password = Column(String, nullable=False)
    is_admin = Column(Boolean, default=False)
    tallies = Column(Integer, default=0)
    consecutive_clean_weeks = Column(Integer, default=0)

    
