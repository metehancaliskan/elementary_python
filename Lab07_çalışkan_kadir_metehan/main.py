# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 13:57:20 2020

@author: User
"""

from Stock import *


def getByStockQuantity(all_stocks, quantity):
    """


    Parameters
    ----------
    all_stocks : list
    quantity : string
        take a list and a value of quantity. Find the count in list and check is quantity greater or not than count in list.

    Returns
    -------
    greater_stocks : list
        returns the list of Stocks in the database who have a quantity greater than
that passed as a parameter.

    """

    greater_stocks = []
    for c in all_stocks:
        if (int(c.get_count()) > quantity):
            greater_stocks.append(c)
    return greater_stocks


def getByPrice(greater_stocks, value):
    """


    Parameters
    ----------
    greater_stocks : list
    value : string
         take a list and a value. Find the price in list and check is value less or not than price in list..

    Returns
    -------
    prc : list
        returns the list of Stocks in the database who have a
price less than the value passed as a parameter.

    """

    prc = []
    for p in greater_stocks:
        if (float(p.get_price()) < value):
            prc.append(p)
    return prc


file = open('input.txt', 'r')
all_stocks = []
for line in file:
    line = line.strip()
    line = line.split(';')
    new = Stock(line[0], line[1], line[2], line[3])
    all_stocks.append(new)
file.close()

quantity = 6
value = 5

print('Printing Stocks whose price is less than {} and count is over {}:'.format(value, quantity))
for i in getByPrice(getByStockQuantity(all_stocks, quantity), value):
    print(i)