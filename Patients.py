class Patients:
    def __init__(self, pps, fname, lname, age, condition, priority, treatment):
        self.pps = pps
        self.fname = fname
        self.lname = lname
        self.age = age
        self.condition = condition
        self.priority = priority
        self.treatment = treatment

    def display_info(self):
        print(f"{self.fname} {self.lname}, Priority score: {self.priority}")
