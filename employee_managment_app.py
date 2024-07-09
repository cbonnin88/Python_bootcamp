# Building our Employee Class :
class EmployeeManagementSystem:
    def __init__(self):
        self.employees = {}

    # Creating our 'create employee' method
    def create_employee(self, emp_id, name, job_title, department, salary):
        self.employees[emp_id] = {'Full Name': name, 'Job Title': job_title, 'Department': department, 'Salary': salary}

    # Creating our 'Read Employee' method
    def read_employee_info(self, emp_id):
        return self.employees.get(emp_id, None)

    # Creating our 'Update Employee' method
    def update_employee_info(self, emp_id, name=None, position=None):
        if emp_id in self.employees:
            if name:
                self.employees[emp_id]['name'] = name
            if position:
                self.employees[emp_id]['position'] = position
                return True
            else:
                return False

    # Creating our 'Delete Employee' Method
    def delete_employee_info(self, emp_id):
        if emp_id in self.employees:
            del self.employees[emp_id]
            return True
        else:
            return False

    # Defining the functions for the Admin Menu


def admin_menu():
    print("Admin Menu")
    print("1. Add New Employee")
    print("2. View Employee Information")
    print("3. Update Employee Information")
    print("4. Delete Employee Information")
    print("5. Exit")


def main():
    global name, department, salary
    emp_system = EmployeeManagementSystem()
    while True:
        admin_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            emp_id = input("Enter Employee ID: ")
            name = input("Enter Employee Full name: ")
            position = input("Enter Job Title: ")
            department = input("Enter department Name: ")
            salary = input("Enter salary : ")
            emp_system.create_employee(emp_id, name, position, department, salary)
            print("Employee Successfully Added")

        elif choice == "2":
            emp_id = input("Enter Employee ID: ")
            employee = emp_system.read_employee_info(emp_id)

            if employee:
                print("Employee details: ")
                print("ID: ", emp_id)
                print("Name: ", name)
                print("Position: ", employee['Job Title'])
                print("Department: ", department)
                print("Salary: ", salary)
            else:
                print("Employee not found")

        elif choice == "3":
            emp_id = input("Enter employee ID: ")
            name = input("Enter new name (press ENTER to skip): ")
            position = input("Enter new position (press ENTER to skip): ")

            if emp_system.update_employee_info(emp_id, name, position):
                print("Employee details successfully updated")
            else:
                print("Employee not found.")

        elif choice == "4":
            emp_id = input("Enter Employee ID: ")
            if emp_system.delete_employee_info(emp_id):
                print("Employee successfully deleted.")
            else:
                print("Employee not found")

        elif choice == "5":
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please enter a valid option")


if __name__ == "__main__":
    main()
