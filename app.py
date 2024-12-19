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
    name = input("\nEnter hostel name: >> ")
    capacity = int(input("Enter the number rooms >> "))
    hostel = Hostel(name=name, capacity=capacity)
    session.add(hostel)
    session.commit()
    print(f"Hostel '{name}' created was successfully")

def update_hostel():
    hostel_id = int(input("Enter the hostel's ID to update: >> "))
    hostel = session.get(Hostel, hostel_id)
    if not hostel:
        print(f"Could not find a hostel the id of {hostel_id}")
        return
    hostel.name = input(f"Enter the new name for hostel '{hostel.name}': >> " )
    capacity = input("Update the number of students for '{hostel.name}' Currently: '{hostel.capacity}' >> ")  or hostel.capacity
    hostel.capacity = int(capacity) if capacity else hostel.capacity
    session.commit()
    print("Hostel Updated successfully.")

def create_student():
    name = input("Enter Student's name: >> ")
    reg_no = int(input("Enter student's registration number: >> "))
    
    while True:
        hostel_id = int(input("Enter Student's hostel ID: >> "))
        hostel = session.get(Hostel, hostel_id)
        if hostel:
            break
        print(f"Sorry, hostel with ID {hostel_id} does not exist. Please try again.")

    student = Student(name=name, reg_no=reg_no, hostel_id=hostel_id)
    session.add(student)
    session.commit()
    print(f"Student '{name}' was created successfully!")    

def update_student():
    while True:
        student_id = int(input("Enter the student's ID to update: >> "))
        student = session.get(Student, student_id)
        if student:
            break
        print(f"The student with ID {student_id} does not exist. Please try again.")

    student.name = input(f"Enter new name for '{student.name}' (press Enter to keep current): >> ") or student.name
    reg_no = inp~ut(f"Enter new registration number for '{student.reg_no}' (press Enter to keep current): >> ")
    student.reg_no = int(reg_no) if reg_no else student.reg_no

    while True:
        new_hostel_id = input(f"Enter student's new hostel ID (press Enter to keep current: {student.hostel_id}): >> ")
        if not new_hostel_id: 
            break
        new_hostel_id = int(new_hostel_id)
        new_hostel = session.get(Hostel, new_hostel_id)
        if new_hostel:
            student.hostel_id = new_hostel_id
            break
        print(f"Hostel with ID {new_hostel_id} does not exist. Please try again.")

    session.commit()
    print(f"Student with ID {student_id} was updated successfully!")


def delete_student():
    student_id = int(input("Enter the id for student to be deleted: >> "))
    student = session.get(Student, student_id)
    if not student:
        print(f"Could not find student with id {student_id}")
        return
    confirm = input(f"Are you sure you want to delete student '{student.name}'? (y/n): ")
    if confirm != 'y':
        print("Operation cancelled.")
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
      hostel_id = int(input("Enter Hostel id: >> "))
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

def menu():
    print("\nWelcome >>>>")
    print("1. Create Hostel")
    print("2. Update Hostel")
    print("3. Register Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. View Hostels")
    print("7. View all students")
    print("8. View students from specific Hostel")
    print("9. Exit")

    while True:        
        user_input = input("Enter Your choice >> ")

        if user_input == '1':
            create_hostel()
        elif user_input == '2':
            update_hostel()
        elif user_input == '3':
            create_student()
        elif user_input == '4':
            update_student()
        elif user_input == '5':
            delete_student()
        elif user_input == '6':
            list_hostels()
        elif user_input == '7':
            list_students()
        elif user_input == '8':
            view_student_by_hostel()
        elif user_input == '9':
            print("Thanks for using the application")
            sys.exit()
        else:
            print("Ivalid Choice. Please select a valid choice")

if __name__ == '__main__':
    init_db()
    menu()
        
                      