#Create a class “Programmer” for storing information of few programmers  working at Microsoft

class Programmer:
    Company= "Microsoft"
    Country= "Barat"

    def __init__(self,name):
        self.name=name


employerr_1001=Programmer("hemraj bhai")
employerr_1002=Programmer("Tushar bhai")
employerr_1003=Programmer("prithak bhai")
employerr_1004=Programmer("charan bhai")

print(employerr_1001.name,employerr_1001.Company,employerr_1001.Country,"this is detailes for employee 1")
print(employerr_1002.name,employerr_1002.Company,employerr_1002.Country,"this is detailes for employee 2")
print(employerr_1003.name,employerr_1003.Company,employerr_1003.Country,"this is detailes for employee 3")
print(employerr_1004.name,employerr_1004.Company,employerr_1004.Country,"this is detailes for employee 4")


        