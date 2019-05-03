class Exam():

    def __init__(self, student, japanese, english, math, history, science):
        self.student = student
        self.japanese = japanese
        self.english = english
        self.math = math
        self.history = history
        self.science = science

    def get_student(self):
        return self.student

    def get_japanese(self):
        return self.japanese

    def get_english(self):
        return self.english

    def get_math(self):
        return self.math

    def get_history(self):
        return self.history

    def get_science(self):
        return self.science

    def set_japanese(self, japanese):
        self.japanese = japanese

    def set_english(self, english):
        self.english = english

    def set_math(self, math):
        self.math = math

    def set_history(self, history):
        self.history = history

    def set_science(self, science):
        self.science = science

    # get summary
    def get_literature(self):
        return self.get_japanese() + self.get_english() + self.get_history()

    def get_sciences(self):
        return self.get_math() + self.get_science()

    def get_summary(self):
        return self.get_literature() + get_sciences()
