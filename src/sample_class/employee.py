
class Employee():

    def __init__(self, id, name):
        self.__id = id
        self.__name = name

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def work(self):
        print("I am {} working".format(self.__name))


ryo_emp = Employee(10, "ryo")

print(ryo_emp.work())
