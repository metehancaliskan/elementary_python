# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 13:33:35 2020

@author: User
"""


class Stock:
    def __init__(self, name, count, price, city):
        """


        Parameters
        ----------
        name : string
        count : string
        price : string
        city : string

        Returns
        -------
        None.

        """

        self.__name = name
        self.__count = count
        self.__price = price
        self.__city = city

    def __repr__(self):
        """

        Returns
        -------
        s : string
            return the parameters defined in the object called Stock one under the other.

        """

        s = 'Name:' + self.__name + '\n'
        s += 'Count:' + self.__count + '\n'
        s += 'Price:' + self.__price + '\n'
        s += 'City:' + self.__city + '\n'
        return s

    def get_name(self):
        """


        Returns
        -------
        string
            return the name defined in the object called Stock.

        """

        return self.__name

    def get_count(self):
        """


        Returns
        -------
        string
            return the count defined in the object called Stock..

        """

        return self.__count

    def get_price(self):
        """


        Returns
        -------
        string
            return the price defined in the object called Stock..

        """

        return self.__price

    def get_city(self):
        """


        Returns
        -------
        string
            return the city defined in the object called Stock..

        """

        return self.__city

    def set_count(self, c):
        """


        Parameters
        ----------
        c : string
            take a new data and update the old one.

        Returns
        -------
        None.

        """

        self.__count = c

