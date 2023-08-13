from unittest import result


class employee:
    def __init__(self,emp_id,emp_name,emp_sal,empdept,hoursworked):
        self.emp_id = emp_id 
        self.emp_name = emp_name
        self.emp_sal =emp_sal
        self.empdept = empdept

 def addEmployee(empList, employee1):
     empList.append(employee1)
     print(f"{employee1.name} has been added to the employee managment system ")

def remove_employee(empList, emp_name):
    removed = False
    for employee in empList:
        if employee1.name == emp_name:
            empList.remove(employee1)
            print(f"{employee1.name} has been removed from the Employee Management System.")
            removed = True
            break

    if not removed:
        print(f"Employee with name '{employee1_name}' not found in the system.")

def view_employees(empList):
    if not empList:
        print("No employees found in the system.")
        return

    print("Employee list:")
    for employee in empList:
        print(f"Name: {employee1.name}, Age: {employee1.age}, Department: {employee1.department}, Salary: {employee1.salary}")


employees = []

emp1 = Employee("Alanood", 23, "IT", 1000)
emp2 = Employee("Said", 26, "IT", 2000)
emp3 = Employee("Aisha", 31, "HR", 900)

add_employee(employees, emp1)
add_employee(employees, emp2)
add_employee(employees, emp3)

remove_employee(employees, "Said")

view_employees(employees)
    
 
