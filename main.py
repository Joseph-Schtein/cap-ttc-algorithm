from course import Course
from student import Student


def create_matrix(dic_list, course_list, row_number, column_number):
    list_of_name = ["" for i in range(row_number)]
    list_of_ranking = [0 for i in range(row_number * column_number)]
    counter1 = 0
    counter2 = 0
    for i in range(row_number):
        for j in range(column_number):
            if j % row_number == 0:
                list_of_name[counter1] = list(dic_list[i][j].values())[0]

            list_of_ranking[counter2] = list(dic_list[i][j].values())[2]
            counter2 += 1

        counter1 += 1

    counter = 0
    course_price = {}
    for i in range(row_number):
        student_bidding = {}
        for j in range(column_number):
            student_bidding[course_list[j]] = list_of_ranking[counter]
            counter += 1

        course_price[list_of_name[i]] = student_bidding

    return course_price


def create_students(fixed):
    student_name_list = list(fixed.keys())
    student_rank = list(fixed.values())
    student_list = []
    for i in range(len(fixed)):
        stu = Student(student_name_list[i], student_rank[i])
        student_list.append(stu)

    return student_list


def create_courses(fixed):
    tmp = list(fixed.values())
    courses_name_list = list(tmp.keys())
    course_list = []
    for i in range(len(courses_name_list)):
        cou = Course(courses_name_list[i], 5, 4)
        course_list.append(cou)

    return course_list


def algorithm(rank, number_of_rounds):
    i = 1


def main():
    courses = ["a", "b", "c", "d"]
    ranking = [[{'name': 'Joseph Stein', 'course name': 'a', 'rank': 150},
                {'name': 'Joseph Stein', 'course name': 'b', 'rank': 50},
                {'name': 'Joseph Stein', 'course name': 'c', 'rank': 200},
                {'name': 'Joseph Stein', 'course name': 'd', 'rank': 100}],
               [{'name': 'Itay Simchayov', 'course name': 'a', 'rank': 110},
                {'name': 'Itay Simchayov', 'course name': 'b', 'rank': 120},
                {'name': 'Itay Simchayov', 'course name': 'c', 'rank': 140},
                {'name': 'Itay Simchayov', 'course name': 'd', 'rank': 130}],
               [{'name': 'Lihi Belfer', 'course name': 'a', 'rank': 250},
                {'name': 'Lihi Belfer', 'course name': 'b', 'rank': 130},
                {'name': 'Lihi Belfer', 'course name': 'c', 'rank': 70},
                {'name': 'Lihi Belfer', 'course name': 'd', 'rank': 50}]]

    row_number = len(ranking)
    column_number = len(ranking[0])
    fixed = create_matrix(ranking, courses, row_number, column_number)
    student_list = create_students(fixed)
    course_list = create_courses(fixed)


if __name__ == '__main__':
    main()
