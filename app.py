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

def create_student():
    name = input("Enter Student's name: >> ")
    reg_no = int(input("Enter students reg no: >> "))
    hostel_id = int(input("Enter Student's hostel: >> "))
    hostel = session.get(Hostel, hostel_id)
    if not hostel:
        print(f"Sorry hostel with Id {hostel.id} doesnot exist")
        return
    student = Student(name=name, reg_no=reg_no, hostel_id=hostel_id)
    session.add(student)
    session.commit()
    print(f"Student '{name}' was created successfully!!'")

