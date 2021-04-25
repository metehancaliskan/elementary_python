# -*- coding: utf-8 -*-
"""
Created on Thu Nov  5 15:52:20 2020

@author: User
"""

n = int(input('Enter the value of n:'))
SUM = 1


def estimateE(n):
    """


    Parameters
    ----------
    n : integer
    take a integer and calculate each elemant of 'e' series.

    Returns
    -------
    TYPE: tuple
        show the each elemant of 'e' series.

    """

    result = (1,)

    def factoriel(number):
        """


        Parameters
        ----------
        number : integer
            take integer and calculate factorial of integer.

        Returns
        -------
        factorial : integer
            return the factorial value of number.

        """

        factorial = 1
        for i in range(1, number + 1):
            factorial *= i
        return factorial

    global SUM
    SUM = 1
    for i in range(n):
        SUM = SUM + (1 / factoriel(i + 1))
        result += (1 / factoriel(i + 1),)
    return result


string = ''
for a in estimateE(n):
    string += ' ' + '+' + ' ' + str(a)
    """ the above line show the each elemant of tuple respectively."""
print('E ={}'.format(string))
print('Estimated value:{}'.format(SUM))
e = 2.718281828459045
print('Error = {}'.format(e - SUM))