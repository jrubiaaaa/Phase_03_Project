from helpers import (
    exit_program,
    list_students,
    find_student_by_name,
    find_student_by_id,
    create_student,
    update_student,
    delete_student,
)

def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            list_students()
        elif choice == "2":
            find_student_by_name()
        elif choice == "3":
            find_student_by_id()
        elif choice == "4":
            create_student()
        elif choice == "5":
            update_student()
        elif choice == "6":
            delete_student()

def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. List all students")
    print("2. Find student by name")
    print("3. Find student by id")
    print("4: Create student")
    print("5: Update student")
    print("6: Delete student")

if __name__=="__main__":
    main()