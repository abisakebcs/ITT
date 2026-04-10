print("=== User 1 ===")
User_1 = set()
n = int(input("Enter the No.of Courses:"))
for i in range(n):
    Course_interest = input("Enter the interested Course of the User 1:")
    User_1.add(Course_interest)
print("Interested Courses of User 1:",User_1)

print("=== User 2 ===")
User_2 = set()
m = int(input("Enter the No.of Courses:"))
for i in range(m):
    Course_interest = input("Enter the interested Course of the User 2:")
    User_2.add(Course_interest)
print("Interested Courses of User 2:",User_2)

print("=== Online Learning Platform ===")

Common_interests = User_1.intersection(User_2)
print("Interested Courses common to both Users:", Common_interests)

Sugg_Course = User_1.difference(User_2)
print("Suggested New Courses:", Sugg_Course)

