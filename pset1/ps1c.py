startingSalary = float(input('Enter the starting salary:'))

semiAnnualRaise = 0.07
r = 0.04
portionDownPayment = 0.25
totalCost = 1000000
accuracy = 100
currentSavings = 0
totalMonths = 36
downPayment = portionDownPayment*totalCost

low = 0
high = 1 
portionToBeSaved = (low + high)/2
steps = 0

def savings(totalMonths, annualSalary, moneySaved, r, semiAnnualRaise, portionToBeSaved):
    while totalMonths >= 1:
        monthlySalary = annualSalary/12
        moneySaved += moneySaved*r/12
        moneySaved += monthlySalary*portionToBeSaved
        totalMonths -= 1
        if totalMonths % 6 == 0:
            annualSalary += semiAnnualRaise*annualSalary
    return moneySaved
    
whileTemp = 0
        
while abs(whileTemp - downPayment) >= 100 and portionToBeSaved != 1:
    steps += 1
    temp = savings(totalMonths,startingSalary,currentSavings,r,semiAnnualRaise,portionToBeSaved)
    if temp > downPayment:
        high = portionToBeSaved
    elif temp < downPayment:
        low = portionToBeSaved
    
    portionToBeSaved = (low + high)/2
    whileTemp = savings(totalMonths,startingSalary,currentSavings,r,semiAnnualRaise,portionToBeSaved)
    
if portionToBeSaved != 1:
    print('Best savings rate:',round(portionToBeSaved,4))
    print('Steps in bisection search:',steps)
else:
    print('It is not possible to pay the down payment in three years.')
