from courses.course import Course

class Cooking(Course):
    FLAT_COST = 1000
    COST_PER_STUDENT = 0
    MAXIMUM_STUDENTS_ALLOWED = 10

    def __init__(self, id, name, teacherName, feePerStudent, students = None):
        super().__init__(id, name, teacherName, students)
        self._feePerStudent = feePerStudent

    def flatCost(self):
        return self.FLAT_COST

    def costPerStudent(self):
        return self.COST_PER_STUDENT

    def feePerStudent(self):
        return self._feePerStudent

    def maximumStudentsAllowed(self):
        return self.MAXIMUM_STUDENTS_ALLOWED
