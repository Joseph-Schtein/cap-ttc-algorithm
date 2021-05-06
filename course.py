class Course:

    def __init__(self, course_name, maximal_capacity, capacity_bounds, overlap_courses=[]):
        self.name = course_name
        self.maximal_capacity = maximal_capacity
        self.capacity = capacity_bounds
        self.students = []
        self.overlap = overlap_courses
        self.lowest_bid = 0

    def student_enrollment(self, student_name, student_element):
        if self.capacity > 0 and student_name not in self.students and student_element.get_need_to_enroll():
            self.capacity -= 1
            self.maximal_capacity -= 1
            self.students.append(student_name)
            if student_element.get_current_highest_bid() < self.lowest_bid or self.lowest_bid == 0:
                self.lowest_bid = student_element.get_current_highest_bid()

        else:
            print("We can't enroll you to the course")

    def can_be_enroll(self, number_of_students):
        return self.capacity >= number_of_students

    def get_lowest_bid(self):
        return self.lowest_bid

    def get_overlap_list(self):
        return self.overlap

    def get_name(self):
        return self.name

    def get_capacity(self):
        return self.capacity

    def to_string(self):
        print("Course name: ", self.name, ", Capacity: ", self.capacity, "\n" 
              "Number of student that enroll to this course is: ", len(self.students), "\n"
              "Student list: ", self.students, "\n", "Overlap courses are: ", self.overlap)
