
class employee():
    def __init__(self, name, place, phone="", home=""):
        self.name = name
        self.phone = phone
        self.home = home
        self.place = place

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_phone(self):
        return self.phone

    def set_phone(self, phone):
        self.phone = phone

    def get_home(self):
        return self.home

    def set_home(self, home):
        self.home = home

    def get_place(self):
        return self.place

    def set_place(self, place):
        self.place = place
