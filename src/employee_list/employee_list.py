import Employee


class EmployeeList():

    def __init__(self):
        self.emp_list = []

    def get_emp_list(self):
        return self.emp_list

    def show_list(self):
        if(len(self.emp_list) <= 0):
            return

        for i in range(len(self.emp_list)):
            print('{}: {} {} {} {}'.format(
                i, self.emp_list[i].name, self.emp_list[i].phone, self.emp_list[i].home, self.emp_list[i].place)
            )

    def add_emp(self):
        name = input("name: ")
        phone = input("phone: ")
        home = input("home: ")
        place = input("place: ")
        emp = employee.employee(name, place, phone, home)
        self.emp_list.append(emp)

    def delete_emp(self, emp_num):
        del self.emp_list[emp_num]

    def update_emp(self, emp_num):
        self.emp_list[emp_num].set_name(
            input("name [" + self.emp_list[emp_num].get_name() + "]: ")
        )

        self.emp_list[emp_num].set_phone(
            input("phone [" + self.emp_list[emp_num].get_phone() + "]: ")
        )

        self.emp_list[emp_num].set_home(
            input("home [" + self.emp_list[emp_num].get_home() + "]: ")
        )

        self.emp_list[emp_num].set_place(
            input("place [" + self.emp_list[emp_num].get_place() + "]: ")
        )
