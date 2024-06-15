from student import Students
from fees import Fees


def exit_program():
    print("Goodbye!")
    exit()


def list_students():
    students = Students.view()
    for student in students:
        print(student)


def find_student_by_name():
    name = input("Enter the student's name: ")
    student = Students.search(name)
    print(student) if student else print(f"{name} not found")


def find_student_by_id():
    id = input("Enter the student's id: ")
    student = Students.search(id)
    print(student) if student else print(f"Student with {id} was not found.")


def create_student():
    name=input("Enter student's full name: ")
    fname = input("Enter student's first name: ")
    mname = input("Enter student's middle name: ")
    address = input("Enter student's address: ")
    mobno = input("Enter student's mobile number: ")
    email = input("Enter student's email: ")
    dob = input("Enter student's date of birth: ")
    gender = input("Enter student's gender: ")
    try:
        student = Students.create(name,fname, mname,address,mobno,email,dob,gender)
        print(f"Newly added,{student}")
    except Exception as exc:
        print("Error creating student: ", exc)


def update_student():
    id = input("Enter the student's id: ")
    if student := Students.search(id):
        try:
            name=input("Enter student's full name: ")
            student.name=name
            fname = input("Enter the student's name: ")
            student.fname = fname
            mname = input("Enter the student's new middle name: ")
            student.mname = mname
            address = input("Enter the student's new addrress: ")
            student.address = address
            mobno = input("Enter the student's new mobile number: ")
            student.mobno = mobno
            email = input("Enter the student's new email address: ")
            student.email = email
            dob = input("Enter the student's new date of birth: ")
            student.dob = dob
            gender = input("Enter the student's new gender: ")
            student.gender = gender

            student.update()
            print(f"Successfully updated!")
        except Exception as exc:
            print(f"Error updating the department.", exc)
    else:
        print(f"Student was not found.Please check the student id.")


def delete_student():
    id = input("Enter the student's id: ")
    if student := Students.search(id):
        student.delete()
        print(f"The student was successfully deleted from the database")
    else:
        print(f"Student was not found.Please check the id.")

def list_fees():
    fees = Fees.view()
    for fee in fees:
        print(fee)


def find_fee_by_name():
    name = input("Enter the student's name: ")
    fee = Students.search(name)
    print(fee) if fee else print(f"{name} not found")


def find_fee_by_id():
    id = input("Enter the student's id: ")
    fee = Fees.search(id)
    print(fee) if fee else print(f"Student with {id} was not found.")


def create_fee():

    fname = input("Enter student's first name: ")
    mname = input("Enter student's middle name: ")
    try:
        fee= Students.create(fname, mname)
        print(f"Newly added,{fee}")
    except Exception as exc:
        print("Error creating student: ", exc)


def update_student():
    id = input("Enter the student's id: ")
    if student := Students.search(id):
        try:
            fname = input("Enter the student's name: ")
            student.fname = fname
            mname = input("Enter the student's new middle name: ")
            student.mname = mname
            address = input("Enter the student's new addrress: ")
            student.address = address
            mobno = input("Enter the student's new mobile number: ")
            student.mobno = mobno
            email = input("Enter the student's new email address: ")
            student.email = email
            dob = input("Enter the student's new date of birth: ")
            student.dob = dob
            gender = input("Enter the student's new gender: ")
            student.gender = gender

            student.update()
            print(f"Successfully updated!")
        except Exception as exc:
            print(f"Error updating the department.", exc)
    else:
        print(f"Student was not found.Please check the student id.")


def delete_student():
    id = input("Enter the student's id: ")
    if student := Students.search(id):
        student.delete()
        print(f"The student was successfully deleted from the database")
    else:
        print(f"Student was not found.Please check the id.")
