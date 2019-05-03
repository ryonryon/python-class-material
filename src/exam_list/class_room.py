class ClassRoom():
    def __init__(self, major):
        self.class_member = []
        self.class_major = major

    def show_class_member(self):
        pass

    def add_member(self, student):
        self.class_member.append(student)
