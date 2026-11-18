def display_menu():
    print("\n Welcome Student Mangaement System")
    print("1. Add Student")
    print("2. View Student")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Search Student")
    print("6. Exit")
students = {}

def add_student():
    Roll_no = input("Enter Roll Number : ").strip()
    if not Roll_no.isdigit():
        print("Roll number must contain only digits!")
        return
    else:
        if Roll_no in students:
            print("Already exists")
            return
        else:
            print("Continue adding student...")
            name = input("Enter student name:  ")
            age = input("Enter student age: ")
            students[Roll_no]={"name" : name,
                            "age" : age}
            print("Student addedd Successfully") 
            save_students()

def view_students():
    if not students:
        print("No student found")
    else:
        for Roll_no, details in students.items():
            print("\nRoll_num: ", Roll_no)
            print("Name : ", details["name"])
            print("Age: ", details["age"])

def search_student():
    Roll_num = input("Enter Roll num: ").strip()
    if not Roll_num.isdigit():
        print("Roll number must contain only digits!")
        return
    else:

        if Roll_num not in students:
            print("Roll_num Does'nt exists")
            return 
        else:
            details = students[Roll_num]

            print("\nRoll_no: ", Roll_num)
            print("Name: ", details["name"])
            print("Age: ", details["age"])

def update_student():
    Roll_no = input("Enter Roll num: ").strip()
    if not Roll_no.isdigit():
        print("Roll number must contain only digits!")
        return
    else:    
        if Roll_no not in students:
            print("Student not found")
            return
        else:
            name = input("Enter new name: ")
            age = input("Enter new age: ")
            students[Roll_no]["name"]= name
            students[Roll_no]["age"]= age 
            print("Update Successful")
            save_students()

def delete_student():
    Roll_no = input("Enter Roll num: ").strip()
    if not Roll_no.isdigit():
        print("Roll number must contain only digits!")
        return
    else:
        if Roll_no not in students:
            print("Student not found")
        else:
            students.pop(Roll_no)
            print("Student data deleted successfully")
            save_students()

import json
import os
print("JSON file location:", os.path.abspath("data.json"))

def save_students():
    with open("data.json", "w") as file:
        json.dump(students, file, indent=4)
def load_students():
    global students

    if os.path.exists("data.json"):
        with open("data.json", "r") as file:
            students = json.load(file)

load_students()
    

while True:
    display_menu()
    choice = input("Enter your choice (1-6): ")

    if choice == '1':
        add_student()
    elif choice == '2':
        view_students()
    elif choice == '3':
        update_student()
    elif choice == '4':
        delete_student()
    elif choice == '5':
        search_student()
    elif choice == '6':
        print("Exiting the Student Management System. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")