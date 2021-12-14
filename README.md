from datetime import datetime
from datetime import date


Students = {}
Modules = {}
Units = dict([])
class manager:
    global Students
    global Modules
    global Unit

    def __init__(self):
        self.Manager_menu()
        pass
    def Manager_menu(self):
        print("select your options, Manager! \n 1.Manage Modules \n 2.Manage units \n 3.Manage Students \n 4.Logout")
        i = int(input("enter your number\n"))
        while i not in range(1,4):
            if i == 4:
                quit()
                break
            else:
                print("please enter a valid number\n")
                i = int(input("please enter your choice , make sure that the number between 1 to 5"))
        else:
            if i == 1:
                self.Manage_modules()
                self.Manager_menu()
            elif i == 2:
                self.Manage_units()
                self.Manager_menu()
            elif i == 3:
                self.Manage_students()
                self.Manager_menu()
    def Manage_students(self):
        print("select your options,mange_students menu! \n 1.create student\n 2.view students\n 3.update student\n 4.delete student\n 5.v_students\n 6.quit")
        i = int(input("enter the number\n"))
        while (i not in range(1,6)):
            if i == 6:
                quit()
                break
            else:
                print("enter a valid number, make sure that the number between 1 to 5\n")
                i = int(input("enter the number: "))
        else:
            if i == 1:
                self.create_student()
                self.Manage_students()
            if i == 2:
                self.view_student()
                self.Manage_students()
            if i == 3:
                self.update_student()
                self.Manage_students()
            if i == 4:
                self.delete_student()
                self.Manage_students()
            if i == 5:
                self.v_students()
                self.Manage_students()
    def create_student(self):
        print("Okay, lets create a new student")
        num = input("please enter contact number if student does not exist!\n")
        while num in Students:
            print("it seems the student already exist\n")
            break
        else:
            Students[num] = {}
            print(" okay seems like the student does not exist! please enter the details")
            full_name = input("please enter full name of student!:\n")
            Students[num]["full name"] = full_name
            age = input("please enter the age\n")
            while (age.isdigit() == False):
                age = input("enter age in numbers only")
            Students[num]["Age"] = age
            gender = input("enter your gender")
            while (gender not in ["male","MALE","m","M","Female","FEMALE","F","f","others","o","O"]):
                gender = input("please enter your gender m,f,o\n")
            Students[num]["Gender"] = gender

            Students[num]["contactnumber"] = num

            email = input("enter your email address!\n")
            Students[num]["email"] = email
            module = input("enter the course, what he/she want!")
            Students[num]["module"] = module
    def view_student(self):
        check = input("please enter contact number of the student\n")
        if check in Students:
            print("the details of the student is: ")
            for detail in Students[check]:
                if type(Students[check][detail]) != dict:
                    print("{},{}".format(detail,Students[check][detail]))
                else:
                    print(detail + ":")
                    for j in Students[check][detail]:
                        print("{},{}".format(detail,Students[check][detail][j]))
                
        else:
            print("sorry, the student details does not exist\n")
        print("let's go back to the main menu\n\n")
    
    def v_students(self):
        for i,x in Students.items():
            print(i,x)
            

    def update_student(self):
        check = input("please enter the contact number of student: ")
        if check in Students:
            print("here are the details")
            label = 1
            for i in Students[check]:
                print("{},{}".format(label,i))
                label += 1
            val = input("please enter the name of details you want to update")
            while (val not in Students[check]):
                print("this details not present for this student\n\n")
                break
            else:
                if val == "module":
                    print("select change module or revoke student")
                    n = int(input("1.change module \n 2.revoke student"))
                    while (n not in range(1,3)):
                        n = int(input("please enter number either 1 or 2"))
                    else:
                        if n == 1:
                            module = input("enter the course name do you want! ")
                            Students[check]["module"] = module
                            print("you sucessfully changed module")
                        elif n == 2:
                            self.delete_student(check)
                            print("student has been sucessfully deleted")
        print("Lets go back to main menu!\n\n")

    def delete_student(self):
        num = input("enter the contact number")
        if num in Students:
            del Students[num]
        else:
            print("the student does not exist")
        print("lets go back to main menu")
    def Manage_modules(self):
        print("select your options! in modules \n 1.create module \n 2.list of modules\n 3.show module\n 4.delete module\n 5.show detailed module\n 6.quit")
        i = int(input("enter the number\n"))
        while (i not in range(1,6)):
            if i == 6:
                quit()
                break
            else:
                print("enter a valid number, make sure that the number between 1 to 3\n")
                i = int(input("enter the number: "))
        else:
            if i == 1:
                self.create_module()
                self.Manage_modules()
            if i == 2:
                self.view_module()
                self.Manage_modules()
            if i == 3:
                self.show_modules()
                self.Manage_modules()
            if i == 4:
                self.delete_module()
                self.Manage_modules()
            if i == 5:
                self.view_detailed_module()
                self.Manage_modules()
    def create_module(self):
        print("Okay, lets create a new module")
        num = input("please enter module key does not exist!\n")
        while num in Modules:
            print("it seems the module already exist\n")
            break
        else:
            Modules[num] = {}
            print(" okay seems like the module does not exist! please enter the details")
            Module_name = input("please enter module name!:\n")
            Modules[num]["module name"] = Module_name
            
            Modules[num]["id"] = num
            start_date = input("enter the starting date of module ")
            Modules[num]["startdate"] = start_date
            end_date = input("enter the closing date: ")
            Modules[num]["end date"] = end_date
            units = input("enter the number of units")
            Modules[num]["units"] = units
            date = input("please enter today's date")
            Modules[num]["date"] = date
            i = ["upcoming","ongoing","complete"]
            if date < start_date:
                n = i[0]
                print(i[0])
            
            elif date <= end_date:
                n = i[1]
                print(i[1])
            
            else:
                n = i[2]
                print(i[2])
            status = n
            Modules[num]["status"] = status
    def view_module(self):
        check = input("please enter module name\n")
        if check in Modules:
            print("the details of the module is: ")
            for detail in Modules[check]:
                if type(Modules[check][detail]) != dict:
                    print("{},{}".format(detail,Modules[check][detail]))
                else:
                    print(detail + ":")
                    for j in Modules[check][detail]:
                        print("{},{}".format(detail,Modules[check][detail][j]))
        else:
            print("sorry, the module details does not exist\n")
        print("let's go back to the main menu\n\n")
        
    def show_modules(self):
        module_list = Modules.keys()
        print("choose modules")
        temp = input(module_list)
        if temp not in module_list:
            print("please choose from available from above module list")
            return show_module()
        else:
            return temp
    
    def delete_module(self):
        num = input("please enter contact number")
        if num in Modules:
            del Modules[num]
        else:
            print("the module does not exist")
        print("lets go back to main menu")
        
    def Manage_units(self):
        print("select your options! in units \n 1.create unit \n 2. choose units\n 3.update unit\n 4.delete unit\n 5.quit")
        i = int(input("enter the number\n"))
        while (i not in range(1,5)):
            if i == 5:
                quit()
                break
            else:
                print("enter a valid number, make sure that the number between 1 to 5\n")
                i = int(input("enter the number: "))
        else:
            if i == 1:
                self.create_unit()
                self.Manage_units()
            if i == 2:
                self.choose_unit()
                self.Manage_units()
            if i == 3:
                self.view_all_units()
                self.Manage_units()
            if i == 4:
                self.delete_unit()
                self.Manage_units()
    def create_unit(self):
        unit_list = list(Modules.keys())
        print("Okay, lets create a new unit")
        num = input("please enter unit key does not exist!\n")
        while num in Units:
            print("it seems the unit already exist\n")
            break
        else:
            Units[num] = {}
            print(" okay seems like the module does not exist! please enter the details")
            unit_name = input("please enter module name!:\n")
            Units[num]["unit name"] = unit_name
            unit_type = input("the the type of unit\n")
            Units[num]["type"] = unit_type
            
            Units[num]["id"] = num
            start_date = input("enter the starting date of module\n ")
            Units[num]["startdate"] = start_date
            end_date = input("enter the closing date: \n")
            Units[num]["end date"] = end_date
            
    def choose_unit():
        unitlist = (Units.keys())
        print("choose the unit")
        tempn = input(unitlist)
        if tempn not in unitlist:
            print("please choose freom available units")
            return choose_unit()
        else:
            return tempn
    def view_all_units():
        print("the list of units")
        for i in Units:
            print(i)
    def delete_unit(self):
        num = input("enter the contact number")
        if num in Units:
            del Units[num]
        else:
            print("the units does not exist")
        print("lets go back to main menu")
        
        
class student:
    def __init__(self):
        self.num = input("please enter the contact number: ")
        if self.num in Students:
            print("welcome {} to killer's digital university".format(Students[self.num]["full name"]))
            self.student_menu()
        else:
            print("sorry, your details are not found\n please ask the manager to add your details")
    def student_menu(self):
        print("please choose one of the options\n 1.Today sechudule\n 2.view my modules\n 3.update profile\n 4.logout")
        i = int(input())
        while i not in range(1,4):
            if i == 4:
                login()
                break
                i = int(input("please enter a valid number 1 or 2 or 3"))
            else:
                if i == 1:
                    self.view_module()
                    self.student_menu()
                if i == 2:
                    self.update_profile()
                    self.student_menu()
                if i == 3:
                    self.student_profile()
                    self.student_menu()
    def student_profile(self):
        print("your! complete profile is : ")
        for i in Students[self.num]:
            if i != "module":
                print("{}:{}".format(i,Students[self.num][i]))
            else:
                pass
    def update_profile(self):
        check = input("please enter the contact number of student: ")
        if check in Students:
            print("here are the details")
            label = 1
            for i in Students[check]:
                print("{},{}".format(label,i))
                label += 1
            val = input("please enter the name of details you want to update")
            while (val not in Students[check]):
                print("this details not present for this student\n\n")
                break
            else:
                print("select change name or change email")
                n = int(input("1.change name \n 2.change email\n"))
                while (n not in range(1,3)):
                    n = int(input("please enter number either 1 or 2"))
                else:
                    if n == 1:
                        name = input("enter the name do you want! ")
                        Students[check]["full name"] = full_name
                        print("you sucessfully changed name")
                    elif n == 2:
                        email = input("enter e mail")
                        Students[check]["email"] = email
                        print("you sucessfully change email ")
        print("Lets go back to main menu!\n\n")
        
    def view_my_modules(self):
        check = input("please enter module name\n")
        if check in Modules:
            print("the details of the module is: ")
            for detail in Modules[check]:
                if type(Modules[check][detail]) != dict:
                    print("{},{}".format(detail,Modules[check][detail]))
                else:
                    print(detail + ":")
                    for j in Modules[check][detail]:
                        print("{},{}".format(detail,Modules[check][detail][j]))
        else:
            print("sorry, the module details does not exist\n")
        print("let's go back to the main menu\n\n")

        
        
        
        
        
def login():
    print("welcome to Switch_Blade's Academy".center(100,"*"))
    i = int(input("please choose one of the following to login\n 1.manager\n 2.student\n"))
    while i not in range(1,3):
        print('please enter valid number to login\n')
        i = int(input())
    else:
        if i == 1:
            print('please enter your username and password')
            username=input()
            password=input()
            while username!='admin' or password!='admin':
                print('please enter valid username and password')
                username=input()
                password=input()
            else:
                print('welcome manager')
            obj = manager()

        else:
            i == 2
            obj1 = student()
login()
