import json
import os
students = {}

def load_students():
    global students
    students = {}
# Loads the data.json file for managing student details
    if os.path.exists("data.json"):
        try:
            with open("data.json", "r") as file:
                data = json.load(file)
                if not isinstance(data, dict):
                    print("Invalid student database format")
                    return
                valid_dict = {}
                skipped = 0
                for roll_no, details in data.items():
                    if not roll_no.isdigit():
                        print("Roll no is not valid")
                        skipped += 1
                        continue
                    if not isinstance(details, dict):
                        print("Invalid student record")
                        skipped += 1
                        continue
                    if "name" not in details or "age" not in details :
                        print("Student name or age is missing")
                        skipped += 1
                        continue
                    if not isinstance(details["age"], int) or isinstance(details["age"], bool) or details["age"]<= 0:
                        print("Age is not valid ")
                        skipped += 1
                        continue
                    if not isinstance(details["name"], str) or details["name"].strip() == "":
                        print("Name is not valid")
                        skipped += 1
                        continue  
                    valid_dict[roll_no] = details
                    
                students = valid_dict
                print(f"{len(students)} students loaded successfully")
                print(f"{skipped} invalid entries skipped")
        except json.JSONDecodeError:
            print("The JSON contains invalid entries")
        except PermissionError:
            print("Permission to file is denied")
        except OSError as e:
            print("File operation failed:", e)

def save_students():
    # Saves the current record to data.json
    try:
        with open("data.json" , "w")as file:
            json.dump(students ,file , indent=4)
    except PermissionError:
        print("Permission denied: Cannot save student data")
    except OSError as e:
        print("File operation failed:" , e)

load_students()

def display_menu():
    print("\n Welcome to Student Management System")
    print("1. Add Student")
    print("2. View Student")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Search Student")
    print("6. Exit")

# Validate's the student's age
def get_valid_age():
    while True:
        age = input("Enter age: ")
        
        if not age.isdigit():
            print("It's invalid")
            continue
        
        age = int(age)
        if age <= 0:
            print("Zero is not valid")
            continue
        return age

# Validate's the student's name
def get_valid_name():
    while True:
        name = input("Enter Name: ")
        f = name.strip()

        if f == "":
            print("Name shouldn't be empty")
            continue

        if not f.replace(" ", "").isalpha():
            print("Invalid name")
            continue

        return f
    
def add_student():
    roll_no = input("Enter Roll Number : ").strip()
    if not roll_no.isdigit():
        print("Roll number must contain only digits!")
        return
    if roll_no in students:
        print("Already exists")
        return
    name = get_valid_name()
    age = get_valid_age()
    students[roll_no]={"name" : name,
                        "age" : age}
    print("Student added successfully") 
    save_students()

def view_students():
    if not students:
        print("No student found")
        return
    for roll_no, details in students.items():
        print("\nroll_no: ", roll_no)
        print("Name : ", details["name"])
        print("Age: ", details["age"])

def search_student():
    roll_no = input("Enter Roll num: ").strip()
    if not roll_no.isdigit():
        print("Roll number must contain only digits!")
        return

    if roll_no not in students:
        print("Roll number doesn't exists")
        return 

    details = students[roll_no]

    print("\nroll_no: ", roll_no)
    print("Name: ", details["name"])
    print("Age: ", details["age"])

def update_student():
    roll_no = input("Enter Roll no: ").strip()
    if not roll_no.isdigit():
        print("Roll number must contain only digits!")
        return 
    if roll_no not in students:
        print("Student not found")
        return
    
    name = get_valid_name()
    age = get_valid_age()
    students[roll_no]["name"]= name
    students[roll_no]["age"]= age 
    print("Update Successful")
    save_students()

def delete_student():
    roll_no = input("Enter Roll num: ").strip()
    if not roll_no.isdigit():
        print("Roll number must contain only digits!")
        return
    if roll_no not in students:
        print("Student not found")
        return
    students.pop(roll_no)
    print("Student data deleted successfully")
    save_students()
    

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