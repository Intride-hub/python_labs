from src.lab09 import Group
from src.lab08.models import Student

group = Group("data/lab09/students.csv")

# CREATE
group.add(Student("Чееловеек ПАУК", "2003-01-15", "БИВТ-21-1", 4.7))











# # READ
# print(group.list())

# # FIND
# print(group.find("иванов"))

# # UPDATE
# group.update("Иванов Иван", gpa=4.6)

# # DELETE
# group.remove("Петров Пётр")

# # # STATS ★
# # print(group.stats())

