Students = {}
Modules = {}
Units = {}

class manager:
    global Students
    global Modules
    global Unit

    def __init__(self):
        self.Manager_menu()
        pass

    def Manager_menu(self):
        print("choose your options from below\n 1.Manage Modules \n 2.Manage units \n 3.Manage Students \n 4.Logout")
        i = int(input("select your option: "))
        while i not in range(1, 4):
            if i == 4:
                print('Logging Out')
                login()
                break
            else:
                print("please choose a valid number: ")
                i = int(input("please enter your choice from 1 to 4: "))
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

    def Manage_modules(self):
        print(
            "choose from options to:\n 1.create module \n 2.list of modules\n 3.show module\n 4.delete module\n 5.show detailed module\n 6.Update Module\n 7.exit")
        i = int(input("enter the number to select your option: "))
        while i not in range(1, 7):
            if i == 7:
                self.Manager_menu()
                break
            else:
                print("Enter a valid number to choose from below: ")
                i = int(input("enter the number: "))
        else:
            if i == 1:
                self.create_module()
                self.Manage_modules()
            if i == 2:
                self.view_all_modules()
                self.Manage_modules()
            if i == 3:
                self.view_module_details()
                self.Manage_modules()
            if i == 4:
                self.delete_module()
                self.Manage_modules()
            if i == 5:
                self.view_detailed_modules()
                self.Manage_modules()
            if i == 6:
                self.update_module()
                self.Manage_modules()

    def create_module(self):
        print("Okay!!, lets create a new module")
        num = input("Enter a unique key to create new module: ")
        while num in Modules:
            print("it seems the module already exist\n")
            break
        else:
            Modules[num] = {}
            print("okay seems like module does't exist! please enter the details to create new module")
            Module_name = input("please enter module name to be created: ")
            Modules[num]["module name"] = Module_name

            Modules[num]["id"] = num
            start_date = input("Enter the starting date of module:  ")
            Modules[num]["start_date"] = start_date
            end_date = input("Enter the Ending date: ")
            Modules[num]["End_date"] = end_date
            units = input("enter the number of units: ")
            Modules[num]["units"] = units
            date = input("please enter today's date: ")
            Modules[num]["date"] = date
            i = ["upcoming", "ongoing", "complete"]
            if date < start_date:
                n = i[0]
                print('status: ',n)

            elif date <= end_date or date >= start_date:
                n = i[1]
                print('status: ',n)

            elif date>=end_date:
                n = i[2]
                print('status: ',n)
            status = n
            Modules[num]["status"] = status

    def view_module_details(self):
        check_module = input("please enter module Key: ")
        if check_module in Modules:
            print("the details of the module you selected is: ")
            for detail in Modules[check_module]:
                if type(Modules[check_module][detail]) != dict:
                    print("{}:{}".format(detail, Modules[check_module][detail]))
                else:
                    print(detail + ":")
                    for j in Modules[check_module][detail]:
                        print("{}:{}".format(detail, Modules[check_module][detail][j]))
        else:
            print("sorry, the module details does not exist\n")
        print("let's go back to the main menu\n\n")

    def view_all_modules(self):
        module_list = [key_val for key_val in Modules.keys()]
        print("Available Modules are:", module_list)


    def view_detailed_modules(self):
        for module in Modules:
            print("All the module details are as follows: ")
            for detail in Modules[module]:
                if type(Modules[module][detail]) != dict:
                    print("{}:{}".format(detail, Modules[module][detail]))
                else:
                    print(detail + ":")
                    for j in Modules[module][detail]:
                        print("{}:{}".format(detail, Modules[module][detail][j]))

    def update_module(self):
        check_module = input("please enter module Key: ")
        if check_module in Modules:
            print("Module found! ")
            print("Please enter the content to be updated below")
            Updated_data = {}
            Module_name = input("please enter module name to be updated: ")
            Updated_data["module name"] = Module_name
            start_date = input("Enter the starting date of module:  ")
            Updated_data["start_date"] = start_date
            end_date = input("Enter the Ending date: ")
            Updated_data["End_date"] = end_date
            units = input("enter the number of units: ")
            Updated_data["units"] = units
            date = input("please enter today's date: ")
            Updated_data["date"] = date
            i = ["upcoming", "ongoing", "complete"]
            if date < start_date:
                n = i[0]
                print(i[0])

            elif date <= end_date and date >= start_date:
                n = i[1]
                print(i[1])

            else:
                n = i[2]
                print(i[2])
            status = n
            Updated_data["status"] = status
            dictkey = {check_module:Updated_data}
            Modules.update(dictkey)
            print("update successful")
        else:
            print("sorry, the module details does not exist\n")
        print("let's go back to the main menu\n\n")


    def delete_module(self):
        key = input("please enter Module Key")
        if key in Modules:
            del Modules[key]
        else:
            print("the module does not exist")
        print("lets go back to main menu")


    def Manage_units(self):
        print(
            "select your options! in units \n 1.create unit \n 2.view_all_units\n 3.view_module_details\n 4.update unit\n 5.delete unit\n 6.exit")
        i = int(input("enter the number: "))
        while (i not in range(1, 6)):
            if i == 6:
                break
            else:
                print("enter a valid number, make sure that the number from 1 to 5\n")
                i = int(input("enter the number: "))
        else:
            if i == 1:
                self.create_unit()
                self.Manage_units()
            if i == 2:
                self.view_all_units()
                self.Manage_units()
            if i == 3:
                self.view_unit_details()
                self.Manage_units()
            if i == 4:
                self.update_units()
                self.Manage_units()
            if i == 5:
                self.delete_unit()
                self.Manage_units()

    def create_unit(self):
        module_list = list(Modules.keys())
        print("modules list --> ", module_list)
        print("Okay, lets create a new unit")
        num = input("please enter unit key that's not already used: ")
        while num in Units:
            print("it seems the unit already exist, use unique num\n")
            break
        else:
            Units[num] = {}
            print("okay seems like the module does not exist! please enter the details")
            unit_name = input("please enter unit name!: ")
            Units[num]["unit name"] = unit_name
            unit_type = input("The type of unit?: ")
            Units[num]["type"] = unit_type

            Units[num]["id"] = num
            start_date = input("enter the starting date of module: ")
            Units[num]["startdate"] = start_date
            end_date = input("enter the closing date: ")
            Units[num]["enddate"] = end_date
            module_id = input("enter the module id that this unit will be apart of: ")
            Units[num]["module_id"] = module_id
            date = input("please enter today's date: ")
            Units[num]["date"] = date
            i = ["upcoming", "ongoing", "complete"]
            if date < start_date:
                n = i[0]
                print(i[0])

            elif date <= end_date and date >= start_date:
                n = i[1]
                print(i[1])

            else:
                n = i[2]
                print(i[2])
            status = n
            Units[num]["status"] = status

    def view_all_units(self):
        print("the list of all units")
        for i in Units:
            print("Unit ID =", Units[i]['id'],
                  ", Unit Name =", Units[i]['unit name'],
                  ", Unit Type =", Units[i]["type"],
                  ", Module Name =", Modules[Units[i]['module_id']]["module name"])

    def view_unit_details(self):
        unit_id = input("please enter unit id to view details")
        print("Unit ID =", Units[unit_id]['id'],
              ", Unit Name =", Units[unit_id]['unit name'],
              ", Unit Start Date =", Units[unit_id]['startdate'],
              ", Unit End Date =", Units[unit_id]['enddate'],
              ", Module Name =", Modules[Units[unit_id]['module_id']]["module name"],
              ", Unit Status =", Units[unit_id]["status"],
              )

    def update_units(self):
        check_unit = input("please enter unit Key: ")
        if check_unit in Units:
            print("Unit found! ")
            print("Please enter updated content below")
            Updated_data = {}
            unit_name = input("please enter unit name to be updated: ")
            Updated_data["unit name"] = unit_name
            unit_type = input("please enter unit to be updated: ")
            Updated_data["type"] = unit_type
            unit_id = check_unit
            Updated_data["id"] = unit_id
            start_date = input("Enter the starting date of unit:  ")
            Updated_data["startdate"] = start_date
            end_date = input("Enter the Ending date: ")
            Updated_data["enddate"] = end_date
            module_id = input("Enter the Module ID: ")
            Updated_data["module_id"] = module_id
            date = input("please enter today's date: ")
            Updated_data["date"] = date
            i = ["upcoming", "ongoing", "complete"]
            if date < start_date:
                n = i[0]
                print(i[0])

            elif date <= end_date and date >= start_date:
                n = i[1]
                print(i[1])

            else:
                n = i[2]
                print(i[2])
            status = n
            Updated_data["status"] = status
            dictkey = {check_unit:Updated_data}
            Units.update(dictkey)
            print("update successful")
        else:
            print("sorry, the unit details does not exist\n")
        print("let's go back to the main menu\n\n")


    def choose_unit(self):
        unitlist = (Units.keys())
        print("choose the unit")
        tempn = input("choose the unit")
        if tempn not in unitlist:
            print("please choose from available units")
            choose_unit()
        else:
            return tempn

    def delete_unit(self):
        module_list = list(Modules.keys())
        key = input("enter the Unit key")
        if key in Units:
            del Units[key]
            print('unit has been successfully removed')
        if key in module_list:
            module_list.remove(key)
        else:
            print("the units does not exist")
        print("lets go back to main menu")

    def Manage_students(self):
        print(
            "select your options,mange_students menu! \n 1.create student\n 2.view students\n 3.update student\n 4.delete student\n 5.v_students\n 6.exit")
        i = int(input("enter the number: "))
        while (i not in range(1, 6)):
            if i == 6:
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
        num = input("please enter contact number if student does not exist!: ")
        while num in Students:
            print("it seems the student already exist\n")
            break
        else:
            Students[num] = {}
            print("okay seems like the student does not exist! please enter the details")
            full_name = input("please enter full name of student!: ")
            Students[num]["full name"] = full_name
            age = input("please enter the age: ")
            while (age.isdigit() == False):
                age = input("enter age in numbers only: ")
            Students[num]["Age"] = age
            gender = input("enter your gender: ")
            while (gender not in ["male", "MALE", "m", "M", "Female", "FEMALE", "F", "f", "others", "o", "O"]):
                gender = input("please enter your gender m,f,o: ")
            Students[num]["Gender"] = gender

            Students[num]["contactnumber"] = num

            email = input("enter your email address!: ")
            Students[num]["email"] = email
            module = input("enter the course, what he/she want: ")
            Students[num]["module"] = module

    def view_student(self):
        check = input("please enter contact number of the student: ")
        if check in Students:
            print("the details of the student is: ")
            for detail in Students[check]:
                if type(Students[check][detail]) != dict:
                    print("{},{}".format(detail, Students[check][detail]))
                else:
                    print(detail + ":")
                    for j in Students[check][detail]:
                        print("{},{}".format(detail, Students[check][detail][j]))

        else:
            print("sorry, the student details does not exist\n")
        print("let's go back to the main menu\n\n")

    def update_student(self):
        check_num = input("please enter Student Contact Key\n")
        if check_num in Students:
            print(" Student found")
            print("Please enter updated content below")
            Updated_data = {}
            full_name = input("please enter updated full name of student!: ")
            Updated_data["full name"] = full_name
            age = input("please enter the age: ")
            while (age.isdigit() == False):
                age = input("enter age in numbers only")
            Updated_data["Age"] = age
            gender = input("enter your gender")
            while (gender not in ["male", "MALE", "m", "M", "Female", "FEMALE", "F", "f", "others", "o", "O"]):
                gender = input("please enter your gender m,f,o: ")
            Updated_data["Gender"] = gender
            email = input("enter your email address!: ")
            Updated_data["email"] = email
            module = input("enter the course, what he/she want!")
            Updated_data["module"] = module
            dictkey = {check_num:Updated_data}
            Students.update(dictkey)
            print("update successful")
        else:
            print("sorry, the Student Contact does not exist\n")
        print("let's go back to the main menu\n\n")

    def delete_student(self):
        num = input("enter the contact number: ")
        if num in Students:
            del Students[num]
        else:
            print("the student does not exist")
        print("lets go back to main menu")

    def v_students(self):
        for i, x in Students.items():
            print(i, x)


class student:
    def __init__(self):
        self.num = input("please enter the contact number: ")
        if self.num in Students:
            print(f"welcome ",{Students[self.num]["full name"]}," to Switch_Blade's Academy")
            self.student_menu()
        else:
            print("sorry, your details are not found, please ask the manager to add your details!!")
            login()

    def student_menu(self):
        print(
            "please choose from the below options\n 1.View_Todays_Sechudule\n 2.View_My_Modules\n 3.Update_Profile\n 4.Logout\n")
        i = int(input('please choose from available options: '))
        while i not in range(1, 4):
            if i == 4:
                print('Logging Out')
                login()
                break
            i = int(input("please enter a valid number to choose from available options of 1,2,3 and 4: "))
        else:
            if i == 1:
                self.view_todays_schedule()
                self.student_menu()
            if i == 2:
                self.view_my_modules()
                self.student_menu()
            if i == 3:
                self.update_profile()
                self.student_menu()

    def view_todays_schedule(self):
        num=input('please enter your contact number: ')
        for i in Modules:
            if Modules[i]['status']=='ongoing':
                for i in Students:
                    if num==i:
                        module_name=Students[num]['module']
                        for i in Units:
                            if module_name==Units[i]['module_id']:
                                print(Units[i]['unit name'])
                                print(Units[i]['type'])
                                print(Units[i]['module_id'])

    def update_profile(self):
        contact_num=input('Enter Your Contact Number: ')
        i=int(input('Please choose from the following to update your details\n 1.full name\n 2.Age\n 3.Gender\n 4.contactnumber\n 5.email\n 6.exit: '))
        while i not in range(1,6):
            if i==6:
                break
            else:
                print('please enter a valid number from 1 to 5')
                i=int(input('please enter valid number: '))
        else:
            for num in Students:
                if Students[num]==contact_num:
                    if i==1:
                        Student[num]['full name']=input('update your name: ')
                    elif i==2:
                        Students[num]['Age']=int(input('update your age: '))
                    elif i==3:
                        Students[num]['Gender']=input('update your gender: ')
                    elif i==4:
                        Students[num]['contactnumber']=input('update your contact_no: ')
                    elif i==5:
                        Student[num]['email']=input('update your email: ')

    
    def view_my_modules(self):
        num=input('enter your contact number: ')
        for i in Students:
            if Students[i]['contactnumber']==num:
                print(Students[i]['module'])
            else:
                print("sorry, you are not enrolled to any module!")
        

        
def login():
    print("welcome to Switch_Blade's Academy".center(100, "*"))
    i = int(input("please choose one of the following to login\n 1.manager\n 2.student\n 3.Logout: "))
    while i not in range(1, 3):
        if i==3:
            exit()
        else:
            print('please enter valid number to login\n')
            i = int(input())
    else:
        if i == 1:
            print('please enter your username and password')
            username = input()
            password = input()
            print('welcome manager')
            while username != 'admin' or password != 'admin':
                print('please enter valid username and password')
                username = input()
                password = input()
            
            obj = manager()

        elif i== 2:
            obj1 = student()


login()
