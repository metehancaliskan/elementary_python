class Doctor:

    def __init__(self, dId, dName, dSpec, hosp):
        self.__doctorId = dId
        self.__doctorName = dName
        self.__specialty = dSpec
        self.__hospital = hosp

    def get_doctor_id(self):
        return self.__doctorId

    def set_doctor_id(self, dId):
        self.__doctorId = dId

    def get_doctor_name(self):
        return self.__doctorName

    def set_doctor_name(self, dName):
        self.__doctorName = dName

    def get_specialty(self):
        return self.__specialty

    def set_specialty(self, dSpec):
        self.__specialty = dSpec

    def get_hospital(self):
        return self.__hospital

    def set_hospital(self, hosp):
        self.__hospital = hosp

    def __repr__(self):
        return self.__doctorId + ' ' + self.__doctorName + ' ' + self.__specialty + ' ' + self.__hospital

    def __lt__(self, other):
        return self.__doctorId < other.__doctorId





