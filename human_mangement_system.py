# Creating our Employees Class with their attributes:
class Employees:
    def __init__(self, emp_id, name, job_title, dob, department, salary):
        self.emp_id = emp_id
        self.name = name
        self.job_title = job_title
        self.dob = dob
        self.department = department
        self.salary = salary


# Creating  our HRMS class with their attributes:
class HRMS:
    def __init__(self):
        self.employees = []

    # Creating a method to add an employee :
    def add_employee(self):
        emp_id = input("Enter Employee ID: ")
        name = input("Enter Employee Full name: ")
        job_title = input("Enter Employee Job Title: ")
        dob = input("Enter Employee date of birth: ")
        department = input("Enter Employee Department: ")
        salary = input("Enter Employee Salary: ")

        new_employee = Employees(emp_id, name, job_title, dob, department, salary)
        self.employees.append(new_employee)
        print(f"Employee {name} successfully added.\n")

    # Creating a method to view all employees:
    def view_employee_info(self):
        if not self.employees:
            print("Employee not found in system.\n")
            return
        for emp in self.employees:
            print(f"ID: {emp.emp_id}, Name: {emp.name}, Job Title: {emp.job_title}, Date of Birth: {emp.dob}, "
                  f"Department: {emp.department}, Salary: {emp.salary}\n")

        print("")

    # Creating a method to update employee information:
    def update_employee_info(self):
        emp_id = input("Enter Employee ID to update information: ")

        for emp in self.employees:
            if emp.emp_id == emp_id:
                emp.name = input("Enter new name: ")
                emp.job_title = input("Enter new job title: ")
                emp.department = input("Enter new department: ")
                emp.salary = input("Enter new salary: ")
                print(f"Employee {emp_id} successfully updated.\n")
                return

        print(f"No employee found with the ID {emp_id}.\n")

    # Creating a method to delete an employee from the system
    def delete_employee_info(self):
        emp_id = input("Enter Employee ID to delete from system: ")

        for emp in self.employees:
            if emp.emp_id == emp_id:
                self.employees.remove(emp)
                print(f"Employee {emp_id} deleted successfully")
                return

            print(f"No Employee found with ID: {emp_id}.\n")

    # Creating our method to search for an employee:
    def employee_search(self):
        emp_id = input("Enter Employee ID: ")

        for emp in self.employees:
            if emp.emp_id == emp_id:
                print(
                    f"Employee found: ID {emp.emp_id}, Name: {emp.name}, Job Title: {emp.job_title}, Department: {emp.department}, Salary: {emp.salary}\n")
                return

        print(f"No Employee found with ID {emp_id}.\n")


# Creating our Command menu:

def main():
    hrms = HRMS()

    while True:
        print("1. Add New Employee")
        print("2. View Existing Employee")
        print("3. Update Existing Employee")
        print("4. Delete an Employee")
        print("5. Search for an Employee")
        print("6. Exit")

        choice = input("Please enter your choice: ")

        if choice == "1":
            hrms.add_employee()

        elif choice == "2":
            hrms.view_employee_info()

        elif choice == "3":
            hrms.update_employee_info()

        elif choice == "4":
            hrms.delete_employee_info()

        elif choice == "5":
            hrms.employee_search()

        elif choice == "6":
            print("Exiting our system. Thank you ")
            break

        else:
            print("Invalid Choice, Please try again\n")


if __name__ == "__main__":
    main()
