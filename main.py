from copy import deepcopy

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


def create_students(fixed, course_names):
    student_name_list = list(fixed.keys())
    student_rank = list(fixed.values())
    student_list = []
    course_take = {}
    for i in range(len(course_names)):
        course_take[course_names[i]] = 0

    for i in range(len(fixed)):
        course_tmp = deepcopy(course_take)
        stu = Student(student_name_list[i], student_rank[i], course_tmp)
        student_list.append(stu)

    return student_list


def create_courses(fixed):
    tmp = list(fixed.values())
    courses_name_list = list(tmp[0].keys())
    course_list = []
    for i in range(len(courses_name_list)):
        if i == 0:
            cou = Course(courses_name_list[i], 3, 2, ["c"])
            course_list.append(cou)

        elif i == 2:
            cou = Course(courses_name_list[i], 3, 2, ["a"])
            course_list.append(cou)

        else:
            cou = Course(courses_name_list[i], 3, 2, [])
            course_list.append(cou)

    return course_list


def check_overlap(student_object, course_object):
    overlap_courses = course_object.get_overlap_list()
    if len(overlap_courses) > 0:
        output = True
        enroll_status = student_object.get_enrolment_status()
        for overlap in range(len(overlap_courses)):
            course_name = overlap_courses[overlap]
            check = enroll_status[course_name]
            if check == 1:
                student_object.get_next_preference(course_object.get_name())
                if output:
                    output = False

        return output

    else:
        return True


def ready_to_new_round(student_names, ranks):
    _data = {}
    for i in range(len(ranks)):
        course_names = list(ranks[i].keys())
        vector_rank = list(ranks[i].values())
        index = vector_rank.index(max(vector_rank))
        _data[student_names[i]] = {course_names[index]: vector_rank[index]}

    return _data


def second_phase(_data, student_list, course_list):
    max_enrolled = 0
    for index in range(len(student_list)):
        if max_enrolled < student_list[index].get_number_of_enrollments():
            max_enrolled = student_list[index].get_number_of_enrollments()

    tmp_student_list = []
    tmp_data = {}
    _data_value = list(_data.values())
    _data_keys = list(_data.keys())
    for stu in range(len(student_list)):
        if student_list[stu].get_number_of_enrollments() < max_enrolled:
            tmp_student_list.append(student_list[stu])
            tmp_data[_data_keys[stu]] = _data_value[stu]
    if len(tmp_student_list) > 0:
        enroll_students(tmp_data, tmp_student_list, course_list)


def there_is_a_tie(student_object):
    start_end = [0 for i in range(len(student_object))]
    counter = 0
    same = False
    for index in range(len(student_object)-1):
        if student_object[index].get_current_highest_bid() == student_object[index+1].get_current_highest_bid() and not same:
            start_end[counter] = index
            counter += 1
            same = True

        elif student_object[index].get_current_highest_bid() != student_object[index+1].get_current_highest_bid() and same:
            start_end[counter] = index
            counter += 1
            same = False

    if len(start_end) % 2 == 0:
        start_end[counter] = len(student_object) - 1

    return start_end


def enroll_students(_data, student_list, course_list):
    amount_of_bidrs = {'a': [], 'b': [], 'c': [], 'd': []}
    student_element = {'a': [], 'b': [], 'c': [], 'd': []}
    course_bid = list(_data.values())
    for i in range(len(student_list)):
        course = list(course_bid[i].keys())
        amount_of_bidrs[course[0]].append(student_list[i].get_name())
        student_element[course[0]].append(student_list[i])

    for key in amount_of_bidrs.keys():
        for j in range(len(course_list)):
            try_to_enroll = amount_of_bidrs[key]
            student_object_try = student_element[key]
            if key == course_list[j].get_name() and course_list[j].can_be_enroll(len(try_to_enroll)):
                if len(try_to_enroll) > 0:  # when we can enroll everyone
                    for need_to in range(len(try_to_enroll)):
                        if check_overlap(student_object_try[need_to], course_list[j]):  # Enroll student if he dose
                            # not have overlap course to course_list[j]
                            course_list[j].student_enrollment(try_to_enroll[need_to], student_object_try[need_to])
                            for stu in range(len(student_object_try)):
                                if student_object_try[stu].get_name() == try_to_enroll[need_to] and \
                                        student_object_try[stu].get_need_to_enroll() != 0:
                                    student_object_try[stu].got_enrolled(course_list[j].get_name())

                        else:  # If the student enrolled already to overlap course over course_list[j]
                            counter = 0
                            _data[try_to_enroll[counter]] = \
                                student_object_try[need_to].get_next_preference(course_list[j].get_name())
                            counter += 1

            elif key == course_list[j].get_name() and course_list[j].get_capacity() == 0:  # If the capacity is zero
                counter = 0
                for stu in range(len(student_object_try)):
                    if len(try_to_enroll) > counter:
                        if student_object_try[stu].get_name() == try_to_enroll[counter]:
                            if student_object_try[stu].get_need_to_enroll() != 0:
                                _data[try_to_enroll[counter]] = \
                                    student_object_try[stu].get_next_preference(course_list[j].get_name())
                                counter += 1

            elif key == course_list[j].get_name() and not course_list[j].can_be_enroll(len(try_to_enroll)):
                # If the capacity is not let to enroll all student who put bid over that course
                student_object_try = sorted(student_object_try, key=lambda x: x.get_current_highest_bid(), reverse=True)

                check = there_is_a_tie(student_object_try)
                print(check)
                for stu in range(len(student_object_try)):
                    if check_overlap(student_object_try[stu], course_list[j]) and course_list[j].get_capacity() > 0:
                        # If there is a place to enroll student stu
                        course_list[j].student_enrollment(student_object_try[stu].get_name(), student_object_try[stu])
                        student_object_try[stu].got_enrolled(course_list[j].get_name())

                    else:
                        # If there is a student such that want to enroll to course but is overlap or have zero capacity
                        _data[student_object_try[stu].get_name()] = student_object_try[stu].get_next_preference(course_list[j].get_name())


def algorithm(fixed, student_list, course_list, rounds=3):
    student_names = list(fixed.keys())
    ranks = list(fixed.values())
    for i in range(rounds):
        round_data = ready_to_new_round(student_names, ranks)
        enroll_students(round_data, student_list, course_list)
        second_phase(round_data, student_list, course_list)


def main():
    courses = ["a", "b", "c", "d"]
    ranking = [[{'name': 'Joseph Stein', 'course name': 'a', 'rank': 50},
                {'name': 'Joseph Stein', 'course name': 'b', 'rank': 100},
                {'name': 'Joseph Stein', 'course name': 'c', 'rank': 200},
                {'name': 'Joseph Stein', 'course name': 'd', 'rank': 150}],
               [{'name': 'Itay Simchayov', 'course name': 'a', 'rank': 110},
                {'name': 'Itay Simchayov', 'course name': 'b', 'rank': 100},
                {'name': 'Itay Simchayov', 'course name': 'c', 'rank': 150},
                {'name': 'Itay Simchayov', 'course name': 'd', 'rank': 140}],
               [{'name': 'Lihi Belfer', 'course name': 'a', 'rank': 60},
                {'name': 'Lihi Belfer', 'course name': 'b', 'rank': 130},
                {'name': 'Lihi Belfer', 'course name': 'c', 'rank': 250},
                {'name': 'Lihi Belfer', 'course name': 'd', 'rank': 50}]]

    row_number = len(ranking)
    column_number = len(ranking[0])
    fixed = create_matrix(ranking, courses, row_number, column_number)
    student_list = create_students(fixed, courses)
    course_list = create_courses(fixed)
    algorithm(fixed, student_list, course_list)
    for i in range(len(student_list)):
        student_list[i].to_string()
        print()

    for i in range(len(course_list)):
        course_list[i].to_string()
        print()


if __name__ == '__main__':
    main()
