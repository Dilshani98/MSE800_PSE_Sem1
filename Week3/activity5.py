import sqlite3

class QueryData:
    def __init__(self, specialisation, patient_age, connnection):
        self.specialisation = specialisation
        self.patient_age = patient_age
        self.connection = connnection
    

    #Display the total number of doctors who specialise in ophthalmology
    def getCount_of_specialists(self):
        conn = self.connection
        cursor = conn.cursor()
        
        select_statement = "SELECT COUNT(d.doctor_id) as doctor_count FROM doctor d where d.specialisation=?;"

        cursor.execute(select_statement, (self.specialisation,))
        row = cursor.fetchone()
        
        return row[0] if row else 0
    

    #List the full information of all patients who are classified as seniors in the clinic
    def listSeniorPatients(self):
        conn = self.connection
        cursor = conn.cursor()
        
        select_statement = """
        SELECT * 
        FROM patient
        WHERE age > ?;
        """

        cursor.execute(select_statement, (self.patient_age,))
        rows = cursor.fetchall()

        return rows
    

def initiateDatabase(connection):
    conn = connection

    cursor = conn.cursor() # create cursor object to execute sql commands

    #define commands
    sql_CreatePrimaryTable_statement = [
    """CREATE TABLE IF NOT EXISTS doctor (
        doctor_id INTEGER PRIMARY KEY,
        first_name VARCHAR,
        last_name VARCHAR,
        specialisation VARCHAR,
        contact_no VARCHAR,
        email VARCHAR
    );""",
                
    """CREATE TABLE IF NOT EXISTS patient (
        patient_id INTEGER PRIMARY KEY,
        first_name VARCHAR,
        last_name VARCHAR,
        age INTEGER,
        gender VARCHAR,
        contact_no VARCHAR,
        address VARCHAR
    );""",

    """CREATE TABLE IF NOT EXISTS appointment (
        appointment_id INTEGER PRIMARY KEY,
        date DATE,
        reason VARCHAR,
        patient_id INTEGER,
        doctor_id INTEGER,
        FOREIGN KEY (patient_id) REFERENCES patient(patient_id),
        FOREIGN KEY (doctor_id) REFERENCES doctor(doctor_id)
        );"""
    ]

    #drop databases if exists
    cursor.execute("DROP TABLE IF EXISTS doctor;")# Drop existing tables
    cursor.execute("DROP TABLE IF EXISTS patient;")
    cursor.execute("DROP TABLE IF EXISTS appointment;")


    #execute create Tables commands
    for statement in sql_CreatePrimaryTable_statement:
        cursor.execute(statement)

    conn.commit()


def insertInitialData(connection, doctor_data, patient_data, appointment_data):
    conn = connection 

    cursor = conn.cursor() # create cursor object to execute sql commands

    # Insert Data into primary tables
    cursor.executemany("INSERT INTO doctor VALUES(?, ?, ?, ?, ?, ?)", doctor_data)
    cursor.executemany("INSERT INTO patient VALUES(?, ?, ?, ?, ?, ?, ?)", patient_data)
    cursor.executemany("INSERT INTO appointment VALUES(?, ?, ?, ?, ?)", appointment_data)

    conn.commit()


def main():

    filePath = "ClinicSystemDB.db"

    db_connection = sqlite3.connect(filePath) #create database connection

    initiateDatabase(db_connection)

    # define Data
    doctor_data = [
        (1, 'Dr. Anne', 'Fernando', 'Ophthalmology', '+6420771112222', 'anne@clinic.com'),
        (2, 'Dr. Ravi', 'Perera', 'Cardiology', '+6420773334444', 'ravi@clinic.com'),
        (3, 'Dr. Saman', 'Jayasinghe', 'Ophthalmology', '+6420775556666', 'saman@clinic.com')
    ]

    patient_data = [
        (1, 'Nimal', 'Perera', '68', 'Male', '0771234567', 'Colombo'),
        (2, 'Kamal', 'Silva', '72', 'Male', '0719876543', 'Kandy'),
        (3, 'Sunitha', 'Fernando', '45', 'Female', '0754567890', 'Galle')
    ]

    appointment_data = [
        (1, '2025-12-01', 'Eye check-up', 1, 1),
        (2, '2025-12-02', 'Heart consultation', 2, 2),
        (3, '2025-12-03', 'Vision test', 3, 3)
    ]


    insertInitialData(db_connection,doctor_data, patient_data, appointment_data)

    specialization = "Ophthalmology"
    age_limit = 65  

    filter_obj = QueryData(specialization,age_limit, db_connection) #create QueryData object

    doctor_count = filter_obj.getCount_of_specialists()
    print(f"Total doctors who specialized in ophthalmology: {doctor_count}")

    seniorPatients = filter_obj.listSeniorPatients()
    print("Senior Patients:")
    for patient in seniorPatients:
        print(f"ID: {patient[0]}, Name: {patient[1]}, Email: {patient[2]}")

    db_connection.close()

if __name__ == "__main__":
    main()
