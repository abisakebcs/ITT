print("=== Day 1 ===")
Day_1 = set()
n = int(input("Enter the No.of Students:"))
for i in range(n):
    student_rollno = input("Enter the Roll No of the Student(day 1):")
    Day_1.add(student_rollno)
print("Students present on Day 1:",Day_1)

print("=== Day 2 ===") 
Day_2 = set()
n = int(input("Enter the No.of Students:"))
for i in range(n):
    student_rollno = input("Enter the Roll No of the Student(day 2):")
    Day_2.add(student_rollno)
print("Students present on Day 2:",Day_2)

print("=== Students Attendence ===")

Stu_pre_both = Day_1.intersection(Day_2)
print("Students present on both days:", Stu_pre_both)

stu_pre_either = Day_1.union(Day_2)
print("Students present on either of two days:", stu_pre_either)

stu_abs_second = Day_1.difference(Day_2)
print("Students absent on second day:", stu_abs_second)
