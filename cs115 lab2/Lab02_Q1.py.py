a = float(input('Enter the length of side a:'))
b = float(input('Enter the length of side b:'))
c = float(input('Enter the length of side c:'))
if (a > 0 and b > 0 and c > 0):
    if (a + b > c and a + c > b and b + c > a):
        print('This is a valid triangle.')
    else:
        print('This is NOT a valid triangle.')

else:
    print('Side lengths cannot be negative or zero. Exiting...')