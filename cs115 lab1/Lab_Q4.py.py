# this program converts feet and inches to centimeters. #
feet=int(input('enter number of feet:'))
inches=int(input('enter number of inches:'))
cm=(feet*12*2.54)+(inches*2.54)
print('{} ft {} in = {} cm'.format(feet,inches,cm))
