# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 12:02:17 2020

@author: User
"""

import datetime


class Patient(object):
    __hospitalFee = 200

    def __init__(self, pName, isInsured, coveragePercent):
        """


        Parameters
        ----------
        pName : string
            stores the string name of the patient.
        isInsured : string
            boolean field that indicates if patient has private insurance.
        coveragePercent : float
            stores the percent (as decimal value) of the
patient’s insurance coverage. Zero if not insured.

        Returns
        -------
        None.

        """

        self.__pName = pName
        self.__isInsured = isInsured
        self.__coveragePercent = 0.0
        if (self.__isInsured == 'True'):
            self.set_coveragePercent(coveragePercent)

    def get_pName(self):
        """


        Returns
        -------
        string

        """

        return self.__pName

    def set_pName(self, new_name):
        """


        Parameters
        ----------
        new_name : string

        Returns
        -------
        None.

        """

        self.__pName = new_name

    def get_isInsured(self):
        """


        Returns
        -------
        str
            if there is a insurance return yes.Otherwise return no

        """

        if (self.__isInsured == 'True'):
            return 'yes'
        else:
            return 'no'

    def set_isInsured(self, insurance):
        """


        Parameters
        ----------
        new_isInsured : string

        Returns
        -------
        None.

        """

        self.__isInsured = insurance

    def get_coveragePercent(self):
        """


        Returns
        -------
        float.

        """
        return self.__coveragePercent

    def set_coveragePercent(self, percent):
        """


        Parameters
        ----------
        percent : float
        calculate the deduction of percent
        Returns
        -------
        None.

        """

        if percent > 0:
            self.__coveragePercent = percent / 100

    def get_hospitalFee(self):
        """


        Returns
        -------
        float.

        """

        return self.__hospitalFee

    def __repr__(self):
        """


        Returns
        -------
        s : string.
        represent the parameter in init function

        """

        if (self.__isInsured == 'True'):
            s = 'Patient Name:' + self.__pName + ' ' + 'Insurence:"(yes)"'
            return s
        else:
            s = 'Patient Name:' + self.__pName + ' ' + 'Insurence:"(no)"'
            return s

    def calculateFee(self):
        """


        Returns
        -------
        float
            calculate the hospital fee.

        """

        if (self.__isInsured == 'True'):
            return Patient.__hospitalFee - Patient.__hospitalFee * self.__coveragePercent
        else:
            return self.__hospitalFee


class OutPatient(Patient):
    def __init__(self, name, appointmentDate, appointmentTime, doctorName, polyClinic, insurance, coverage_percent):
        """


        Parameters
        ----------
        name : string
        appointmentDate : string
        stores the date of the appointment.
        appointmentTime : string
            stores the time of the appointment.
        doctorName : string
            DESCRIPTION.
        polyClinic : string
            stores the string name of the poly clinic for the patient’s
        appointment.
        insurance : string
        coverage_percent : float

        Returns
        -------
        None.

        """

        if polyClinic == "Dentistry" or polyClinic == "Optometry":
            coverage_percent /= 2
        Patient.__init__(self, name, insurance, coverage_percent)
        self.__polyClinic = polyClinic
        self.__doctorName = doctorName
        self.__appointmentTime = appointmentTime
        self.set_appointmentDate(appointmentDate)

    def get_polyClinic(self):
        """


        Returns
        -------
        string.

        """

        return self.__polyClinic

    def set_polyClinic(self, new_polyClinic):
        """


        Parameters
        ----------
        new_polyClinic : string

        Returns
        -------
        None.

        """

        self.__polyClinic = new_polyClinic

    def get_doctorName(self):
        """


        Returns
        -------
        string

        """

        return self.__doctorName

    def set_doctorName(self, new_Name):
        """


        Parameters
        ----------
        new_doctorName : string

        Returns
        -------
        None.

        """

        self.__doctorName = new_Name

    def get_appointmentTime(self):
        """


        Returns
        -------
        string

        """

        return self.__appointmentTime

    def set_appointmentTime(self, new_appointmentTime):
        """


        Parameters
        ----------
        new_appointmentTime : string

        Returns
        -------
        None.

        """

        self.__appointmentTime = new_appointmentTime

    def get_appointmentDate(self):
        """


        Returns
        -------
        integer

        """

        return self.__appointmentDate

    def set_appointmentDate(self, new_Date):
        """


        Parameters
        ----------
        new_appointmentDate : string
            arrange the date.

        Returns
        -------
        None.

        """

        self.__appointmentDate = datetime.datetime.strptime(new_Date, '%Y%m%d').date()

    def __lt__(self, other):
        """


        Parameters
        ----------
        other : integer

        Returns
        -------
        bool

        """

        if self.__appointmentDate != other.__appointmentDate:
            return self.__appointmentDate < other.__appointmentDate
        else:
            return self.__appointmentTime < other.__appointmentTime

    def __repr__(self):
        """


        Returns
        -------
        s : string
            represent the parameters in outpatient class.

        """

        s = 'Appointment Date:' + str(self.__appointmentDate) + ' ' + self.__appointmentTime + '\n'
        s += Patient.__repr__(self) + '\n'
        s += 'Poly Clinic:' + self.__polyClinic + ' ' + '(Dr. {})'.format(self.__doctorName) + '\n'
        s += 'Fee:' + ' ' + str(Patient.calculateFee(self))
        return s