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

def update_student():
    student_id = int(input("Enter students id to update: >> "))
    student = session.get(Student, student_id)
    if not student:
        print(f"The Student with id {student_id} does not exist")
        return
    student.name = input("Enter new name: >> ") or student.name
    student.reg_no = int(input("Enter new reg no: >> ")) or student.reg_no
    new_hostel_id = int(input("Enter student's new hostel: >> ")) or student.hostel_id
    if new_hostel_id:
        new_hostel = session.get(Hostel, new_hostel_id)
        if not new_hostel:
            print(f"Hostel with id '{new_hostel_id}' does not exist!")            
        else:
            student.hostel_id = new_hostel_id
    session.commit()
    print(f"Student with id {student_id} was updated successfully!")

def delete_student():
    student_id = int(input("Enter the id for student to be deleted: >> "))
    student = session.get(Student, student_id)
    if not student:
        print(f"Could not find student with id {student_id}")
        return
    session.delete(student)
    session.commit()
    print(f"Student with Id of {student_id} was deleted successfully")

def list_hostels():
    hostels = session.query(Hostel).all()
    if not hostels:
        print("Not hostels found")
        for hostel in hostels:
            print(hostel)

def list_students():
    students = session.query(Student).all()
    if not students:
        print("No students found! ")
    for student in students:
        print(student)
    
def view_student_by_hostel():
      hostel_id = int(input("Enter Hostel id"))
      hostel = session.get(Hostel, hostel_id)
      if not hostel:
          print(f"Hostel with id '{hostel_id}' was not found")
          return
      students = hostel.students
      if not students:
          print(f"No student found with!")
          return
      print(f"Students in {hostel.name} hostel are...")
      for student in students:
          print(student)

