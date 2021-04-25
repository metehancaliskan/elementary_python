# -*- coding: utf-8 -*-
"""
Created on Thu Nov  5 16:06:04 2020

@author: User
"""

filename = 'words.txt'


def form(filename):
    """


    Parameters
    ----------
    filename : string
        take a file. Read each line and cretates a sentence from the given words by sorting the numbers given at the end of the words in ascending order. 

    Returns
    -------
    sentence : list
       a list containing the composed sentence.

    """

    file = open(filename, 'r', encoding="utf-8")
    numbers = []
    words = []
    sentence = []
    for i in file.readlines():
        i = i.strip()
        i = i.split(' ')
        numbers.append(i[1])
        words.append(i[0])
    for a in range(1, len(numbers) + 1):
        sentence.append(words[numbers.index(str(a))])
    file.close()
    return sentence


for i in form(filename):
    print(i, end=' ')