annualSalary = float(input('Enter your starting annual salary:'))
portionSaved = float(input('Enter the percent of your salary to save, as a decimal:'))
totalCost = float(input('Enter the cost of your dream home:'))
semiAnnualRaise = float(input('Enter the semi-annual raise, as a decimal:'))
portionDownPayment = 0.25
currentSavings = 0
r = 0.04

downPayment = portionDownPayment * totalCost
monthlySalary = annualSalary/12

totalMonths = 0
while currentSavings < downPayment:
    monthlySalary = annualSalary/12
    currentSavings += currentSavings*r/12
    currentSavings += monthlySalary*portionSaved
    totalMonths += 1
    if totalMonths % 6 == 0:
        annualSalary += semiAnnualRaise*annualSalary
print('Number of months:',totalMonths)