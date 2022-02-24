class Doctor:
    def __init__(self, doctorid, doctorname, special, consultationfee):
        self.doctorid = doctorid
        self.doctorname = doctorname
        self.special = special
        self.consultationfee = consultationfee
class Hospital(Doctor):
    def __init__(self, doctorDB):
        super().__init__(doctorid, doctorname, special, consultationfee)
        self.doctorDB = doctorDB  
    def searchByDoctorName(self, doctorName_searchFor):
        self.doctorName_searchFor = doctorName_searchFor
        listing = []
        for i in doctorDB.keys():           
            if i==doctorName_searchFor:
                listing.append(i)
        if len(listing)!=0:
            return doctorDB[doctorName_searchFor]
    def calculateConsultationFeeBySpecialization(self, special_new):
        total = 0
        for i in doctorDB.values():
            if special_new==i[2]:
                total = total + i[3]
        return total

n = int(input())
doctorDB = {}

for i in range(n):
    doctorid = int(input())
    doctorname = input()
    special = input()
    consultationfee = int(input())
    doctorDB[doctorname] = doctorid, doctorname, special, consultationfee

doctorName_searchFor = input()
special_new = input()

name_info = Hospital(doctorDB).searchByDoctorName(doctorName_searchFor)
print(name_info[0])
print(name_info[1])
print(name_info[2])
print(name_info[3])

fee_info = Hospital(doctorDB).calculateConsultationFeeBySpecialization(special_new)
print(fee_info)

