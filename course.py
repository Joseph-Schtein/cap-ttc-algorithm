class Course:

    def __init__(self, course_name, maximal_capacity, capacity_bounds):
        self.name = course_name
        self.maximal_capacity = maximal_capacity
        self.capacity = capacity_bounds
        self.students = []

    def student_enrollment(self, student_name):
        if self.capacity > 0:
            self.capacity -= 1
            self.maximal_capacity -= 1
            self.student.append(student_name)

        else:
            print("We can't enroll you to the course")

    def get_free_space(self):
        return self.capacity
