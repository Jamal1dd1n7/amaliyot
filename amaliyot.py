import psycopg2

class DataBase:
    def __init__(self):
        self.database = psycopg2.connect(
            database='postgres',
            user='postgres',
            host='localhost',
            password='252208'
        )
        self.table_names = []

    def manager(self, sql, *args, commit=False, fetchone=False, fetchall=False):
        result = None
        with self.database as db:
            with db.cursor() as cursor:
                cursor.execute(sql, args)
                if commit:
                    db.commit()
                elif fetchone:
                    result = cursor.fetchone()
                elif fetchall:
                    result = cursor.fetchall()
        return result


    def create_teachers(self):
        sql = '''
            CREATE TABLE IF NOT EXISTS teachers(
                teacher_id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
                name VARCHAR(50) NOT NULL,
                experience_years INTEGER CHECK( experience_years >= 0)
            )
        '''
        self.manager(sql, commit=True)

    def create_students(self):
        sql = '''
            CREATE TABLE IF NOT EXISTS students(
                student_id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
                student_name VARCHAR(50) NOT NULL,
                age INTEGER CHECK(age > 0),
                email VARCHAR(255) UNIQUE NOT NULL
            )
        '''
        self.manager(sql, commit=True)

    def create_classes(self):
        sql = '''
            CREATE TABLE IF NOT EXISTS classes(
                class_id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
                teacher_id INTEGER REFERENCES teachers(teacher_id) NOT NULL,
                student_id INTEGER REFERENCES students(student_id) NOT NULL,
            )
        '''
        self.manager(sql, commit=True)

    def insert_teachers(self):
        sql = '''
            INSERT TABLE teachers(name, experience_years) VALUES
            ('Dilshod Nazarov', 10),
            ('Sayyora Akhmedova', 7);
        '''
        self.manager(sql, commit=True)
    
    def insert_students(self):
        sql = '''
            INSERT TABLE students(student_name, age, email)

        '''
        self.manager(sql, commit=True)






















