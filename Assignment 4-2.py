#Employee Details
employee_name = "Jenna Jekins"
num_shifts = 15
num_transactions = 30
transaction_value = 25000.00

#Calculate productivity score
productivity_score = (transaction_value / num_transactions) / num_shifts

#Bonus Base 
bonus = 0.0

#Productivity Score & Bonus Correlations (Nested If Statements)
if productivity_score <= 30:
    bonus = 50.00
else:
    if productivity_score <= 69:
        bonus = 75.00
    else:
        if productivity_score <= 199:
            bonus = 100.00
        else:
            bonus = 200.00

#Display Results
print(f"Employee Name: {employee_name}")
print(f"Employee Bonus: ${bonus:.2f}")