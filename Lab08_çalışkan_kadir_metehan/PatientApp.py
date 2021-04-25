# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 12:17:51 2020

@author: User
"""

from Patient import *
import datetime


def schedulePatients(fileName):
    """


    Parameters
    ----------
    fileName : string
        contain all data.

    Returns
    -------
    outpatient : list
        Outpatients containing the patient data from the input file

    """

    outpatient = []
    file = open(fileName, 'r', encoding='utf-8')
    for line in file:
        line = line.strip()
        line = line.split(';')

        if line[5] == "True":
            OP = OutPatient(line[0], line[1], line[2], line[3], line[4], line[5],
                            float(line[6]))

        elif line[5] == "False":
            OP = OutPatient(line[0], line[1], line[2], line[3], line[4], line[5], 0)

        outpatient.append(OP)
    file.close()
    return outpatient


list_patients = schedulePatients('patients.txt')
list_patients.sort()
for i in list_patients:
    print(i)

