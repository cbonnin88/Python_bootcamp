import openpyxl
from openpyxl import Workbook

# Create a new workbook
workbook = openpyxl.Workbook()

# Opening the active workbook sheet
work_sheet = workbook.active

# Sheet Title
work_sheet.title = "Starfield Enterprise-People Data"

# Create Column headers
work_sheet['A1'] = 'Employee ID'
work_sheet['B1'] = 'Last Name'
work_sheet['C1'] = 'First Name'
work_sheet['D1'] = "DOB"
work_sheet['E1'] = "Job Title"
work_sheet['F1'] = "Department"
work_sheet['G1'] = "Salary"
work_sheet['H1'] = "Remote Work Type"
work_sheet['I1'] = "Contract Type"
work_sheet['J1'] = "City"
work_sheet['K1'] = "Region"

# Define a list of tuples containing our people data:
people_data = [
    (100, 'Lemonde', 'Alice', '2000-05-23', 'People Analyst', 'Human Resources', 56000, 'Remote', 'CDI',
     'Ivry-sur_Seine', "île-de-France"),
    (101, 'Coudray', 'Marc', '1988-10-18', 'People Analyst', 'Human Resources', 45000, 'Hybrid', 'CDI', 'Paris',
     "île-de-France"),
    (103, 'Chartier', 'Marie', '1999-04-22', 'Data Engineer', 'Product and Tech', 85000, 'Remote', 'CDI', 'Bordeaux',
     "Nouvelle-Aquitaine"),
    (
    104, 'Lemarc', 'Alexandre', '2001-11-14', 'Backend Developer', 'Product and Tech', 60000, 'Hybrid', 'CDI', 'Chessy',
    "île-de-France"),
    (105, 'Hayer', 'Valerie', '1988-02-18', 'Financial Analyst', 'Finance', 65000, 'Remote', 'CDI', 'Toulouse',
     "Occitanie"),
    (106, 'Demarnier', 'Jean', '1994-01-15', 'Accountant', 'Finance', 55000, 'Hybrid', 'CDI', 'Joinville-Le-Pont',
     "île-de-France"),
    (107, 'Bernier', 'Héléne', '1987-06-22', 'Marketing Analyst', 'Marketing', 48000, 'Remote', 'CDI', 'Le Rochelle',
     "Nouvelle-Aquitaine"),
    (108, 'Gay', 'Damien', '1996-08-01', 'Social Media Manager', 'Marketing', 47000, 'Hybrid', 'CDI', 'Creteil',
     "île-de-France"),
    (109, 'Dumas', 'Alice', '1985-03-10', 'Key Account Manager', 'Sales', 57000, 'Remote', 'CDI', 'Aix-en-Provence',
     "Provence Côte d'Azur"),
    (110, 'Morel', 'Lucas', '1997-07-31', 'Sales Analyst', 'Sales', 60000, 'Hybrid', 'CDI', 'Dourdan',
     "île-de-France")
]

# Iterating over the data and entering it into the worksheet
for row, (Employee_ID, Last_Name, First_Name, DOB, Job_Title, Department, Salary, Remote_Work_Type, Contract_type, City,
          Region) in enumerate(people_data, start=2):

    work_sheet[f'A{row}'] = Employee_ID
    work_sheet[f'B{row}'] = Last_Name
    work_sheet[f'C{row}'] = First_Name
    work_sheet[f'D{row}'] = DOB
    work_sheet[f'E{row}'] = Job_Title
    work_sheet[f'F{row}'] = Department
    work_sheet[f'G{row}'] = Salary
    work_sheet[f'H{row}'] = Remote_Work_Type
    work_sheet[f'I{row}'] = Contract_type
    work_sheet[f'J{row}'] = City
    work_sheet[f'K{row}'] = Region

# Saving
workbook.save("People_data.xlsx")
