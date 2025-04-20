# input statements
salary = float(input("Enter the employee's salary: "))
numDependents = float(input("Enter the number of dependents: "))
# calculate taxes here
stateTax = 0.065 * salary
# state tax is 6.5% of salary
federalTax = 0.28 * salary
# federal tax is 28% of salary
dependentDeduction = (0.025 * salary) * numDependents
# dependent deduction is 2.5% of salary for each dependent
totalWitholding = stateTax + federalTax + dependentDeduction
takeHomePay = salary - totalWitholding
# output statements
print("State Tax: $" + str(stateTax))
print("Federal Tax: $" + str(federalTax))
print("Dependents: " + str(dependentDeduction))
print("Salary: $" + str(salary))
print("Take Home Pay: $" + str(takeHomePay))