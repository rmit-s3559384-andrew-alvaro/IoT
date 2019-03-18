from courses.course import Course

class Writing(Course):
    COST_PER_STUDENT = 0
    FEE_PER_STUDENT = 200
    MAXIMUM_STUDENTS_ALLOWED = 10

    def __init__(self, id, name, teacherName, flatCost, students = None):
        super().__init__(id, name, teacherName, students)
        self._flatCost = flatCost

    def flatCost(self):
        return self._flatCost

    def costPerStudent(self):
        return self.COST_PER_STUDENT

    def feePerStudent(self):
        return self.FEE_PER_STUDENT

    def maximumStudentsAllowed(self):
        return self.MAXIMUM_STUDENTS_ALLOWED
