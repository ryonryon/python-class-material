import employee
import employee_list


def show_employee_list(emp_list):
    emp_list.show_list()


def add_employee(emp_list):
    emp_list.add_emp()
    print("the employee is successfully added!\n")


def delete_employee(emp_list):
    while True:

        emp_list.show_list()
        emp_num = int(input("Enter the number you want to delete: "))

        if 0 <= emp_num and emp_num < len(emp_list.get_emp_list()):
            emp_list.delete_emp(emp_num)
            break

        print("Enter the valid number!")


def update_employee(emp_list):
    while True:

        emp_list.show_list()
        emp_num = int(input("Enter the number you want to update: "))

        if 0 <= emp_num and emp_num < len(emp_list.get_emp_list()):
            emp_list.update_emp(emp_num)
            print("Successfully updated!")
            break

        print("Enter the valid number!")


def main_menu():
    emp_list = employee_list.employee_list()

    while True:
        print("*==================================*")
        print("* 1. show employee list            *")
        print("* 2. add employee                  *")
        print("* 3. update employee               *")
        print("* 4. delete employee               *")
        print("* 5. quit app                      *")
        print("*==================================*")

        menu = input("Enter the number: ")
        if menu == "1":
            show_employee_list(emp_list)
        elif menu == "2":
            add_employee(emp_list)
        elif menu == "3":
            update_employee(emp_list)
        elif menu == "4":
            delete_employee(emp_list)
        elif menu == "5":
            print("See you")
            break
        else:
            print("Enter the number again!\n")


main_menu()
