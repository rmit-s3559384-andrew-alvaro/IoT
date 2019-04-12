from courses.course import Course

class Sewing(Course):
    FLAT_COST = 0
    COST_PER_STUDENT = 100
    FEE_PER_STUDENT = 300
    MAXIMUM_STUDENTS_ALLOWED = 10

    def __init__(self, id, name, teacherName, students = None):
        super().__init__(id, name, teacherName, students)

    def flatCost(self):
        return self.FLAT_COST

    def costPerStudent(self):
        return self.COST_PER_STUDENT

    def feePerStudent(self):
        return self.FEE_PER_STUDENT

    def maximumStudentsAllowed(self):
        return self.MAXIMUM_STUDENTS_ALLOWED
