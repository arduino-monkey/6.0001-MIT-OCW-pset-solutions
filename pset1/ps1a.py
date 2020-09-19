annualSalary = float(input('Enter your annual salary:'))
portionSaved = float(input('Enter the percent of your salary to save, as a decimal:'))
totalCost = float(input('Enter the cost of your dream home:'))
portionDownPayment = 0.25
currentSavings = 0
r = 0.04

downPayment = portionDownPayment * totalCost
monthlySalary = annualSalary/12

totalMonths = 0
while currentSavings < downPayment:
    currentSavings += currentSavings*r/12
    currentSavings += monthlySalary*portionSaved
    totalMonths += 1
print('Number of months:',totalMonths)