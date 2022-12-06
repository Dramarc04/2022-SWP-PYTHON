from enum import Enum


class Firma:
    def __init__(self, people, departments):
        self.people = people.copy()
        self.departments = departments.copy()

    def employee_count(self):
        temp_count = 0
        for i in self.people:
            if type(i) == Employee:
                temp_count += 1
        return temp_count

    def leader_count(self):
        temp_count = 0
        for i in self.people:
            if type(i) == Leader:
                temp_count += 1
        return temp_count

    def department_count(self):
        return len(self.departments)

    def add_department(self, department):
        self.departments.append(department)

    def add_employee(self, employee):
        self.people.append(employee)

    def biggest_department(self):
        last_count = 0
        for i in self.departments:
            temp_count = 0
            for e in self.people:
                if e.department == i:
                    temp_count += 1
            if temp_count > last_count:
                biggest_dep = i
            last_count = temp_count
        return biggest_dep

    def gender_ratio(self):
        male_count = 0
        female_count = 0
        for i in self.people:
            if i.gender == Gender.MALE:
                male_count += 1
            elif i.gender == Gender.FEMALE:
                female_count +=1
        male_percentage = (male_count/len(self.people))*100
        female_percentage = (female_count / len(self.people)) * 100
        results = [male_percentage, female_percentage]
        return results

class Person:
    def __init__(self, fname, lname, gender):
        self.fname = fname
        self.lname = lname
        self.gender = gender
    def __str__(self):
        return f"{self.fname} {self.lname} ({self.gender})"

class Gender(Enum):
    MALE = 1
    FEMALE = 2

class Employee(Person):
    def __init__(self, fname, lname, gender, department):
        super().__init__(fname, lname, gender)
        self.department = department
    def __str__(self):
        return super().__str__() + f"| {self.department}"

class Leader(Employee):
    def __init__(self, fname, lname, gender, department):
        super().__init__(fname, lname, gender, department)

    def __str__(self):
        return super().__str__() + f"| {self.department} | LEADER"

class Department():
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return f"{self.name}"


dep1 = Department("Production")
dep2 = Department("Manifactury")
employee1 = Employee("Mark", "Davis", Gender.MALE, dep1)
employee2 = Employee("Dave", "Heffley", Gender.MALE, dep1)
employee3 = Leader("Sascha", "Labor", Gender.FEMALE, dep2)

employeeList = [employee1, employee2]
departmentList = [dep1, dep2]

company = Firma(employeeList, departmentList)
company.add_employee(employee3)

print(company.employee_count())
print(company.leader_count())
print(company.department_count())
print(company.biggest_department())
print(company.gender_ratio())