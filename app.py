import sys, os
from models import Hostel, Student, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from colorama import Fore, init


init(autoreset=True)

engine = create_engine('sqlite:///hostel_database.db')
Session = sessionmaker(bind=engine)
session = Session()

def clear_screen():
    os.system("clear")

def print_border(char='-', length=50):
    print(Fore.CYAN + char * length)

def print_centered(text, width=50):
    print(Fore.GREEN + text.center(width))

def init_db():
    Base.metadata.create_all(engine)
    print(Fore.YELLOW + "Hostel Database initialized...")

def create_hostel():
    clear_screen()
    print_centered("Create Hostel")
    print_border()
    name = input(Fore.CYAN + "\nEnter hostel name: >> ")
    capacity = int(input("Enter the number of rooms: >> "))
    hostel = Hostel(name=name, capacity=capacity)
    session.add(hostel)
    session.commit()
    print(Fore.GREEN + f"Hostel '{name}' created successfully")

def update_hostel():
    clear_screen()
    print_centered("Update Hostel")
    print_border()
    hostel_id = int(input("Enter the hostel's ID to update: >> "))
    hostel = session.get(Hostel, hostel_id)
    while not hostel:
        print(Fore.RED + f"Could not find a hostel with ID {hostel_id}")
        hostel_id = int(input("Enter a valid hostel ID: >> "))
        hostel = session.get(Hostel, hostel_id)
    print(Fore.YELLOW + f"Current Name: {hostel.name}, Capacity: {hostel.capacity}")
    hostel.name = input(f"Enter new name for '{hostel.name}' (Leave blank to keep current): >> ") or hostel.name
    capacity = input(f"Update capacity for '{hostel.name}' (Leave blank to keep {hostel.capacity}): >> ")
    hostel.capacity = int(capacity) if capacity else hostel.capacity
    session.commit()
    print(Fore.GREEN + f"Hostel '{hostel.name}' updated successfully.")

def create_student():
    clear_screen()
    print_centered("Register Student")
    print_border()
    name = input("Enter student's name: >> ")
    reg_no = int(input("Enter student's reg no: >> "))
    hostel_id = int(input("Enter student's hostel ID: >> "))
    hostel = session.get(Hostel, hostel_id)
    while not hostel:
        print(Fore.RED + f"Hostel with ID {hostel_id} does not exist.")
        hostel_id = int(input("Enter a valid hostel ID: >> "))
        hostel = session.get(Hostel, hostel_id)
    student = Student(name=name, reg_no=reg_no, hostel_id=hostel_id)
    session.add(student)
    session.commit()
    print(Fore.GREEN + f"Student '{name}' registered successfully.")

def update_student():
    clear_screen()
    print_centered("Update Student")
    print_border()
    student_id = int(input("Enter student's ID to update: >> "))
    student = session.get(Student, student_id)
    while not student:
        print(Fore.RED + f"Student with ID {student_id} does not exist.")
        student_id = int(input("Enter a valid student ID: >> "))
        student = session.get(Student, student_id)
    print(Fore.YELLOW + f"Current Name: {student.name}, Reg No: {student.reg_no}, Hostel ID: {student.hostel_id}")
    student.name = input("Enter new name (Leave blank to keep current): >> ") or student.name
    student.reg_no = int(input("Enter new reg no (Leave blank to keep current): >> ") or student.reg_no)
    new_hostel_id = int(input("Enter new hostel ID (Leave blank to keep current): >> ") or student.hostel_id)
    new_hostel = session.get(Hostel, new_hostel_id) if new_hostel_id else None
    if new_hostel_id and not new_hostel:
        print(Fore.RED + f"Hostel with ID {new_hostel_id} does not exist. Keeping current hostel.")
    else:
        student.hostel_id = new_hostel_id
    session.commit()
    print(Fore.GREEN + f"Student '{student.name}' updated successfully.")

def delete_student():
    clear_screen()
    print_centered("Delete Student")
    print_border()
    student_id = int(input("Enter the ID of the student to delete: >> "))
    student = session.get(Student, student_id)
    if not student:
        print(Fore.RED + f"No student found with ID {student_id}")
        return
    confirm = input(Fore.YELLOW + f"Are you sure you want to delete '{student.name}'? (y/n): >> ")
    if confirm.lower() != 'y':
        print(Fore.RED + "Operation cancelled.")
        return
    session.delete(student)
    session.commit()
    print(Fore.GREEN + f"Student '{student.name}' deleted successfully.")

def list_hostels():
    clear_screen()
    print_centered("Hostel List")
    print_border()
    hostels = session.query(Hostel).all()
    if not hostels:
        print(Fore.RED + "No hostels found.")
        return
    for hostel in hostels:
        print(Fore.CYAN + f"ID: {hostel.id}, Name: {hostel.name}, Capacity: {hostel.capacity}")

def list_students():
    clear_screen()
    print_centered("Student List")
    print_border()
    students = session.query(Student).all()
    if not students:
        print(Fore.RED + "No students found.")
        return
    for student in students:
        print(Fore.CYAN + f"ID: {student.id}, Name: {student.name}, Reg No: {student.reg_no}, Hostel ID: {student.hostel_id}")

def view_student_by_hostel():
    clear_screen()
    print_centered("View Students by Hostel")
    print_border()
    hostel_id = int(input("Enter hostel ID: >> "))
    hostel = session.get(Hostel, hostel_id)
    if not hostel:
        print(Fore.RED + f"No hostel found with ID {hostel_id}.")
        return
    students = hostel.students
    if not students:
        print(Fore.YELLOW + f"No students found in hostel '{hostel.name}'.")
        return
    print(Fore.GREEN + f"Students in hostel '{hostel.name}':")
    for student in students:
        print(Fore.CYAN + f"ID: {student.id}, Name: {student.name}, Reg No: {student.reg_no}")

def menu():
    clear_screen()
    while True:
        print_border('=')
        print_centered("Welcome to my app 😊")
        print_border('=')
        print("\n1. Create Hostel")
        print("2. Update Hostel")
        print("3. Register Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. View Hostels")
        print("7. View All Students")
        print("8. View Students by Hostel")
        print("9. Exit")
        print_border('=')
        user_input = input(Fore.CYAN + "Enter your choice: >> ")

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
            print(Fore.GREEN + "Thanks for using the application.")
            sys.exit()

if __name__ == '__main__':
    init_db()
    menu()
