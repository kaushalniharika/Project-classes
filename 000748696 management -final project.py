from Doctor import Doctor
from facility import facility
from Laboratory import Laboratory   
from Patient import Patient

class management :
    def display menu ();
        isback = False
        while True:
            if isback == True:
                print('back to main menu\n')

            print('Welcome to Alberta Hospital management system  ')
            print('Select from the following options,press 0 to stop:')
            print('1= Doctors')
            print('2= Facilities')
            print('3= Laboraties')
            print('4= Patients\n')

            digit = input('\n')

            if digit =='1':
                Management.displaydoctorMenu()
            elif digit == '2':
                Management.displayfacilityMenu()
            elif digit == '3':
                Management.displayLaboratoryMenu()
            elif digit == '4':
                Management.displayPatientMenu()
            elif digit == '0':
                break
            
            else isback = True

def displayDoctorsMenu();
    isback = False
    while True:
        if isback ==True:
            print('Back to previous menu\n')

        print(' Print Patient menu:')
        print('1 - Display patients list')
        print('2 - patient id')
        print('3 - add patient')    
        print('4 - Edit')
        print('5 - Back to main menu\n')

        digit = input(" ")

        if digit == "1":
                Doctor.displayDoctorsList()
        elif digit == "2":
                idSearch = input(" Enter the doctor Id: \n")
                Doctor.searchDoctorById(idSearch)
        elif digit == "3":
                nameSearch = input(" Enter the doctor name: \n")
                Doctor.searchDoctorByName(nameSearch)
        elif digit == "4":
                Doctor.enterDrInfo(Doctor)
        elif digit == "5":
                Doctor.editDoctorInfo()
        elif digit == "6":
                break

            isback = True

def displayFaclityMenu():
    isback = False
    while True:
        if isback == True:
            print('Back to the previous menu\n')
        print('Fac') def displayFacilityMenu():
        isback = False
        while True:
            if isback == True:
                print("\nBack to the previous Menu\n")
            
            print("Facilities Menu:")
            print("1 - Display Facilities list")
            print("2 - Add Facility")
            print("3 - Back to the Main Menu\n")
            
            userinput = input("")
            
            if userinput == "1":
                Facility.displayFacilities()
            elif userinput == "2":
                Facility.addFacility(Facility)
            elif userinput == "3":
                break
            
            isback = True
    
    def displayLaboratoryMenu():
        isback = False
        while True:
            if isback == True:
                print("Back to the previous Menu")
            
            print("Laboratories Menu:")
            print("1 - Display laboratories list")
            print("2 - Add laboratory")
            print("3 - Back to the Main Menu\n")
            
            userInput = input("")
            
            if userInput == "1":
                Laboratory.displayLabList()
            elif userInput == "2":
                Laboratory.enterLaboratoryInfo(Laboratory)
            elif userInput == "3":
                break
            
            isback = True
    
    def displayPatientMenu():
        isback = False
        while True:
            if isback == True:
                print("\nBack to the previous Menu\n")
                
            print("Patient Menu:")
            print("1 - Display patients list")
            print("2 - Search for patient by ID")
            print("3 - Add patient")
            print("4 - Edit patient info")
            print("5 - Back to the Main Menu\n")
            
            userInput = input("")
            
            if userInput == "1":
                Patient.displayPatientsList()
            if userInput == "2":
                idSearch = input("\n Enter the Patient Id: \n")
                Patient.searchPatientById(idSearch)
            if userInput == "3":
                Patient.enterPatientInfo(Patient)
            if userInput == "4":
                Patient.editPatientInfo()
            if userInput == "5":
                break
            
            isback = True