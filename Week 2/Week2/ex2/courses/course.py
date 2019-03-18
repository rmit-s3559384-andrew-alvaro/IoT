from abc import ABC, ABCMeta, abstractmethod

class Course(ABC):
    def __init__(self, id, name, teacherName, students):
        super().__init__()
        self.id = id
        self.name = name
        self.teacherName = teacherName
        self.students = students if students is not None else set()

    def cost(self):
        return self.flatCost() + self.costPerStudent() * len(self.students)

    def income(self):
        return len(self.students) * self.feePerStudent()

    def addStudent(self, studentID):
        if(len(self.students) >= self.maximumStudentsAllowed() or studentID in self.students):
            return False
        self.students.add(studentID)
        return True

    def __str__(self):
        return "Course ID {}, Course Name: {}, Teacher Name: {}, Cost: ${}, Income: ${}, Student Count: {}". \
        format(self.id, self.name, self.teacherName, self.cost(), self.income(), len(self.students))

    @abstractmethod
    def flatCost(self):
        pass

    @abstractmethod
    def costPerStudent(self):
        pass

    @abstractmethod
    def feePerStudent(self):
        pass

    @abstractmethod
    def maximumStudentsAllowed(self):
        pass
