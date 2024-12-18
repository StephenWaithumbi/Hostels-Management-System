import sys
from models import Hostel, Student

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = 'sqlite:///hostel_database.db'

engine = create_engine(DATABASE_URL)

Session = sessionmaker(bind=engine)
session = Session()

def init_db():
    pass