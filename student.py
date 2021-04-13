import copy


def check_budget(order):
    sum_bidding = 0
    order_values = list(order.values())
    for i in range(len(order_values)):
        sum_bidding += order_values[i]

    if sum_bidding > 500:
        print("need to throw an exception here")
        return False

    else:
        return True


def create_ordinal_order(order):
    count = 1
    ordinal = list(order.values())
    course_names = list(order.keys())
    for i in range(len(ordinal)):
        ind = ordinal.index(max(ordinal))
        ordinal[ind] = count
        count += 1

    output = copy.deepcopy(order)
    for i in range(len(output)):
        output[course_names[i]] = ordinal[i]

    return output


class Student:

    def __init__(self, name, cardinal_order, enrolled_or_not):
        self.name = name
        self.need_to_enroll = 2
        self.cardinal_order = cardinal_order
        self.enrolled_or_not = enrolled_or_not
        self.ordinal_order = {}
        if check_budget(self.cardinal_order):
            self.ordinal_order = create_ordinal_order(cardinal_order)

    def get_name(self):
        return self.name

    def get_ordinal(self):
        return self.ordinal_order

    def get_cardinal(self):
        return self.cardinal_order

    def get_need_to_enroll(self):
        return self.need_to_enroll

    def get_enrolment_status(self):
        return self.enrolled_or_not

    def get_next_preference(self, course_name):
        self.cardinal_order[course_name] = 0
        index = list(self.cardinal_order).index(max(self.cardinal_order))
        cardinal_keys = list(self.cardinal_order.keys())
        cardinal_value = list(self.cardinal_order.values())
        return {cardinal_keys[index]: cardinal_value[index]}

    def got_enrolled(self, course_name):
        if self.need_to_enroll > 0 and self.enrolled_or_not[course_name] == 0:
            self.need_to_enroll -= 1
            self.cardinal_order[course_name] = 0
            self.enrolled_or_not[course_name] = 1

        elif self.enrolled_or_not[course_name] == 1:
            print("Student: ", self.name, ", is already enrolled to the course: ", course_name)

        else:
            print("Student: ", self.name, " got to the limit of courses enrollment")

    def to_string(self):
        print("Student name:", self.name, ", The cardinal order is: ", self.cardinal_order, "\n"
              "The ordinal is: ", self.ordinal_order, "\n", "The courses that: ", self.name,  " enrolled are: ", self.enrolled_or_not, "\n")