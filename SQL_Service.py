import sqlite3


class SQL_Service:
    def __init__(self, filename):
        self.conn = sqlite3.connect(filename)
        self.c = self.conn.cursor()

    def add_patient(self, pps, fname, lname, age, condition, priority, treatment):
        query = f"""INSERT INTO patients (pps, fname, lname, age, condition, priority, treatment) VALUES 
        ('{pps}', '{fname}', '{lname}', {age}, '{condition}', {priority}, '{treatment}')"""
        try:
            self.c.execute(query)
            self.conn.commit()
        except:
            print("Error with SQL insert statement")
