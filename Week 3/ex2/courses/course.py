from abc import ABC, ABCMeta, abstractmethod

class Course(ABC):
    def __init__(self, id, name, teacherName, students):
        super().__init__()
        self.__id = id
        self.__name = name
        self.__teacherName = teacherName
        self.__students = students if students is not None else set()

    def getID(self):
        return self.__id

    def getName(self):
        return self.__name

    def getTeacherName(self):
        return self.__teacherName

    def setTeacherName(self, teacherName):
        self.__teacherName = teacherName

    def getStudents(self):
        return self.__students

    def cost(self):
        return self.flatCost() + self.costPerStudent() * len(self.__students)

    def income(self):
        return len(self.__students) * self.feePerStudent()

    def addStudent(self, studentID):
        if(len(self.__students) >= self.maximumStudentsAllowed() or studentID in self.__students):
            return False
        self.__students.add(studentID)
        return True

    def __str__(self):
        return "Course ID {}, Course Name: {}, Teacher Name: {}, Cost: ${}, Income: ${}, Student Count: {}". \
        format(self.__id, self.__name, self.__teacherName, self.cost(), self.income(), len(self.__students))

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
