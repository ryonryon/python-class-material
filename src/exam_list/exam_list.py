import src.exam_list.exam


class exam_list():

    def __init__(self):
        self.exams = []

    def show_list(self):

        for i, result in enumerate(self.exams, start=0):
            print('{} (Name: {} Result: {} Literature:{} Sciences:{})'.format(
                i, result.get_student().get_name(), result.get_summary(), result.get_literature(), result.get_sciences()))

    def add_exam(self, exam_result):
        self.exams.append(exam_result)

    def delete_exam(self, index_num):
        del self.exams[index_num]

    def update_exam(self, index_num):
        self.exams[index_num].set_japanese(
            input("japanese (" + self.exams[index_num].get_japanese() + "): ")
        )
        self.exams[index_num].set_english(
            input("english (" + self.exams[index_num].get_english() + "): ")
        )
        self.exams[index_num].set_math(
            input("math (" + self.exams[index_num].get_math() + "): ")
        )
        self.exams[index_num].set_history(
            input("history (" + self.exams[index_num].get_history() + "): ")
        )
        self.exams[index_num].set_science(
            input("science (" + self.exams[index_num].get_science() + "): ")
        )
