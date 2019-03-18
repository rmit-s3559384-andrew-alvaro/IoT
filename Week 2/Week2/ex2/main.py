from courses.cooking import Cooking
from courses.sewing import Sewing
from courses.writing import Writing

italianCooking = Cooking("001", "Italian Cooking", "Matthew", 500)
italianCooking.addStudent("s1234567")
italianCooking.addStudent("s1234568")
italianCooking.addStudent("s1234569")

seafoodCooking = Cooking("002", "Seafood Cooking", "Shekhar", 700, set(["s1234567", "s1234568"]))
sewing = Sewing("003", "Sewing", "Rodney", set(["s1234567", "s1234568", "s1234569", "s1234569"]))
creativeWriting = Writing("004", "Creative Writing", "Kevin", 800, set(["s1234567", "s1234568", "s1234569"]))
businessWriting = Writing("005", "Business Writing", "Ryan", 600, set(["s1234567", "s1234568"]))

print(italianCooking)
print(seafoodCooking)
print(sewing)
print(creativeWriting)
print(businessWriting)
