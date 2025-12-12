import sqlite3

class FilterData:
    def __init__(self, course1_id, course2_id, connnection):
        self.course1_id = course1_id
        self.course2_id = course2_id
        self.connection = connnection
    
    def countStudentsInCourse(self):
        conn = self.connection
        cursor = conn.cursor()
        
        select_statement = "SELECT COUNT(sc.student_id) as student_count FROM student_course sc where course_id=?;"

        cursor.execute(select_statement, (self.course1_id,))
        row = cursor.fetchone()
        
        return row[0] if row else 0
    
    def listTeachersInCourse(self):
        conn = self.connection
        cursor = conn.cursor()
        
        select_statement = """
        SELECT t.id, t.name, t.email 
        FROM teacher t
        JOIN teacher_course tc ON t.id = tc.teacher_id
        WHERE tc.course_id = ?;
        """

        cursor.execute(select_statement, (self.course2_id,))
        rows = cursor.fetchall()

        return rows
    

def initiateDatabase(connection):
    conn = connection

    cursor = conn.cursor() # create cursor object to execute sql commands

    #define commands
    sql_CreatePrimaryTable_statement = [
    """CREATE TABLE IF NOT EXISTS teacher (
    id INTEGER PRIMARY KEY,
    name varchar,
    email varchar
    );""",
                
    """CREATE TABLE IF NOT EXISTS student (
        id INTEGER PRIMARY KEY,
        name varchar,
        email varchar
    );""",

    """CREATE TABLE IF NOT EXISTS course (
        id INTEGER PRIMARY KEY,
        title varchar,
        description varchar
    );"""
    ]

    sql_CreatemanyToManyTables_statement = [
        """CREATE TABLE IF NOT EXISTS teacher_course (
        teacher_id INTEGER,
        course_id INTEGER,
        PRIMARY KEY (teacher_id, course_id),
        FOREIGN KEY (teacher_id) REFERENCES teacher(id),
        FOREIGN KEY (course_id) REFERENCES course(id)
    );""",
                
    """CREATE TABLE IF NOT EXISTS student_course (
        student_id INTEGER,
        course_id INTEGER,
        PRIMARY KEY (student_id, course_id),
        FOREIGN KEY (student_id) REFERENCES student(id),
        FOREIGN KEY (course_id) REFERENCES course(id)
    );"""
    ]

    #drop databases if exists

    cursor.execute("DROP TABLE IF EXISTS student;")# Drop existing tables
    cursor.execute("DROP TABLE IF EXISTS teacher;")
    cursor.execute("DROP TABLE IF EXISTS course;")
    cursor.execute("DROP TABLE IF EXISTS student_course;")
    cursor.execute("DROP TABLE IF EXISTS teacher_course;")

    #execute create Tables commands
    for statement in sql_CreatemanyToManyTables_statement:
        cursor.execute(statement)

    for statement in sql_CreatePrimaryTable_statement:
        cursor.execute(statement)

    conn.commit()


def insertInitialData(connection, teacher_data, student_data, course_data, teacher_course_data, student_course_data):
    conn = connection 

    cursor = conn.cursor() # create cursor object to execute sql commands

    # Insert Data into primary tables
    cursor.executemany("INSERT INTO teacher VALUES(?, ?, ?)", teacher_data)
    cursor.executemany("INSERT INTO student VALUES(?, ?, ?)", student_data)
    cursor.executemany("INSERT INTO course VALUES(?, ?, ?)", course_data)

    # Insert Data into many to many tables
    cursor.executemany("INSERT INTO teacher_course VALUES(?, ?)", teacher_course_data)
    cursor.executemany("INSERT INTO student_course VALUES(?, ?)", student_course_data)

    conn.commit()


def main():

    filePath = "YB_College.db"

    db_connection = sqlite3.connect(filePath) #create database connection

    initiateDatabase(db_connection)

    # define Data
    teacher_data = [
        (1, 'Alice', 'alice@example.com'),
        (2, 'Brian', 'brian@example.com'),
        (3, 'Chamari', 'chamari@example.com')
    ]

    student_data = [
        (1, 'Nimal', 'nimal@student.com'),
        (2, 'Kavindu', 'kavindu@student.com'),
        (3, 'Dinithi', 'dinithi@student.com'),
        (4, 'Ashen', 'ashen@student.com')
    ]

    course_data = [
        (1, 'Database Systems', 'Introduction to SQL, schema design, and data modeling'),
        (2, 'Software Engineering', 'Principles of software development and project management'),
        (3, 'Data Structures', 'Core algorithms and data structures with practical examples')
    ]

    teacher_course_data = [
        (1, 1), 
        (1, 2), 
        (2, 1),
        (2, 3),
        (3, 2)
    ]

    student_course_data = [
        (1, 1),  
        (1, 2),
        (2, 1),
        (3, 2),
        (3, 3), 
        (4, 1)
    ]

    insertInitialData(db_connection,teacher_data, student_data, course_data, teacher_course_data, student_course_data)

    filter_obj = FilterData(1,2, db_connection)

    student_count = filter_obj.countStudentsInCourse()
    print(f"Total students enrolled in course 1: {student_count}")

    teachers = filter_obj.listTeachersInCourse()
    print("Teachers teaching course 2:")
    for teacher in teachers:
        print(f"ID: {teacher[0]}, Name: {teacher[1]}, Email: {teacher[2]}")

    db_connection.close()

if __name__ == "__main__":
    main()
