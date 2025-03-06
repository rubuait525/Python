#HW_Python_String_Formatting
empName = "ruby"
empAge = 200
yearlySalary = 100000
fullTimeEmployee = True

employeesInformation = f"Employee Name: {empName.upper()}, Employee Age: {empAge},Employee Yearly Salary: {yearlySalary:,.2f}$,Is Employee Fulltime: {fullTimeEmployee}"
print(employeesInformation)