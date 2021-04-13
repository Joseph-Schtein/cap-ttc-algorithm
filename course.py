class Course:

    def __init__(self, course_name, maximal_capacity, capacity_bounds, overlap_courses=[]):
        self.name = course_name
        self.maximal_capacity = maximal_capacity
        self.capacity = capacity_bounds
        self.students = []
        self.overlap = overlap_courses

    def student_enrollment(self, student_name, student_element):
        if self.capacity > 0 and student_name not in self.students and student_element.get_need_to_enroll():
            self.capacity -= 1
            self.maximal_capacity -= 1
            self.students.append(student_name)

        else:
            print("We can't enroll you to the course")

    def can_be_enroll(self):
        return self.capacity > 0

    def get_overlap_list(self):
        return self.overlap

    def get_name(self):
        return self.name

    def to_string(self):
        print("Course name: ", self.name, ", Capacity: ", self.capacity, "\n" 
              "Number of student that enroll to this course is: ", len(self.students), "\n"
              "Student list: ", self.students, "\n", "Overlap courses are: ", self.overlap)
