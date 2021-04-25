# -*- coding: utf-8 -*-
"""
Created on Thu Nov  5 16:01:11 2020

@author: User
"""

Original_List = [2, 3.75, False, 'Today', 'CS115', 6, 1.5, 4.0, 'python', True, 25,
                 1.9]


def separate(Original_List):
    """


    Parameters
    ----------
    Original_List : list
        take a list and separate it according to type of element in list.

    Returns
    -------
    dictionary : dictionary
        there are 4 keys in dictionary and all keys have more than one values.

    """

    dictionary = {}
    b = []
    ı = []
    s = []
    f = []
    for i in Original_List:
        if (type(i) == bool):
            b.append(i)
        elif (type(i) == int):
            ı.append(i)
        elif (type(i) == str):
            s.append(i)
        elif (type(i) == float):
            f.append(i)
    """ for loop separate elements in list according to type"""

    dictionary['<class "bool"> -> '] = b
    dictionary['<class "int"> -> '] = ı
    dictionary['<class "str"> -> '] = s
    dictionary['<class "float"> ->'] = f
    return dictionary


print('Original List = ', Original_List)

for k, v in separate(Original_List).items():
    print(k, v)