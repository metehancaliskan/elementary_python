from doctor import *
def bubble_sort(doctors):
    """
    

    Parameters
    ----------
    doctors : list
  

    Returns
    -------
    doctors : list
        take list and sort the list according to hospital name and specialty.

    """
    for x in range(len(doctors)-1):
        for y in range(0, len(doctors) - (1 + x)):
            if doctors[y].get_hospital() == doctors[y + 1].get_hospital():
                if doctors[y].get_specialty() > doctors[y + 1].get_specialty():
                    doctors[y], doctors[y + 1] = doctors[y + 1], doctors[y]
            
            
            elif doctors[y].get_hospital() > doctors[y + 1].get_hospital():
                
                doctors[y], doctors[y + 1] = doctors[y + 1], doctors[y]
    return doctors


def binary_search(doctors, doctor_id, start_ind, end_ind):
    """
    

    Parameters
    ----------
    doctors : list
    doctor_id : string
    start_ind : integer
        first index of list.
    end_ind : intiger
        last index of list

    Returns
    -------
    intiger
        if given doctor_id is in the doctors list find the index. othereise return -1

    """
    
    
    if (end_ind >= start_ind):

        mid = start_ind + (end_ind - start_ind) // 2

        if (doctors[mid].get_doctor_id() == doctor_id):
            return mid
        elif (doctors[mid].get_doctor_id() > doctor_id):

            return binary_search(doctors, doctor_id, start_ind, mid - 1)
        else:

            return binary_search(doctors, doctor_id, mid + 1, end_ind)

    return -1

def read_doctors(file_name):
    """
    

    Parameters
    ----------
    file_name : string
   

    Returns
    -------
    doctors : list
        read the file and split it according to ';' after call the Doctor class and give the data in file to Doctor class.

    """
    
    doctors = []
    file = open(file_name, "r")
    for line in file:
        line = line.strip()
        line = line.split(';')
        doctors.append(Doctor(line[0], line[1], line[2], line[3]))
    file.close()
    return doctors


doctors = read_doctors("doctors.txt")
doctors.sort()
doctor_id = input("Enter id of doctor to search: ")
ind = binary_search(doctors, doctor_id, 0, len(doctors))
if (ind == -1):
    print("No such doctor")
else:
    print("Doctor with id", doctor_id)
    print(doctors[ind])
print("Doctors by Hospital and Specialty:")
for i in bubble_sort(doctors):
    print(i)
 