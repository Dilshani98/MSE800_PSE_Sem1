#Activity 2: Gross Pay and Net Pay Calculator

#function to calculate gross pay
def calculateGrossPay(hours, payRate):
    return hours * payRate

#function to calculate annual tax deduction
def calculateTaxDeduction(annualIncome):

    if (0 < annualIncome < 15600):
        taxRate = 0.105

    elif (15601 <  annualIncome < 53500):
        taxRate = 0.175

    elif ( 53501 < annualIncome < 78100):
        taxRate = 0.30

    elif ( 78101 < annualIncome < 180000):
        taxRate = 0.33

    else:
        taxRate = 0.39

    taxDeduction = annualIncome*taxRate
    return taxDeduction

#get user unputs for hours worked and pay rate
hours = float(input("Enter Hours Worked for this Month: "))
payRate = float(input("Enter Pay Rate: "))

#call functions to calculate gross pay and tax deduction
grossPay = calculateGrossPay(hours, payRate)

annualIncome = grossPay * 12
taxDeduction = calculateTaxDeduction(annualIncome)

#calculate net pay for the month
netPay = grossPay - (taxDeduction / 12)

print(f"Net Pay for this month:{netPay:.2f}")