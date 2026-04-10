from collections import namedtuple
Employee = namedtuple("Employee",["name","salary"])
emps = [
Employee("A",50000),
Employee("B",75000),
Employee("C",65000)
]
highest = max(emps, key=lambda x:x.salary)
print("Highest salary:",highest)
