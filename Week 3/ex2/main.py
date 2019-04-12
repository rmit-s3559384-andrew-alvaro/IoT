from courses.cooking import Cooking
from courses.sewing import Sewing
from courses.writing import Writing

class Main:
    @staticmethod
    def main():
        courses = [
            Cooking("001", "Italian Cooking", "Matthew", 500),
            Cooking("002", "Seafood Cooking", "Shekhar", 700, set(["s1234567", "s1234568"])),
            Sewing("003", "Sewing", "Rodney", set(["s1234567", "s1234568", "s1234569", "s1234569"])),
            Writing("004", "Creative Writing", "Kevin", 800, set(["s1234567", "s1234568", "s1234569"])),
            Writing("005", "Business Writing", "Ryan", 600, set(["s1234567", "s1234568"]))
        ]

        courses[0].addStudent("s1234567")
        courses[0].addStudent("s1234568")
        courses[0].addStudent("s1234569")
        
        for course in courses:
            print(course)
        print()
        
        course = courses[0]
        course.setTeacherName("Matt")
        print("Course ID {}, Course Name: {}, Teacher Name: {}, Cost: ${}, Income: ${}, Student Count: {}". \
            format(course.getID(), course.getName(), course.getTeacherName(), course.cost(), course.income(), \
            len(course.getStudents())))

Main.main()
