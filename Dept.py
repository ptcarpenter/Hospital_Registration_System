from Patients import Patients
from SQL_Service import SQL_Service


class Department:
    def __init__(self, title, sll_patient_list):
        self.title = title
        self.sll_patient_list = sll_patient_list

# add_patient method allows staff to enter patient details via input including description of the condition
# priority score is automatically set to zero and treatment is set to 'Not treated'
# the patient is then instantiated as an object in the Patients class and added to the singly linked list
    def add_patient(self):
        print("********** New Patient Details **********")
        pps = input("Enter pps number: ")
        fname = input("Enter first name: ")
        lname = input("Enter last name: ")
        age = int(input("Enter age: "))
        condition = input("Enter condition description: ")
        priority = 0
        treatment = "Not treated"
        patient = Patients(pps, fname, lname, age, condition, priority, treatment)
        self.sll_patient_list.add(patient)

# display_patients method loops through each node in the Department's SLL using a counter
# get_node and get_obj are used to get the details of each individual patient
    def display_patients(self):
        print("********** Patients in A&E Waiting List **********")
        current_size = self.sll_patient_list.size()
        counter = 1
        while counter <= current_size:
            tmp_node = self.sll_patient_list.get_node(counter)
            tmp_patient = tmp_node.get_obj()
            tmp_patient.display_info()
            counter = counter + 1

# triage_patient allows triage nurse to input priority scores
# It does so by looping through the SLL and pulling out the patient details
# The triage nurse can then input the priority for the first patient in the list whose priority is currently zero
# The break ensures that the nurse can only triage one patient at a time
    def triage_patient(self):
        current_size = self.sll_patient_list.size()
        counter = 1
        while counter <= current_size:
            tmp_node = self.sll_patient_list.get_node(counter)
            tmp_patient = tmp_node.get_obj()
            if tmp_patient.priority == 0:
                tmp_patient.priority = int(
                    input(f"Enter priority score for {tmp_patient.fname} {tmp_patient.lname} (1-10): "))
                break
            else:
                counter = counter + 1

# treat_patient also works by looping through the SLL and pulling out patient details for each node in the list
# Firstly, it checks if there are any patients currently on the waiting list. If not, it prints out a message saying so
# Patient info is extracted using get_node and get_obj, pos_treat is used to keep track of the location of each node
# The method compares priority scores of every patient in the list and returns the patient with the highest one
# The doctor then enters the treatment details via input and the patient is returned and removed from the SLL
    def treat_patient(self):
        tmp_treat = None
        pos_treat = 0
        current_size = self.sll_patient_list.size()
        counter = 1
        if current_size > 0:
            while counter <= current_size:
                tmp_node = self.sll_patient_list.get_node(counter)
                tmp_patient = tmp_node.get_obj()
                if tmp_treat is None:
                    tmp_treat = tmp_patient
                    pos_treat = 1
                else:
                    if tmp_patient.priority > tmp_treat.priority:
                        tmp_treat = tmp_patient
                        pos_treat = counter
                counter = counter + 1
            print(f"Patient: {tmp_treat.fname} {tmp_treat.lname}, Condition: {tmp_treat.condition}")
            tmp_treat.treatment = input(f"Enter treatment details: ")
            self.sll_patient_list.remove(pos_treat)
            return tmp_treat
        else:
            print("Waiting list is empty")

# display_menu method allows the hospital staff to select required functionality via input
    def display_menu(self):
        menu = """Please select one of the following options:
        1) Add new patient.
        2) Triage patient.
        3) Treat patient.
        4) Display waiting list.
        5) Exit.

        Your selection: """

# The user enters their selected option and a while loop cycles through the options calling the method which matches.
# The while loop will run continuously allowing the user to perform multiples tasks and terminates when '5' is entered
# After a patient has been treated, their details are stored in a file which the user specifies via input
# This file is an object in the SQL_Service class
# The input approach allows for different files to be used to store patient details by different depts in the hospital
# If there are no patients in the waiting list then nothing is exported to the file.
        while True:
            user_input = input(menu)
            if user_input == "1":
                self.add_patient()
            elif user_input == "2":
                self.triage_patient()
            elif user_input == "3":
                tmp = self.treat_patient()
                if tmp is not None:
                    sql_obj = SQL_Service(input("Please enter file name to store patient details: "))
                    sql_obj.add_patient(tmp.pps, tmp.fname, tmp.lname, tmp.age, tmp.condition, tmp.priority, tmp.treatment)
            elif user_input == "4":
                self.display_patients()
            elif user_input == "5":
                print("Exit")
                break
            else:
                print("Invalid input")
