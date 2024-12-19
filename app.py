import sys
from models import Hostel, Student, Base

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///hostel_database.db')

Session = sessionmaker(bind=engine)
session = Session()

def init_db():
    #iniializes the db
    Base.metadata.create_all(engine)
    print("Hostel Database initialized...")

def create_hostel():
    #create a new hostel in the data base
    name = input("Enter hostel name: >> ")
    capacity = int(input("Enter the number rooms >> "))
    hostel = Hostel(name=name, capacity=capacity)
    session.add(hostel)
    session.commit()
    print(f"Hostel '{name}' created successfully")

