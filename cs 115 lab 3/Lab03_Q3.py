"""
This function take an integer as input and returns total digit sum of the numbers.
parameter:a
parameter type:integer
return:total sum of the digit numbers up to num,itself included.
 """

def sumDigits(a):
    n = 0
    if (a > 0):
        for i in range(1, a + 1):
            while (i > 0):
                b = i % 10
                n += b
                i = i // 10
        print('The sum of the digits in the number from 1 to {} is {}'.format(a, n))
    else:
        print('Value must be Positive')


a = int(input('Enter a positive integer:'))
sumDigits(a)


