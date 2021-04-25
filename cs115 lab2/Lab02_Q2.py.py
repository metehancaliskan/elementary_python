income = float(input('Enter the total income (TL) : '))
if (0 < income and income < 10000):
    net_income = income - (income * 0.22)
    print('The net income is {}'.format(net_income))

elif (10000 < income and income < 100000):
    net_income = income - (income * 0.26)
    print('The net income is {}'.format(net_income))

elif (100000 <= income):
    net_income = income - (income * 0.33)
    print('The net income is {}'.format(net_income))

if (income <= 0):
    net_income = income - (income * 0.22)
    print('Entered income value is not valid. Exiting...')  