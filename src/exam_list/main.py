import student
import utility


def show_student(students):

    for std in students:
        print("******************")
        print("student id: ", std.get_student_id())
        print("student name: ", std.get_name())
        print("student wish major: ", std.get_wish_major())
        print("")


def input_wish_major():
    while True:
        major = input("Enter your major[1: Literature, 2: Sciences]: ")

        if major != "1" and major != "2":
            continue

        return major


def import_student():
    students = []
    csv_file = utility.CsvReader("src/exam_list/data/student.csv")
    sdts = csv_file.csv_data

    for num, sdt in enumerate(sdts, start=1):
        sdt_instance = student.Student(num, sdt[0], sdt[1])
        students.append(sdt_instance)

    return students


def registerStudent(add_by_hand=False):

    students = import_student()

    if add_by_hand:
        for i in range(len(students), 3):
            std = student.Student(
                i, input("student name: "), input_wish_major())
            students.append(std)

    return students


def main():

    students = registerStudent()
    show_student(students)


main()
