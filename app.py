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

def update_hostel():
    hostel_id = int(input("Enter the hostel's ID to update: >> "))
    hostel = session.get(Hostel, hostel_id)
    if not hostel:
        print("Could not find a hostel the id of {hostel_id}")
        return
    hostel.name = input("Enter the new name for hostel '{hostel.name}': >> " or hostel.name)
    hostel.capacity = int(input("Update the number of rooms for hostel '{hostel.name}' >> " or hostel.capacity))
    session.commit()
    print("Hostel Updated successfully.")

